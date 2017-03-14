# This is the main script that runs the whole analysis

#print ('Welcome to the surface exposition residues predictor by using SVM')
import os
import runSVM as fSVM
main_path = '/home/u2188/PredProj' #Write the main path to the project directory
#main_path = '/home/jlanillos/PredProj' #Write the main path to the project directory
os.chdir (main_path)
data_path = os.path.join(main_path, 'data','datasets')

dataset_file = 'buried-exposed.3line.txt'
bin_path = os.path.join(main_path, 'bin')

save_file = os.path.join(main_path, 'results','parametricAnal_kern_REGULARIZATION_linear_20170312.txt')
save_model_path = os.path.join(main_path, 'models')


# PARAMETERS

#add prefiltering or others

ws_range = [15] #window size of the vectors
kern_range = ['linear']#['poly', 'rbf','linear'] #Choose the kernel function for SVM
cv_range = [7]#[3,5,7,9] #number of training datasets (plus the test dataset) for cross-validation
C_range = [0.001,0.005,0.01,0.07,0.1,0.5,1]

# RUN SUPPORT VECTOR MACHINE ANALYSIS
path2functions = os.path.join(bin_path,'functions')
os.chdir(path2functions)
import datetime
import runSVM


for kern in kern_range:
	for ws in ws_range:
		for cv in cv_range:
			for C in C_range:

				now = datetime.datetime.now()
				print ('Current date and time using str method of datetime object: ')
				print (str(now))
				print('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv))
	
				f = open(save_file,'a+')
				f.write('Current date and time using str method of datetime object: ' + str(now) + '\n')
				f.write('Kernel ' + kern + ' ' + 'window size '+ str(ws) + ' ' + 'training sets ' + str(cv)+'\n')

				scores,y,y_pred  = fSVM.runSVM(main_path,data_path,bin_path,dataset_file,ws,kern,cv,C,save_model_path)


				f.write('Score ' + str(scores) +'\n')

				print(scores)
				print('The average score is:' + str(sum(scores)/cv))

				f.write('Average score ' + str(sum(scores)/cv) +'\n')
				labels=[0, 1]
				f.write(np.array_str(confusion_matrix(y, y_pred, labels = labels).ravel()))
				f.write('\n')
				f.close()
