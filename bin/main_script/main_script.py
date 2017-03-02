# This is the main script that runs the whole analysis

#print ('Welcome to the surface exposition residues predictor by using SVM')
import os
import runSVM as fSVM
main_path = '/home/u2188/PredProj' #Write the main path to the project directory
os.chdir (main_path)
data_path = os.path.join(main_path, 'data','datasets')
#dataset_file = 'buried-exposed_TRIAL.txt'
dataset_file = 'buried-exposed.3line.txt'
bin_path = os.path.join(main_path, 'bin')

# PARAMETERS

#add prefiltering or others

ws = 7 #window size of the vectors
kern = 'rbf' #Choose the kernel function for SVM
cv = 5 #number of training datasets (plus the test dataset) for cross-validation


# RUN SUPPORT VECTOR MACHINE ANALYSIS
path2functions = os.path.join(bin_path,'functions')
os.chdir(path2functions)
print(path2functions)

import runSVM

scores = fSVM.runSVM(main_path,data_path,bin_path,dataset_file,ws,kern,cv)

print(scores)
print('The average score is:' + str(sum(scores)/cv))
