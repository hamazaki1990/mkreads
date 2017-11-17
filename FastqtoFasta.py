from Bio import SeqIO

for i in [1, 2]:
    SeqIO.convert("DXZ1artificial_DXZ1_al%s.fastq" %i, "fastq", "DXZ1artificial_DXZ1_al%s.fasta" %i, "fasta")





