from Bio import SeqIO
sequence = [gen for gen in SeqIO.parse("dataset/genome.fna", "fasta")]
covid_seq_record = sequence[0]
#assert len(covid_seq_record.seq) % 3 == 0
print("The genome of the SARS-CoV-2 virus has " +
      str(len(sequence[0])) + " base pairs.")

# remove last 2 characters to allow translate without warning: must be divible 3
covid_seq_record.seq = covid_seq_record.seq[:-2]
covid_seq = covid_seq_record.seq
assert len(covid_seq) % 3 == 0

print(f"Length: {len(covid_seq)}")
print(f"First 100 bp of virus DNA: {covid_seq[:100]}")
mRNA = covid_seq.transcribe()
print(len(mRNA) % 3)
print("Transcribed DNA to mRNA: " + mRNA[:99])
protein = mRNA.translate()
print("Amino Acid Sequence: " + protein[:33])
proteins = protein.split("*")
print(proteins[:10])
