from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def unify_pairedseq(file1, format1, file2, format2):
        rec_f = SeqIO.parse(file1, format1)
        rec_r = SeqIO.parse(file2, format2)
        uniqueseq = [[next(rec_f), next(rec_r)]]
        while True:
            try:
                seq_f = next(rec_f)
                seq_r = next(rec_r)
            except StopIteration:
                break
            else:
                for i in uniqueseq:
                    if str(i[0].seq) == str(seq_f.seq) and str(i[1].seq) == str(seq_r.seq):
                        break
                else:
                    uniqueseq.append([seq_f, seq_r])
        return uniqueseq


inputfq1 = "test2_1.fastq"
inputfq2 = "test2_2.fastq"
inputfa1 = "test2_1.fa"
inputfa2 = "test2_2.fa"
outputf1 = "test2_1_unique.fa"
outputf2 = "test2_2_unique.fa"
print(next(SeqIO.parse(inputfq1, "fastq")))

SeqIO.convert(inputfq1, "fastq", inputfa1, "fasta")
SeqIO.convert(inputfq2, "fastq", inputfa2, "fasta")

uniqueseq = unify_pairedseq(inputfa1, "fasta", inputfa2, "fasta")

with open(outputf1, "w") as outfile:
    for i in uniqueseq:
        seq1 = i[0]
        SeqIO.write(seq1, outfile, "fasta")
with open(outputf2, "w") as outfile:
    for i in uniqueseq:
        seq2 = i[1]
        SeqIO.write(seq2, outfile, "fasta")
