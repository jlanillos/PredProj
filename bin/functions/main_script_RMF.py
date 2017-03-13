#main_script with SVM with psiblast info

#print ('Welcome to the surface exposition residues predictor by using SVM')
import os
import datetime
import numpy as np
import runRFC as RFC
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import math
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


#main_path = '/home/u2188/PredProj' #Main path to the project directory
main_path = '/home/jlanillos/PredProj' #Main path to the project directory
data_path = os.path.join(main_path, 'data','datasets')
#dataset_file = 'example_oneseq.fasta'
dataset_file = 'buried-exposed.3line.txt'
pssm_data_folder = os.path.join(main_path, 'data', 'psi_blast')
bin_path = os.path.join(main_path, 'bin')



save_file = os.path.join(main_path, 'results','RFM_param_ws_20170312.txt')
functions_path = os.path.join(main_path, 'bin','functions')




#PARAMETERS

ws_range = [7,11,19,23,27,31] #window size of the vectors 
kern_range = ['poly'] #['linear', 'poly', 'rbf', 'sigmoid'] #Choose the kernel function for SVM
n_estimators = [3,5,7,9,101] #number of training datasets (plus the test dataset) for cross-validation FIXED ON 7 AS DECIDED





# RUN SUPPORT VECTOR MACHINE ANALYSIS

path2functions = os.path.join(bin_path,'functions')
os.chdir(path2functions)


for ws in ws_range:
	for cv in n_estimators:		

		now = datetime.datetime.now()
		print ('Current date and time using str method of datetime object: ')
		print (str(now))
		print('window size '+ str(ws) + ' ' + 'n_estimators ' + str(cv))
		f = open(save_file,'a+')
		f.write('Current date and time using str method of datetime object: ' + str(now) + '\n')
		f.write('window size '+ str(ws) + ' ' + 'n_estimators ' + str(cv) +'\n')
		y,y_pred = RFC.runSVM(main_path,data_path,bin_path,dataset_file,pssm_data_folder,ws,cv)


		#Confusion matrix: tn, fp, fn, tp
		labels=[0, 1]
		f.write(np.array_str(confusion_matrix(y, y_pred, labels = labels).ravel()))
		print(np.array_str(confusion_matrix(y, y_pred, labels = labels).ravel()))
		#print(classification_report(y,y_pred, labels=labels))
		f.close()
