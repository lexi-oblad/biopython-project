from Bio import SeqIO
sequences = [gen for gen in SeqIO.parse("dataset/genome.fna", "fasta")]
covid_seq_record = sequences[0]
#assert len(covid_seq_record.seq) % 3 == 0

# remove last 2 characters to allow translate without warning: must be divible 3
covid_seq_record.seq = covid_seq_record.seq[:-2]
assert len(covid_seq_record.seq) % 3 == 0

print(f"Length: { len(covid_seq_record.seq) }")
print(f"Original DNA: {covid_seq_record.seq[:100]}")
print("transcribing mRNA")
mRNA = sequences[0].seq.transcribe()
print(len(mRNA) % 3)
print("Transcribed DNA to mRNA: " + mRNA[:99])
protein = mRNA.translate()
print("Amino Acid Sequence: " + protein[:33])
proteins = protein.split("*")
print(proteins[:50])
