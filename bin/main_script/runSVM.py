# Script that runs every step necessary to perform SVM and SVM itself

def runSVM(main_path,data_path,bin_path,dataset_file,ws,kernel)


# Read FASTA

filename = os.path.join(data_path,dataset_file)

title_list, seq_list, feature_list = read_fasta(filename)


# Dictionaries to use them and code aminoacids into vectors. Outputs: aa2vector feature_dict(Name of the function: dictionaries). No inputs required


# Arrange data as input for sklearn


# Create training datasets and test datasets

# Built SVM model

# Run SVM
