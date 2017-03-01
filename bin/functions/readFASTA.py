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








