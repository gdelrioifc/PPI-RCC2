'''
This code calculates the angles between the vectors in the samples.
If the samples in FulldPDB are few, and have few vectors, this is the final code to use.
If the samples have hundreds of vectors, it's better to use the p5_runAngles.sh and p6_runAngles.py.
'''


import numpy as np

conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat']
input_name_str = ['af_10000_','exp_10000_','full_'] # files with the list of complexes
separator = ','
models = ['AlphaFold','Experimental','FullPDB']

samples = 50
samples_for_fullPDB = 20

def product(*args):
    # This code calculates the inner product between two vectors
    # if the input is onle one vector, it calculates its magnitude

    n = len(args) # dimension of the vector
    s = 0
    for i in range(len(args[0])):
        s += args[0][i]*args[n-1][i] # inner product
    return s**(1/(3-n))

# For each model
for m in range(len(models)):
	# For each condition
	for size in conditions:

		# Here we check which pairs of proteins
		# ara already interacting proteins
		input_file_name = input_name_str[m]+size
		input_file = open(input_file_name+'.csv','r')
		complexes = {}
		for line in input_file:
			aux = line.split(',')
			if aux[0] != '':
				# The protein 1 interacts with the protein 2
				# as well the protein 2 with the 1.
				complexes[aux[0]+aux[27]] = None
				complexes[aux[27]+aux[0]] = None
		input_file.close()

		average = 0
		print('calculating angles in ',models[m],size)
		if models[m] == 'FullPDB':
			samples = samples_for_fullPDB

		# We wish to know how the angle between 2 proteins
		# if the angle is less than 5°, we say that both proteins are parallel proteins
		# Not all proteins have a protein parallel,
		# so we wish to know how many proteins have at least 1 protein
		for q in range(samples):
			# We save all the elements in each sample
			name = input_name_str[m].split('_')[0]+'_'+size+'_'+str(q)+'.txt'
			input_file = open(models[m]+'/size'+size+'/NonInteracting/'+name,'r')
			vectores = {}
			for line in input_file:
				aux = line.split(separator)
				#print(aux[0])
				vectores[aux[0]] = list(map(int,aux[1:]))
			input_file.close()

			# We print the angles between each possible pair of vector
			output_file = open(models[m]+'/size'+size+'/NonInteracting/AnglesAt_'+name,'w')
			# We print headers, and the quantity of different proteins in the sample
			population = len(vectores)
			print('PDB1\tPDB2\tAngle(degrees)\t'+str(population),file=output_file)

			# The angle between protein 1 and protein 2 is the same
			# that the angle between protein 2 and protein 1,
			# so we are going to avoid it saving in 'pairs_dict'
			pairs_dict = {}
			pdbs_with_one_par = {} # Here are the proteins with at least 1 parallel protein
			for key,value in vectores.items():
				for k, v in vectores.items():
					# We calculate only for pairs that have not been calculated, and are not in the pairs_dict
					# the angle between a protein an itself is also avoided.
					if k != key and (k+key not in complexes or key+k not in complexes) and (k+key not in pairs_dict or key+k not in pairs_dict):
						p1 = vectores[k]
						p2 = vectores[key]
						pairs_dict[k+key] = None
						pairs_dict[key+k] = None
						try:
							cosA = product(p1,p2)/product(p1)/product(p2)
						except ZeroDivisionError:
							cosA = 1
						if cosA > 1:
							cosA = 1

						angulo = np.arccos(cosA)
						angulo = angulo*180/np.pi
						print(k+'\t'+key+'\t'+str(angulo),file=output_file)
						if angulo <= 5:
							pdbs_with_one_par[k] = None
							pdbs_with_one_par[key] = None
						#print(k+'\t'+key+'\t'+str(angulo))
						#print(k,key,product(vectores[k],vectores[key]))
			#print(name)
			output_file.close()
			average +=len(pdbs_with_one_par)/population
		print('Angles files for',models[m],size,'ready,')
		print('Proteins with at least 1 parallel in ',models[m],size,': ',100*average/samples,'%')

		average = 0

		# We wish to know how the angle between 2 proteins
		# if the angle is less than 5°, we say that both proteins are parallel proteins
		# Not all proteins have a protein parallel,
		# so we wish to know how many proteins have at least 1 protein
		for q in range(samples):
			# We save all the elements in each sample
			name = 'sim_'+input_name_str[m].split('_')[0]+'_'+size+'_'+str(q)+'.txt'
			input_file = open(models[m]+'/size'+size+'/NonInteracting/'+name,'r')
			vectores = {}
			for line in input_file:
				aux = line.split(separator)
				#print(aux[0])
				vectores[aux[0]] = list(map(int,aux[1:]))
			input_file.close()

			# We print the angles between each possible pair of vector
			output_file = open(models[m]+'/size'+size+'/NonInteracting/AnglesAt_'+name,'w')
			# We print headers, and the quantity of different proteins in the sample
			population = len(vectores)
			print('PDB1\tPDB2\tAngle(degrees)\t'+str(population),file=output_file)

			# The angle between protein 1 and protein 2 is the same
			# that the angle between protein 2 and protein 1,
			# so we are going to avoid it saving in 'pairs_dict'
			pairs_dict = {}
			pdbs_with_one_par = {} # Here are the proteins with at least 1 parallel protein
			for key,value in vectores.items():
				for k, v in vectores.items():
					# We calculate only for pairs that have not been calculated, and are not in the pairs_dict
					# the angle between a protein an itself is also avoided.
					if k != key and (k+key not in complexes or key+k not in complexes) and (k+key not in pairs_dict or key+k not in pairs_dict):
						p1 = vectores[k]
						p2 = vectores[key]
						pairs_dict[k+key] = None
						pairs_dict[key+k] = None
						try:
							cosA = product(p1,p2)/product(p1)/product(p2)
						except ZeroDivisionError:
							cosA = 1
						if cosA > 1:
							cosA = 1

						angulo = np.arccos(cosA)
						angulo = angulo*180/np.pi
						print(k+'\t'+key+'\t'+str(angulo),file=output_file)
						if angulo <= 5:
							pdbs_with_one_par[k] = None
							pdbs_with_one_par[key] = None
						#print(k+'\t'+key+'\t'+str(angulo))
						#print(k,key,product(vectores[k],vectores[key]))
			#print(name)
			output_file.close()
			average +=len(pdbs_with_one_par)/population
		print()
		print('Angles files for simulated',models[m],size,'ready,')
		print('Proteins with at least 1 parallel in simulated',models[m],size,': ',100*average/samples,'%')
		print()

	print('-----------------------------------------')

