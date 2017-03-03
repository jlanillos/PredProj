#This file creates FASTA files with one single protein sequence of my dataset in order to run psiblast with each of them


import os
save_folder = '/home/u2188/PredProj/data/datasets/separated_seqs'
read_file = '/home/u2188/PredProj' #Write the main path to the project directory
#os.chdir (main_path)
filename = os.path.join('/home/u2188/PredProj', 'data','datasets','buried-exposed.3line.txt')
#filename = os.path.join('/home/u2188/PredProj', 'data','datasets','buried-exposed_TRIAL.txt')
#main_file = 'buried-exposed_TRIAL.txt'



#Read FASTA file (database) and return separatedly as lists the ids, the sequence and feature
def createFASTA(filename):
	f = open(filename,'r')
	content = f.readlines()
	content = [x.strip() for x in content] #Each line is an entry of the a list
	f.close()
# Create 3 lists containing different types of info: id names, sequences and feature

	dict_list ={}
	seq_list = list()
	feature_list = list()

	for i in content:
		if '>' in i:
			curr_id = i
			#title_list.append(i[1:])
		if i.isupper():
			dict_list[curr_id] = i
			#seq_list.append(i)
		#if i.islower() and '>' not in i:
			
			#feature_list.append(i)

	for i in dict_list.keys():
		f = open(save_folder + '/' + i[1:] + '.fasta','w')
		f.write(i + '\n')
		f.write(dict_list[i])
		f.close()
																											

	return;

createFASTA(filename)


