#main_script with SVM with psiblast info

#print ('Welcome to the surface exposition residues predictor by using SVM')
import os
import datetime
import numpy as np
import runSVM_imp_perfo as fSVM
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



#save_file = os.path.join(main_path, 'results','psiblast_parametricAnal_ws_Linearkern_cv_20170306.txt')

save_file = os.path.join(main_path, 'results','parametricAnal_improve_perfo_gamma_C_20170313.txt')

functions_path = os.path.join(main_path, 'bin','functions')
#cd '/home/jlanillos/PredProj/bin/functions'



#PARAMETERS

ws = 15 #window size of the vectors (fixed to 15 as I decided it)
kern_range = ['linear'] #['linear', 'poly', 'rbf', 'sigmoid'] #Choose the kernel function for SVM
cv_range = [7]#[3,5,7,9] #number of training datasets (plus the test dataset) for cross-validation FIXED ON 7 AS DECIDED

C_range = [0.005,0.07,0.5,1] # Regularization parameter




# RUN SUPPORT VECTOR MACHINE ANALYSIS

path2functions = os.path.join(bin_path,'functions')
os.chdir(path2functions)


for kern in kern_range:
	for C in C_range:
		for cv in cv_range:

		

			now = datetime.datetime.now()
			print ('Current date and time using str method of datetime object: ')
			print (str(now))
			print('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv) + ' ' + 'regularization parameter ' + str(C))

			f = open(save_file,'a+')
			f.write('Current date and time using str method of datetime object: ' + str(now) + '\n')
			f.write('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv) + ' ' + 'regularization parameter ' + str(C) + '\n')

			y,y_pred = fSVM.runSVM(main_path,data_path,bin_path,dataset_file,pssm_data_folder,ws,kern,cv,C)



			#Confusion matrix: tn, fp, fn, tp
			labels=[0, 1]
			f.write(np.array_str(confusion_matrix(y, y_pred, labels = labels).ravel()))
			#print(classification_report(y,y_pred, labels=labels))


			f.close()
