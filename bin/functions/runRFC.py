# Script that runs the necessary functions for SVM WITH EVOLUTIONARY DATA

# Script that runs every step necessary to perform SVM and SVM itself


def runSVM(main_path,data_path,bin_path,dataset_file,pssm_data_folder,ws,cv):
	# Read FASTA
	
	#import os
	import datetime
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.model_selection import cross_val_score
	import math
	from sklearn.metrics import confusion_matrix
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import classification_report




	filename = data_path + '/' + dataset_file
	title_list, seq_list, feature_list = read_fasta(filename)


	# Dictionaries to use them and code aminoacids into vectors. Outputs: aa2vector feature_dict(Name of the function: dictionaries). No inputs required
	path2functions = bin_path  + '/' + 'functions'
	#aa_dict, feature_dict, aa2vect_dictionary = dictionaries_psiblast()

	# Arrange data as input for sklearn

	wordscode, featurescode = prot2vect_psiblast(title_list, seq_list, feature_list,ws,pssm_data_folder)


	# Create training and test datasets and perform cross-validation

	#cv is the number of sets are created for the cross validation.


#RUNNING SVM

	X = wordscode
	y = featurescode

	clf = RandomForestClassifier(n_estimators = cv)

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
	clf.fit(X_train, y_train)
	y_pred = clf.predict(X_test)





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
	return y_test,y_pred


	# This function takes the list of proteins as an input and translates it into its code for sklearn

def prot2vect_psiblast(title_list, seq_list, feature_list,ws,pssm_data_folder):

	import numpy as np
	cont = 0
	words = list()
	seq_num_dict = {}
	wordscode = list()
	word_ws_list = list()


	features = list()
	features_dict = {}
	featurescode = list()



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

		#if os.path.exists(file_path):
		feature_dict, aapos2vect_dict = dictionaries_psiblast(pssm_data_folder, seqname)
		#print(feature_dict)
		# For each sequence, make its words according to window size

		word = seq_num_dict[seqname]
		feature = features_dict[seqname]

		word_ws_list = list()
		for i in range(0,(len(word)-ws+1)): #create words with the given window size 'ABC'
			word_ws_list.append(word[i:i+ws])
			features.append(feature[i])
		#print(len(word_ws_list))

# Up to here, the list with all the words with ws for one sequence has been done. Now, it comes the last step where we translate that word into its aa frequencies


		for k in word_ws_list:
			w = list()
			for j in k: #j is a word with the given window size that now is going to be translated into code
				w = w + (aapos2vect_dict[j]) #optimization, this dictionary should have integers better
				
			wordscode.append(w)

		#print(len(features))

	for i in features:
		featurescode.append(feature_dict[i])
	
	return wordscode, featurescode





#Create dictionaries for aminoacid names
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


		#pos_dict[int(aaposition)] = aaletter

	#aa_dict = {'A': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11, 'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'X':20, 'Y':21,'o':0}	

	feature_dict = {}
	feature_dict['b'] = 1
	feature_dict['e'] = 0


	return feature_dict, aapos2vect_dict
 	#return pos_dict, feature_dict, aapos2vect_dict
# First, I made a search of the present aminoacids in all my sequences at the dataset in order to create the dictionary above:
# {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'N', 'P', 'Q', 'R', 'T', 'V', 'W', 'Y'}


# EXTRACT THE FEATURE
# working with filename = '~/PredProj/data/datasets/buried-exposed.3line.txt'
#Read FASTA file (database) and return separatedly as lists the ids, the sequence and feature
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





