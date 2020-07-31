from Bio import SeqIO
sequences = [gen for gen in SeqIO.parse("dataset/genome.fna", "fasta")]
print(len(sequences))
print(sequences[0])
