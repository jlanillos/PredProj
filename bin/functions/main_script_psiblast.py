#main_script with SVM with psiblast info

#print ('Welcome to the surface exposition residues predictor by using SVM')
import os
import datetime
import numpy as np
import runSVM_psiblast as fSVM
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import math
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


main_path = '/home/u2188/PredProj' #Main path to the project directory
#main_path = '/home/jlanillos/PredProj' #Main path to the project directory
data_path = os.path.join(main_path, 'data','datasets')

dataset_file = 'buried-exposed.3line.txt'
pssm_data_folder = os.path.join(main_path, 'data', 'psi_blast')
bin_path = os.path.join(main_path, 'bin')



save_file = os.path.join(main_path, 'results','psiblast_parametricAnal_ws_Linearkern_cv_20170306.txt')


functions_path = os.path.join(main_path, 'bin','functions')
#cd '/home/jlanillos/PredProj/bin/functions'



#PARAMETERS

ws_range = [7,11,15,19,23,27,31] #window size of the vectors
kern_range = ['linear'] #['linear', 'poly', 'rbf', 'sigmoid'] #Choose the kernel function for SVM
cv_range = [3,5,7,9] #number of training datasets (plus the test dataset) for cross-validation






# RUN SUPPORT VECTOR MACHINE ANALYSIS

path2functions = os.path.join(bin_path,'functions')
os.chdir(path2functions)


for kern in kern_range:
	for ws in ws_range:
		for cv in cv_range:

			now = datetime.datetime.now()
			print ('Current date and time using str method of datetime object: ')
			print (str(now))
			print('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv))

			f = open(save_file,'a+')
			f.write('Current date and time using str method of datetime object: ' + str(now) + '\n')
			f.write('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv)+'\n')

			scores,y,y_pred = fSVM.runSVM(main_path,data_path,bin_path,dataset_file,pssm_data_folder,ws,kern,cv)


			f.write('Score ' + str(scores) +'\n')

			print(scores)
			print('The average score is:' + str(sum(scores)/cv))

			f.write('Average score ' + str(sum(scores)/cv) +'\n')

			#Confusion matrix: tn, fp, fn, tp
			labels=[0, 1]
			f.write(np.array_str(confusion_matrix(y, y_pred, labels = labels).ravel()))
			#print(classification_report(y,y_pred, labels=labels))
			#print(type(np.array_str(confusion_matrix(y, y_pred, labels = labels).ravel())))	


			f.close()
