# This function takes a protein sequence as an input and translates it into its code for sklearn

def prot2vect(seq, feature):

#feature <aa> <value> <aa> <value> ... <aa value> 
#First column = feature (for example 0 = H = HELIX ; 1 = E = BETA ; 2 = C = COIL)
#<aa> = amino-acid = <aa> ( A = 1; G = 2 and so on)
#<value> = 0 or 1 (this is valid when you have single sequence)

	from dictionaries import dictionaries

	aa_dict, feature_dict = dictionaries()

	import numpy as np

	
	dic_vect = np.arange(1,len(aa_dict)+1)
	cont = 0
	seq2code = list()

	for i in seq:
		
		aux_vector = np.zeros(len(aa_dict))
		print(aux_vector)
		aux_vector[aa_dict[i]-1] = 1 # Put a 1 at the position it corresponds to the aa involved
		print(aux_vector)
		my_vector = np.empty((aux_vector.size + dic_vect.size), dtype=dic_vect.dtype)
		my_vector[0::2] = dic_vect
		my_vector[1::2] = aux_vector
		final_vector = np.zeros(len(my_vector)+1)
		final_vector[0] = feature_dict[feature[cont]]
		final_vector[1:] = my_vector
		cont = cont + 1
		seq2code.append(final_vector)

	return seq2code


		
		




