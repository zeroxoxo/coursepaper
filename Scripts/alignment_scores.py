from Bio import pairwise2 as pw2
from Bio import SeqIO as sio

path = 'C:/Users/1/Desktop/Flash/Vlad/2BCMES_FASTA/2BCMES.fa'
seq = []
for seq_record in sio.parse(path, "fasta"):
    seq.append(seq_record)

print(seq[3])


dna1 = 'AAAGCC'
dna2 = 'AAGTTC'

alignments = pw2.align.globalxx(dna1, dna2, score_only=True)

