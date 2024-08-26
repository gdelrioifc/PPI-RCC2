'''
This code takes a file with the list of pairs of interactions, formated as:
a_pdb,a_rcc1,a_rcc2,a_rcc3,...,a_rcc26,b_pdb,b_rcc1,b_rcc2,b_rcc3,...,b_rcc26
where a_pbd and b_pdb are two interacting proteins.
In this case those input files are called, i.e., 'af_10000_d7Lat.csv' or 'exp_10000_d7Lat.csv'.
and the output files are called, i.e., 'af_d7Lat.csv' or 'exp_d7Lat.csv'.
For full databases, this code removes the headers and the last column (protein CATH classification)
'''

# Rcc vectors are generated for various contact distances, with or without side chains
conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat']
input_name_str = ['af_10000_','exp_10000_','full_']
separator = ','
models = ['AlphaFold','Experimental','FullPDB']

output_info = open('output_p1_interacting.txt','w') # file to know how many proteins you have
for m in range(len(models)):
	info = []
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
				pdbs_dict[aux[0]] = aux[1:27]
				pdbs_dict[aux[27]] = aux[28:]
				complexes += 1
			elif aux[0] != '' and len(aux) == 28:
				# Here we remove the header for full databases
				if aux[0] != 'PDBID':
					pdbs_dict[aux[0]] = aux[1:27]
		input_file.close()

		number_of_pdbs = len(pdbs_dict)

		# We save a list of the proteins
		output_file = open(output_dir+output_file_name+'.txt','w')
		# For each item in the dictionary
		for key, value in pdbs_dict.items():
			line_to_print = key # we take the key to start a line to print
			for v in pdbs_dict[key]:
				line_to_print += ','+str(int(v)) # with all its values
			print(line_to_print,file=output_file) # and print the item
		output_file.close()

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
