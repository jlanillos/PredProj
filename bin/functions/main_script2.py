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

save_file = os.path.join(main_path, 'results','parametricAnal_ws_kern_cv.txt')

# PARAMETERS

#add prefiltering or others

ws_range = 15#[7,11,15,19,23,27,31,34,39] #window size of the vectors
kern_range = 'rbf'#['linear', 'poly', 'rbf', 'sigmoid'] #Choose the kernel function for SVM
cv_range = 3#[3,5,7,9] #number of training datasets (plus the test dataset) for cross-validation


# RUN SUPPORT VECTOR MACHINE ANALYSIS
path2functions = os.path.join(bin_path,'functions')
os.chdir(path2functions)
import datetime
import runSVM


for kern in kern_range:
	for ws in ws_range:
		for cv in cv_range:
			now = datetime.datetime.now()
			print ('Current date and time using str method of datetime object: ')
			print (str(now))
			f = open(save_file,'w')
			f.write('Current date and time using str method of datetime object: ' + str(now) + '\n')
			print('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv))
			f.write('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv)+'\n')
			scores = fSVM.runSVM(main_path,data_path,bin_path,dataset_file,ws,kern,cv)
			f.write('Score ' + str(scores) +'\n')
			print(scores)
			print('The average score is:' + str(sum(scores)/cv))
			f.write('Average score ' + str(sum(scores)/cv +'\n')
