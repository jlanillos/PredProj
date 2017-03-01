#Create dictionaries for aminoacid names
def dictionaries():

	import numpy as np

	aa_dict = {'A': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11, 'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'X':20, 'Y':21}	

	feature_dict = {}
	feature_dict['b'] = 1
	feature_dict['e'] = 0

	return aa_dict, feature_dict

# First, I made a search of the present aminoacids in all my sequences at the dataset in order to create the dictionary above:
# {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'N', 'P', 'Q', 'R', 'T', 'V', 'W', 'Y'}

