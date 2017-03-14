# run a psi-blast search with buried_exposed.3line.txt.
#the document had to be transformed in previous steps into multiple fasta files.


#change directory to uniref90 
export BLASTDB=/local_uniref/uniref/uniref90

for seq in ~/PredProj/data/datasets/separated_seqs_50new/*.fasta ; do
#for seq in ~/PredProj/data/datasets/separated_seqs/d1a6vh_.b.1.1.1.fasta ; do

#"safety step" to check if the files have been created already in the output directory in case that the computer shuts down or others


if [ ! -f $output_directory/$base.psi ]; then
	echo "Running psiblast on $seq at $(date)..."
	time psiblast -query $seq -db uniref90.db -num_iterations 3 -evalue 0.001 -out $seq.psiblast -out_ascii_pssm $seq.pssm -num_threads 8
	echo "Finished running psiblast on $seq at $(date)."
fi
done

#Know when the iterations are done we will echo:
echo 'PSI-BLAST run is complete'

# I move all the files from the data_files folder to psiblast_output folder as desired
cd ~/PredProj/data/datasets/separated_seqs_50new/
mv *.psiblast ~/PredProj/data/datasets/psi_blast_50new/
mv *.pssm ~/PredProj/data/datasets/psi_blast_50new/
