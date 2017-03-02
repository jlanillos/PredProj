#Create dictionaries for aminoacid names
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
	
	for i in aa2vect_dictionary:
		
		
	return aa_dict, feature_dict, aa2vect_dictionary

# First, I made a search of the present aminoacids in all my sequences at the dataset in order to create the dictionary above:
# {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'N', 'P', 'Q', 'R', 'T', 'V', 'W', 'Y'}

