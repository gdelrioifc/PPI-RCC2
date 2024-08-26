'''
This code counts the number of proteins with at least one parallel given the 'AnglesAt_' file.
In this case is only for the samples in FullPDB, considering that the 'AnglesAt_' file was gotten with the 'p5_runAngles.sh'
'''

conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat']
models = ['FullPDB']
input_name_str = ['full_']

samples = 20
poblacion = 100

for m in range(len(models)):
    for base in conditions:
        folder = models[m]+'/size'+base+'/NonInteracting/'

        average = 0
        for x in range(samples):
            # For the angles in each sample
            input_file = open(folder+'AnglesAt_'+input_name_str[m]+base+'_'+str(x)+'.txt','r')
            proteins_in_DB = {} # we count how many proteins are in the sample
            proteins_with_1_par = {} # and we count how many have at least 1 parallel protein

            for line in input_file:
                aux = line.split(',')
                try:
                    angle = float(aux[-1])
                    p1 = aux[0]
                    p2 = aux[1]
                    proteins_in_DB[p1] = None
                    proteins_in_DB[p2] = None

                    # Here is not needed to remove self-interactions
                    if angle < 5:
                        proteins_with_1_par[p1] = None
                        proteins_with_1_par[p2] = None
                except:
                    pass
            input_file.close()

            proteins_in_DB = len(proteins_in_DB)
            proteins_with_1_par = len(proteins_with_1_par)
            percentage = proteins_with_1_par/proteins_in_DB

            average += percentage # we add the contribution to the average of all samples

        print('Parallels in',models[m],base,'(%):',100*average/samples)

        # we repeat the previous code for the simulation samples
        average = 0
        for x in range(samples):
            input_file = open(folder+'AnglesAt_sim_'+input_name_str[m]+base+'_'+str(x)+'.txt','r')
            proteins_in_DB = {}
            proteins_with_1_par = {}
            for line in input_file:
                aux = line.split(',')
                try:
                    angle = float(aux[-1])
                    p1 = aux[0]
                    p2 = aux[1]
                    proteins_in_DB[p1] = None
                    proteins_in_DB[p2] = None
                    if angle < 5 and p1 != p2:
                        proteins_with_1_par[p1] = None
                        proteins_with_1_par[p2] = None
                except:
                    pass
            input_file.close()
            proteins_in_DB = len(proteins_in_DB)
            proteins_with_1_par = len(proteins_with_1_par)
            percentage = proteins_with_1_par/proteins_in_DB
            average += percentage

        print('Parallels in simulation of',models[m],base,'(%):',100*average/samples)
        print('')
