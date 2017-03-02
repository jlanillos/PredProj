# This function takes a protein sequence as an input and translates it into its code for sklearn

def prot2vect(seq_list, feature_list,ws):

#feature <aa> <value> <aa> <value> ... <aa value> 
#First column = feature (for example 0 = H = HELIX ; 1 = E = BETA ; 2 = C = COIL)
#<aa> = amino-acid = <aa> ( A = 1; G = 2 and so on)
#<value> = 0 or 1 (this is valid when you have single sequence)
	from dictionaries import dictionaries
	aa_dict, feature_dict, aa2vect_dictionary = dictionaries()
	cont = 0
	seq2code = list()
	words = list()
	features = list()
	wordscode = list()
	featurescode = list()
	for seq in seq_list:
		ext = 'o' * int((ws-1)/2)
		extseq = ext + seq + ext #Extended sequence with o to deal with the ws issue
		feature_seq = feature_list[cont]
		cont = cont + 1
		for i in range(0,len(seq)):
			words.append(extseq[i:i+ws])
			features.append(feature_seq[i])
		
	for i in words:
		w = ''
		for j in i: #i is a word with the given window size that now is going to be translated into code
			w = w + (aa2vect_dictionary[j])
		wordscode.append(w)

	for i in features:
		featurescode.append(feature_dict[i])
		
	return wordscode, featurescode

wordscode, featurescode = prot2vect(seq_list, feature_list,ws)





#	import numpy as np
#dic_vect = np.arange(1,len(aa_dict)+1)
#		for i in seq:
#			aux_vector = np.zeros(len(aa_dict))
#			print(aux_vector)
#			aux_vector[aa_dict[i]-1] = 1 # Put a 1 at the position it corresponds to the aa involved
#			print(aux_vector)
#			my_vector = np.empty((aux_vector.size + dic_vect.size), dtype=dic_vect.dtype)
#			my_vector[0::2] = dic_vect
#			my_vector[1::2] = aux_vector
#			final_vector = np.zeros(len(my_vector)+1)
#			final_vector[0] = feature_dict[feature[cont]]
#			final_vector[1:] = my_vector
#			cont = cont + 1
#			seq2code.append(final_vector)
#	return seq2code


		
#	from dictionaries import dictionaries
#	aa_dict, feature_dict = dictionaries()
#	import numpy as np
#	dic_vect = np.arange(1,len(aa_dict)+1)
#	cont = 0
#	seq2code = list()


# with 0 1 0 2 0 3 0 4 0 5 0 6 0....20 0
#	for seq in seq_list:
#		for i in seq:
#			aux_vector = np.zeros(len(aa_dict))
#			print(aux_vector)
#			aux_vector[aa_dict[i]-1] = 1 # Put a 1 at the position it corresponds to the aa involved
#			print(aux_vector)
#			my_vector = np.empty((aux_vector.size + dic_vect.size), dtype=dic_vect.dtype)
#			my_vector[0::2] = dic_vect
#			my_vector[1::2] = aux_vector
#			final_vector = np.zeros(len(my_vector)+1)
#			final_vector[0] = feature_dict[feature[cont]]
#			final_vector[1:] = my_vector
#			cont = cont + 1
#			seq2code.append(final_vector)
#	return seq2code


		
		




