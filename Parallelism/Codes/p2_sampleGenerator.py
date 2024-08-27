'''
This code splits the databases with the list of proteins with at least one reported interaction
The input files are named as 'af_d7Lat' and are formated as follows
pdb1,rcc1,rcc2,...,rcc26
The output files have the same format and are names as 'af_d7Lat_N'
where 'N' is the sample number.
This code also calculates the sum of the 26 components for each pdb in each samble
and prints this value in a file named 'sumsAt_af_d7Lat_N'.
If the sample has 'P' vectors, there are 'P' sums.
This code also calculates the average values for the 26 components in each sample
and prints those averages in a file named 'averagesAt_af_d7Lat_N'.
'''

import pandas as pd
import random as rn
import numpy as np

conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat'] # Contact distance and with or without side chains
input_name_str = ['af_','exp_','full_'] # str to diferentiate between files
separator = ',' # inside files separator

interact_case = True
if interact_case:
	models = ['AlphaFold','Experimental'] # Diferent models used
else:
	models = ['AlphaFold','Experimental','FullPDB'] # Diferent models used


# Here you can configure how many samples and with how large population you want to simulate rcc vectors.
# You can find a sugestion for this values in 'output_p1_interacting.txt'
samples = 1
population = 1717
# FullPDB has more vectors, so you can simulate more vectors
samples_for_full = 440
population_for_full = 83

for m in range(len(models)):
	for size in conditions:
		if interact_case == False:
			main_dir = models[m]+'/size'+size+'/'
			input_dir = main_dir+'Interacting/'
			output_dir = main_dir+'NonInteracting/'

			# Reading of the list of proteins in the database
			input_file = pd.read_csv(input_dir+input_name_str[m]+size+'.txt',header=None)
			vectors_in_dataBase = len(input_file)

			# If one of the databases needs a different number of samples and population
			if models[m] == 'FullPDB':
				samples = samples_for_full
				population = population_for_full

			# Here is printed a sample file 'af_d7Lat_N.txt', where 'N' is the sample number
			for q in range(samples):
				sample_output = open(output_dir+input_name_str[m]+size+'_'+str(q)+'.txt','w')
				# for each sample, there is a set of sums (the sum of the rccs for each pdb)
				sums_output = open(output_dir+'/sumsAt_'+input_name_str[m]+size+'_'+str(q)+'.txt','w')
				# each sample has a set of 26 average values, 1 for each rcc
				average = np.zeros(26)

				for i in range(population):
					# From all vectors in the database, we choose 1 randomly
					pdb = rn.randint(0,vectors_in_dataBase-1)
					pdb = input_file.loc[[pdb]]
					#print(pdb)

					# We take the name of the vector (i.e. PDBID),
					line_to_print = pdb[0].values[0]
					information = 1 # To make sure there is always info in the vector
					for v in range(1,27):
						# we append all the rcc values,
						value = pdb[v].values[0]
						line_to_print += ','+str(value)
						# we sum the rcc values,
						information += value
						# and add its contribution to the average.
						# Due range(1,27), but average is a range(0,26)
						# we use the 'v-1' position
						average[v-1] += value/population

					# Printing in 'af_d7Lat_N.txt'
					print(line_to_print,file=sample_output)
					# Printing in 'sumsAt_af_d7Lat_N.txt'
					print(str(information),file=sums_output)
				sample_output.close()
				sums_output.close()
				# In this point we have the average, but not the standard deviation

				# We open again the database file to calculate the standard deviation
				sample_input = open(output_dir+input_name_str[m]+size+'_'+str(q)+'.txt','r')
				deviation = np.zeros(26)
				for line in sample_input:
					aux = np.array(list(map(int,line.split(separator)[1:])))
					# Each component has a standard deviation
					for i in range(26):
						deviation[i] += (aux[i]-average[i])**2
				sample_input.close()
				# For all the components we have the same number of elements
				deviation /= (population-1)
				deviation = deviation**(1/2)

				# Printing in 'averagesAt_af_d7Lat_N.txt'
				average_output = open(main_dir+'NonInteracting/averagesAt_'+input_name_str[m]+size+'_'+str(q)+'.txt','w')
				for i in range(26):
					print(str(i+1)+','+str(average[i])+','+str(deviation[i]),file=average_output)
				average_output.close()
				print('Ready averagesAt_'+input_name_str[m]+size+'_'+str(q))
			#----------------------------------------------------
		else:
			entrada = open(models[m]+'/size'+size+'/Interacting/'+input_name_str[m]+size+'.txt','r')
			pdbs = []
			for line in entrada:
				aux = line.split(',')
				pdbs.append(aux[0])
			entrada.close()

			entrada = open('af_10000_'+size+'.csv','r')
			salida = open(models[m]+'/size'+size+'/Interacting/'+input_name_str[m]+'complexes_'+size+'.csv','w')
			for line in entrada:
				aux = line.split(',')
				if aux[0] == '':
					pass
				else:
					print(line[:-1],file=salida)
			entrada.close()
			salida.close()

			for q in range(samples):
				entrada = open(models[m]+'/size'+size+'/Interacting/'+'sim_'+input_name_str[m]+size+'_'+str(q)+'.txt','r')
				counter = 0
				corresponding_proteins = {}
				for line in entrada:
					aux = line.split(',')
					corresponding_proteins[pdbs[counter]] = aux[0]
					#print(simulated_proteins)
					counter += 1
				entrada.close()

				entrada = open(models[m]+'/size'+size+'/Interacting/'+'sim_'+input_name_str[m]+size+'_'+str(q)+'.txt','r')
				simulated = {}
				for line in entrada:
					aux = line.split(',')
					nombre = aux[0]
					vector = list(map(int,aux[1:]))
					simulated[nombre] = vector
				entrada.close()

				#print('vectores simulados',len(simulated))

				entrada = open(input_name_str[m]+'10000_'+size+'.csv','r')
				salida2 = open(models[m]+'/size'+size+'/Interacting/'+'sim_'+input_name_str[m]+'complexes_'+size+'_'+str(q)+'.csv','w')
				for line in entrada:
					aux = line.split(',')
					if aux[0] == '':
						pass
					else:
						name1 = corresponding_proteins[aux[0]]
						name2 = corresponding_proteins[aux[27]]
						values1 = simulated[name1]
						values2 = simulated[name2]
						line_to_print = name1
						for r in range(26):
							line_to_print += ','+str(values1[r])
						line_to_print += ','+name2
						for r in range(26):
							line_to_print += ','+str(values2[r])
						print(line_to_print,file=salida2)

				salida2.close()
				entrada.close()

