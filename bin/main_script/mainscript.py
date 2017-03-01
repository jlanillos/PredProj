# This is the main script that runs the whole analysis

print ('Welcome to the surface exposition residues predictor by using SVM')
import os
main_path = '~/PredProj' #Write the main path to the project directory
cd main_path
data_path = os.path.join(main_path, 'data','datasets')
dataset_file = 'buried-exposed.3line.txt'
bin_path = os.path.join(main_path, 'bin')

# PARAMETERS

#add prefiltering or others

ws = 15 #window size of the vectors
kernel = '' #Choose the kernel function for SVM


# RUN SUPPORT VECTOR MACHINE ANALYSIS



