#Create dictionaries for aminoacid names
def dictionaries
import numpy as np

aa2vector = {}
ref_list_aa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'O', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
zero_vector = np.zeros(len(ref_list_aa))


	for i in range(0:len(ref_list_aa)):
		aux_vector = zero_vector
		aux_vector[i] = 1
		aa2vector[ref_list_aa[i]] = aux_vector


feature_dict = {}
feature_dict['b'] = 1
feature_dict['e'] = -1

	return aa2vector feature_dict
