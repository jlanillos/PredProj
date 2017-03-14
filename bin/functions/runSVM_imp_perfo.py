# Script that runs the necessary functions for SVM WITH EVOLUTIONARY DATA.
# Specially, this function is designed to run parametric estimations with different kernels and others.

# Script that runs every step necessary to perform SVM and SVM itself


def runSVM(main_path,data_path,bin_path,dataset_file,pssm_data_folder,ws,kern,cv,C):

	
	import os
	import datetime
	from sklearn.svm import LinearSVC
	from sklearn.svm import SVC
	from sklearn.model_selection import cross_val_score
	import math
	from sklearn.metrics import confusion_matrix
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import classification_report



	#Read the FASTA that contains all proteins
	filename = data_path + '/' + dataset_file
	title_list, seq_list, feature_list = read_fasta(filename)



	# Arrange data as input for sklearn
	wordscode, featurescode = prot2vect_psiblast(title_list, seq_list, feature_list,ws,pssm_data_folder)


#RUNNING SVM

	X = wordscode
	y = featurescode

# IMPORTANT: here I have defined three different kernels with specific parameters for my project. They could be customized as desired
	if kern == 'poly':
		clf = SVC(C=C, kernel=kern, degree=2, gamma= 1.0, coef0=1.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight='balanced', verbose=False, max_iter=-1, decision_function_shape=None, random_state=None)
	
		clf.fit(X, y)
		y_pred = clf.predict(X)

	elif kern == 'rbf':

		clf = SVC(C=C, kernel=kern, degree=3, gamma=0.1, coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight='balanced', verbose=False, max_iter=-1, decision_function_shape=None, random_state=None)

	
		clf.fit(X, y)
		y_pred = clf.predict(X)

	elif kern == 'linear':

		clf = LinearSVC(C=C)

		clf.fit(X, y)
		y_pred = clf.predict(X_50prot)



#	if cv == 3:
#		scores = cross_val_score(clf, wordscode, featurescode, cv = 3)
#	if cv == 5:
#		scores = cross_val_score(clf, wordscode, featurescode, cv = 5)
#	if cv == 7:
#		scores = cross_val_score(clf, wordscode, featurescode, cv = 7)
#	if cv == 9:
#		scores = cross_val_score(clf, wordscode, featurescode, cv = 9)
	#print(scores)
	#print('The mean score after cross-validation is: ', sum(scores)/cv)
###################################
	return y,y_pred


# This function takes the list of proteins as an input and translates it into its code for sklearn. It returns 'wordscode, featurescode' which are the X and y inputs to SVM

def prot2vect_psiblast(title_list, seq_list, feature_list,ws,pssm_data_folder):

	import numpy as np
	cont = 0
	words = list()
	seq_num_dict = {}
	wordscode = list()
	word_ws_list = list()


	features = list() # List to append all the words with the specified window size
	features_dict = {} # Dictionary used as intermediate data structure to play with features.
	featurescode = list() # Final list for the features, It is the output that returns the y values for the SVM


	ext = [0]


	for seq in seq_list:


		s = np.arange(1,len(seq)+1) # The key idea (my approach) of the translation is here
		extvect = ext*(int((ws-1)/2)) #Extending the word at the terminals according to the window size
		seqnum = extvect + s.tolist() + extvect
		seq_num_dict[title_list[cont]] = seqnum
		features_dict[title_list[cont]] = feature_list[cont]
		cont = cont + 1


 # This list has the sequences given by position (the position of each amino acid has replaced the amino acid, so that, I have made sequences with numbers instead)
	cont = 0
# This step takes each sequence (in numbers: seqnum). I create the dictionary according to each sequence by using the specific pssm file.

	for seqname in seq_num_dict.keys():

		file_path = pssm_data_folder  + '/' +  seqname + '.fasta.pssm'

		feature_dict, aapos2vect_dict = dictionaries_psiblast(pssm_data_folder, seqname)

		# For each sequence, make its words according to window size

		word = seq_num_dict[seqname]
		feature = features_dict[seqname]

		word_ws_list = list()
		for i in range(0,(len(word)-ws+1)): #create words with the given window size 'ABC'
			word_ws_list.append(word[i:i+ws])
			features.append(feature[i])


# Up to here, the list with all the words with ws for one sequence has been done. Now, it comes the last step where we translate that word into its aa frequencies


		for k in word_ws_list:
			w = list()
			for j in k: #j is a word with the given window size that now is going to be translated into code
				w = w + (aapos2vect_dict[j]) #optimization, this dictionary should have integers better
				
			wordscode.append(w)



	for i in features:
		featurescode.append(feature_dict[i])
	
	return wordscode, featurescode





#CREATE DICTIONARIES FOR EACH AMINO ACID POSITION:
# This function reads the corresponding pssm data file and stores the evolutionary information of each amino acid position of a sequence into a dictionary
# whose IDs are the position number
def dictionaries_psiblast(pssm_data_folder, seqID):

	import numpy as np
	import os 
	filename = os.path.join(pssm_data_folder, seqID + '.fasta.pssm')
	f = open(filename,'r')
	content = f.readlines()
	content = [x.strip() for x in content] #Each line is an entry of the a list


	aapos2vect_dict = {}
	aapos2vect_dict[0] = [0.0]*20 #include the filler
	#pos_dict = {}
	
	for i in range(3,len(content)-6): # This range due to the pssm file characteristics. this loop gets the frequencies vectors of each aa position. It is sort of the parser.
		line = content[i].split()
		aaposition = line[0]

		strvector = line[22:42]

		strvector = list(map(int, strvector))
		strvector = [j/100 for j in strvector]

		aapos2vect_dict[int(aaposition)] = strvector
	

	feature_dict = {}  # Dictionary to convert my feature into 0s and 1s
	feature_dict['b'] = 1
	feature_dict['e'] = 0


	return feature_dict, aapos2vect_dict



# EXTRACT THE FEATURE

#Read FASTA file (database) and return separatedly as lists the ids, the sequence and feature
# This FASTA reader is prepared for reading the database used in this project

def read_fasta(filename):
	f = open(filename,'r')
	content = f.readlines()
	content = [x.strip() for x in content] #Each line is an entry of the a list

# Create 3 lists containing different types of info: id names, sequences and feature

	title_list = list()
	seq_list = list()
	feature_list = list()

	for i in content:
		if '>' in i:
			title_list.append(i[1:])
		if i.isupper():
			seq_list.append(i)
		if i.islower() and '>' not in i:
			feature_list.append(i)
			
			
	f.close()
	return title_list, seq_list, feature_list
