'''
This code generate random vectors following a 'fited_curve' to the data from FullPDB.
This curve can be modified to other tendencies of the 26 components in a rcc vector.
The 'rccGenerator' generates a number that follows the distribution of specific components in the vector.
The 'massiveGenerator' works for each sample gotten with p2_sampleGenerator.py
'''

import numpy as np

interact_case = True
samples = 1


if interact_case:
    models = ['AlphaFold','Experimental']
else:
    models = ['AlphaFold','Experimental','FullPDB']

conditions = ['d7Lat','d7NoLat','d8Lat','d8NoLat'] # Contact distance and with or without side chains
input_name_str = ['af_','exp_','full_'] # str to diferentiate between files
separator = ',' # inside files separator

# Here you can configure how many samples and with how large population you want to simulate rcc vectors.
# You can find a sugestion for this values in 'output_p1_interacting.txt'

def fited_curve(ne,c):
    # Gaussian curve to model the relation between the 26 components of the rcc vector.
    a = c[0]
    m = c[1]
    s = c[2]
    binomio = (ne-m)**2
    frac = binomio/(2*s**2)
    return a*np.exp(-frac)

def rccModel(me,ajuste):
    # For now, the curve choosen for the tendency of the values is the sum of 4 Gaussian curves
    c1 = ajuste[0]
    c2 = ajuste[1]
    c3 = ajuste[2]
    c4 = ajuste[3]
    return fited_curve(me,c1)+fited_curve(me,c2)+fited_curve(me,c3)+fited_curve(me,c4)

def rccGenerator(rcc,ajustes,valor,incertidumbre):
    # This uses the rccModel to generate components for a vector randomly
    random = np.random.normal(0,incertidumbre)
    if random > 0:
        val = np.rint(rccModel(rcc,ajustes)+random)
    else:
        #val = np.rint(-1*random)
        val = 0
    return int(val)

def massiveGenerator(directory,kind,case,fln):
    # fln: sample number

    if interact_case:
        rccAverageFile = directory+'averagesAt_'+kind+case+'.txt'
        sumsFile = directory+'sums_'+kind+case+'.txt'
        #print(sumsFile)
    else:
        rccAverageFile = directory+'averagesAt_'+kind+case+'_'+str(fln)+'.txt'
        sumsFile = directory+'sumsAt_'+kind+case+'_'+str(fln)+'.txt'

    #print('Reading: ',rccAverageFile)

    curvesFile = 'curvesFrom'+case+'N0.txt'
    output = open(directory+'sim_'+kind+case+'_'+str(fln)+'.txt','w')

    # Here it's Read the 'averagesAt_af_d7Lat_N.txt'
    # where 'N' is the sample number
    #print('Trying to read averages file')
    file = open(rccAverageFile, 'r')
    #print('Opened file:',rccAverageFile)
    average_values = []
    std_deviation = []
    for line in file:
        aux = line.split(separator)
        aux = list(map(float,aux))
        average_values.append(aux[1])
        std_deviation.append(aux[2])
    file.close()
    #print('Read file:',rccAverageFile)
    # At this point we have a list of 26 averages
    # and a list of 26 standard deviations.

    # Here we read the curves file
    # The curves file has parametrs for the function fited_curve()
    #print('Trying to read curves file')
    file = open(curvesFile, 'r')
    ajustes = []
    for line in file:
        aux = line.split(separator)
        aux = list(map(float,aux))
        ajustes.append(aux)
    file.close()
    #print('Read file:',curvesFile)

    # Here we read the file 'sumsAt_af_d7Lat_N.txt'
    #print('Trying to read sums file')
    file = open(sumsFile,'r')
    content = file.readlines()
    elements = len(content)
    #print('Read file:',sumsFile)

    # For the each element in the sample
    print('Trying to generate sample',fln)
    for q in range(elements):
        rcc = [] # we are going to generate a corresponding vector
        condition = int(content[q]) # which has a boundary given in 'sumsAt_af_d7Lat_N.txt'
        #print(condition,input_name_str[m]+size+'_'+str(sample_number),q)
        t = 0 # number of tryings
        for x in range(26):
            # we generate each componente one by one
            #print('Trying to generate component',x)
            rcc.append(rccGenerator(x+1,ajustes,average_values[x],std_deviation[x]))
            # we had used 'x+1' because the fited curve is not defined in [0,25] but [1,26]

        # We transform the array in a numpy array to check the conditions
        rcc = np.array(rcc)
        #print(rcc)
        # The simulted vector should not be only zeros.
        while np.sum(rcc) == 0:
            rcc = []
            for x in range(26):
                rcc.append(rccGenerator(x+1,ajustes,average_values[x],std_deviation[x]))
            rcc = np.array(rcc)

        # The sum of the simultad components should be equal
        # to sum of the correspondind real components,
        # within a tolerance of +/- 20%.
        w = 0
        #print(rcc)
        try:
            while np.sum(rcc) not in range(int(condition*0.8),int(condition*1.2)+1) and w == 0:
                # if the simulated vector is not inside the tolerance
                # we make a renormalization taking the 'condition'
                try:
                    #print('Cheking condition')
                    mult = np.sum(rcc)/condition
                    #print('condition checked')
                except:
                    condition = np.sum(rcc)
                    w = 1
                try:
                    #print('Reescalando vector')
                    rcc = list(map(int,rcc/mult))
                    #print('Vector reescalado:',np.sum(rcc),condition)
                except:
                    rcc = np.array(rcc)
                    w = 1
                # After 10000 attempts we take the rcc as it is
                t += 1
                if t == 10000:
                    texto = str(np.sum(rcc))
                    rcc = np.array(rcc)
                    w = 1
                #print(np.sum(rcc),condition*0.8,condition*1.2,w)
        except:
            pass
        # Here we check if its not a zero vector.
        #print('While loop satisfied')
        while np.sum(rcc) == 0:
            rcc = []
            for x in range(26):
                rcc.append(rccGenerator(x+1,ajustes,average_values[x],std_deviation[x]))
            rcc = np.array(rcc)

        # We reconvert the numpy array into a python list.
        #print(rcc,' en ', 'random'+case+'sub'+str(fln))
        #print('Transforming rcc np.array into python list')
        rcc = list(rcc)

        # The next step is to make sure there are not repeated vectors in the sample
        # The repeated vectors could be avoided using another curve function
        # This section modifies 2 components randomly.
        # Because it's a 26-dimentional vector, +/-1 is negligible for the 'condition'
        extra1 = np.random.randint(0,26)
        rcc[extra1] += 1
        extra2 = np.random.randint(0,26)
        while extra2 == extra1:
            extra2 = np.random.randint(0,26)
        if rcc[extra2] > 0:
            rcc[extra2] -= 1

        # Here the random vector is printed in 'sim_af_d7Lat_N.txt'
        line_to_print = kind+str(fln)+'{:06x}' #.format(fln*elements+count)
        for r in range(26):
            line_to_print += ','+str(rcc[r])
        print(line_to_print.format(fln*elements+q),file=output)
        #print(q,rcc)
        output.flush()
    output.close()

    return rcc

# We simulate the vectors for each model
for m in range(len(models)):
    for size in conditions:
        if interact_case:
            main_dir = models[m]+'/'+'size'+size+'/Interacting/'
        else:
            main_dir = models[m]+'/'+'size'+size+'/NonInteracting/'

        # For each sample, we generate a simulated population
        for sample_number in range(samples):
            try:
                vector = massiveGenerator(main_dir,input_name_str[m],size,sample_number)
            except:
                print('Something went wrong wile generating ',input_name_str[m]+size+'_'+str(sample_number))
                print('Check out your input files.')
        print('Random '+input_name_str[m]+size+' ready')
        print('-----------------------------------------')
