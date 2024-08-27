'''
This code takes a file with the list of pairs of interactions, formated as:
a_pdb,a_rcc1,a_rcc2,a_rcc3,...,a_rcc26,b_pdb,b_rcc1,b_rcc2,b_rcc3,...,b_rcc26
where a_pbd and b_pdb are two interacting proteins.
In this case those input files are called, i.e., 'af_10000_d7Lat.csv' or 'exp_10000_d7Lat.csv'.
and the output files are called, i.e., 'af_d7Lat.csv' or 'exp_d7Lat.csv'.
For full databases, this code removes the headers and the last column (protein CATH classification)
'''

import numpy as np

# Rcc vectors are generated for various contact distances, with or without side chains
conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat']
input_name_str = ['af_10000_','exp_10000_','full_']
separator = ','
models = ['AlphaFold','Experimental','FullPDB']

output_info = open('output_p1_interacting.txt','w') # file to know how many proteins you have
for m in range(len(models)):
	#info = []
	for size in conditions:

		# The names and directory of input and output files can be changed
		# This code asumes it is in the same directory than the input files
		input_file_name = input_name_str[m]+size
		output_dir = models[m]+'/size'+size+'/Interacting/'
		output_file_name = input_name_str[m].split('_')[0]+'_'+size

		input_file = open(input_file_name+'.csv','r')
		# Dictionary to save all pdbs with the corresponding rcc vectors
		pdbs_dict = {}
		complexes = 0
		for line in input_file:
			aux = line.split(separator)
			# Making sure that we know both proteins in the interaction
			if aux[0] != '' and aux[27] != '' and len(aux) > 28:
				# We save the pdbs in the dictionary
				# pdbs_dict[pdb] = [rcc1,rcc2,rcc3,...,rcc26]
				pdbs_dict[aux[0]] = np.array(list(map(int,aux[1:27])))
				pdbs_dict[aux[27]] = np.array(list(map(int,aux[28:])))
				complexes += 1
			elif aux[0] != '' and len(aux) == 28:
				# Here we remove the header for full databases
				if aux[0] != 'PDBID':
					pdbs_dict[aux[0]] = np.array(list(map(int,aux[1:27])))
		input_file.close()

		number_of_pdbs = len(pdbs_dict)

		# We save a list of the proteins
		output_file = open(output_dir+output_file_name+'.txt','w')
		# and save the list of sums of the 26 components for each vector
		output_sums_file = open(output_dir+'sums_'+output_file_name+'.txt','w')

		# Also we store the average values for all components
		average_vector = np.zeros(26)

		# For each item in the dictionary
		for key, value in pdbs_dict.items():
			line_to_print = key # we take the key to start a line to print
			#print(pdbs_dict[key])
			for v in pdbs_dict[key]:
				line_to_print += ','+str(int(v)) # with all its values
			print(line_to_print,file=output_file) # and print the item

			# Here we print the sum of the components in the vector
			information = np.sum(pdbs_dict[key])
			if information == 0: # if there is a null vector
				print(1,file=output_sums_file)	# we asign 1 as information
			else:
				print(information,file=output_sums_file)

			average_vector += pdbs_dict[key]/number_of_pdbs
		output_file.close()
		output_sums_file.close()

		# At this point we have the average values for the 26 components,
		# but we need the standard deviation
		input_file = open(output_dir+output_file_name+'.txt','r')
		deviation_vector = np.zeros(26)
		for line in input_file:
			aux = np.array(list(map(int,line.split(',')[1:])))
			for i in range(26):
				deviation_vector[i] += (aux[i]-average_vector[i])**2
		deviation_vector /= (number_of_pdbs-1)
		input_file.close()

		deviation_vector = deviation_vector**(1/2)

		output_average_file = open(output_dir+'averagesAt_'+output_file_name+'.txt','w')
		for i in range(26):
			print(str(i+1)+separator+str(average_vector[i])+separator+str(deviation_vector[i]),file=output_average_file)
		output_average_file.close()

		# Printing output file
		print('Complexes in '+output_file_name+': '+str(complexes),file=output_info)
		print('Proteins in '+output_file_name+' with at least 1 interaction: '+str(number_of_pdbs),file=output_info)

		# Considering the number of proteins and complexes in the database
		# here is a sugestion of how many and how big the samples could be
		if complexes != 0:
			sample_size = int((2*complexes)**(1/2)+2)
			number_of_samples = (number_of_pdbs*(number_of_pdbs-1))/2-(number_of_pdbs-2)
			number_of_samples = int(number_of_samples/complexes)
		else:
			sample_size = 2000
			number_of_samples = 2500
		print('Recomended sample size:'+str(sample_size),file=output_info)
		print('Recomended number of samples:'+str(number_of_samples),file=output_info)

	print('',file=output_info)
output_info.close()
