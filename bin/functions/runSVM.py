# Script that runs every step necessary to perform SVM and SVM itself
import os
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import math
import pickle	

def runSVM(main_path,data_path,bin_path,dataset_file,ws,kern,cv,C,save_model_path):

	#Read the FASTA that contains all proteins
	filename = os.path.join(data_path,dataset_file)
	title_list, seq_list, feature_list = read_fasta(filename)



	# Arrange data as input for sklearn
	wordscode, featurescode = prot2vect(seq_list, feature_list, ws)

#RUNNING SVM

	X = wordscode
	y = featurescode


	clf = SVC(C=C, kernel=kern, degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None, random_state=None)
	#clf = svm.LinearSVC(C=1)
	clf.fit(X, y)
	
	# Attempt to save the created model
	save_model_filename = kern+'_'+str(ws)+'_'+str(C)+'_'+str(cv)+'.sav'
	pickle.dump(clf, open(filename, 'wb'))


	y_pred = clf.predict(X)
	# Cross-validation scores. cv is the number of training datasets you choose in the main_script
	if cv == 3:
		scores = cross_val_score(clf, wordscode, featurescode, cv = 3)
	if cv == 5:
		scores = cross_val_score(clf, wordscode, featurescode, cv = 5)
	if cv == 7:
		scores = cross_val_score(clf, wordscode, featurescode, cv = 7)
	if cv == 9:
		scores = cross_val_score(clf, wordscode, featurescode, cv = 9)

	return scores,y,y_pred




# This function takes the list of proteins as an input and translates it into its code for sklearn. It returns 'wordscode, featurescode' which are the X and y inputs to SVM

def prot2vect(seq_list, feature_list,ws):



	aa_dict, feature_dict, aa2vect_dictionary = dictionaries() # This dictionary does not uses the evolutionary data from pssm files.
	cont = 0
	seq2code = list()
	words = list()
	features = list()
	wordscode_aux = list()
	wordscode = list()
	featurescode = list()

	for seq in seq_list:
		ext = 'o' * int((ws-1)/2)
		extseq = ext + seq + ext #Extended sequence with 'o' to deal with the ws issue
		feature_seq = feature_list[cont]
		cont = cont + 1
		for i in range(0,len(seq)):
			words.append(extseq[i:i+ws])
			features.append(feature_seq[i])
		
	for i in words:
		w = ''
		for j in i: #i is a word with the given window size that now is going to be translated into code
			w = w + (aa2vect_dictionary[j]) #optimization, this dictionary should have integers better
		wordscode_aux.append(w)

	for i in wordscode_aux:
		t_aux = list()
		for j in i:
			t_aux.append(int(j))
		wordscode.append(t_aux)
	for i in features:
		featurescode.append(feature_dict[i])
		
	return wordscode, featurescode



# CREATE THE DICTIONARY FOR EACH AMINO ACID NAME (No evolutionary data)
def dictionaries():

	import numpy as np

	aa_dict = {'A': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11, 'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'X':20, 'Y':21,'o':0}	

	feature_dict = {}
	feature_dict['b'] = 1
	feature_dict['e'] = 0

	aa2vect_dictionary = {}

	for i in aa_dict:
		
		aux_vector = np.zeros(len(aa_dict)-1)
		if i == 'o':
			aux_vector = np.array_str(aux_vector)
			aa2vect_dictionary[i] = aux_vector.replace('.','').replace('\n','').replace('[','').replace(']','').replace(' ','')
		else:
			aux_vector[aa_dict[i]-1] = 1 # Put a 1 at the position it corresponds to the aa involved
			aux_vector = np.array_str(aux_vector)
			aa2vect_dictionary[i] = aux_vector.replace('.','').replace('\n','').replace('[','').replace(']','').replace(' ','')

	return aa_dict, feature_dict, aa2vect_dictionary

	


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



