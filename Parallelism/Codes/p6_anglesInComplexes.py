'''
This code calculates the angle between the interacting proteins in a complex.
'''

conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat']
models = ['AlphaFold','Experimentals']
input_name_str = ['af_10000_','exp_10000_'] # Files with the complexes information
separator = ','

import numpy as np

def product(*args):
    # This function calculates the magnitude of a vector
    # or the inner product between to vectors
    n = len(args)
    s = 0
    for i in range(len(args[0])):
        s += args[0][i]*args[n-1][i]
    return s**(1/(3-n))

for m in range(len(models)):
    prev = ''
    for c in conditions:
        name = input_name_str[m]+c+'.csv'
        name_out = models[0]+'/size'+c+'/Interacting/AnglesAt_'+input_name_str[m].split('_')[0]+c+'.txt'

        input_file = open(name,'r')
        output_file = open(name_out,'w')


        total = {} # Proteins in the complexes
        parallels = {} # Proteins with at least 1 parallel as defined in p4_runAngles.py
        print('PDB1\tPDB2\tAngle(degrees)',file=output_file)
        for line in input_file:
            if line == prev: # Here is to make sure that each complex is considered only once
                pass
            elif line != prev:
                prev = line
                # for each complex we calculate the angle between its proteins
                aux = line.split(separator)
                if aux[1] != 'arcc1' and aux[0] != '': # and aux[0] != aux[27]:
                    if aux[0] == '':
                        print(aux) # if some info is missing, we can know it
                    try:
                        # We write the components of each vector
                        v1 = list(map(int,aux[1:27]))
                        v2 = list(map(int,aux[28:]))
                        total[aux[0]] = None
                        total[aux[27]] = None
                    except:
                        pass

                    try:
                        # we try to calculate the cos(A) given two vectors
                        cosA = product(v1,v2)/product(v1)/product(v2)
                    except ZeroDivisionError:
                        cosA = 1
                    # Due the float managment of python, some this cosA could be greater that 1
                    if cosA > 1:
                        cosA = 1

                    # We calculate the angle using cosA
                    angle = np.arccos(cosA)
                    angle = angle*180/np.pi # we convert to degrees

                    # Here the angles are printed in the output file
                    print(aux[0]+'\t'+aux[27]+'\t'+str(angle),file=output_file)
                    if angle < 5 and aux[0]!=aux[27]:
                        # If the angle between the proteins is less than 5°,
                        # and it is not a self-interaction, we consider them parallel proteins
                        parallels[aux[0]] = None
                        parallels[aux[27]] = None
        input_file.close()
        output_file.close()

        print(models[m],c)
        print('paralelos (%):',100*len(parallels)/len(total))
