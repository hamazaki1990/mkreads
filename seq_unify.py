from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def unify_pairedseq(file1, format1, file2, format2):
        rec_f = SeqIO.parse(file1, format1)
        rec_r = SeqIO.parse(file2, format2)
        uniqueseq = []
        while True:
            try:
                seq_f = next(rec_f)
                seq_r = next(rec_r)
            except StopIteration:
                break
            else:
                for pair in uniqueseq:
                    if pair[0] == seq_f.seq:
                        break
                    elif pair[1] == seq_r.seq:
                        break
                    else:
                        uniqueseq.append([seq_f.seq, seq_r.seq])
        return uniqueseq


inputf1 = "D11Z1artificial_DXZ1HOR_al_conc_1.fastq"
inputf2 = "D11Z1artificial_DXZ1HOR_al_conc_2.fastq"
outputf1 = "D11Z1artificial_DXZ1HOR_al_conc_1_unique.fasta"
outputf2 = "D11Z1artificial_DXZ1HOR_al_conc_2_unique.fasta"

uniqueseq = unify_pairedseq(inputf1, "fastq", inputf2, "fastq")

for i in uniqueseq:
    seq1 = SeqRecord(uniqueseq[0], id=str(i), description=inputf1+"_1")
    seq2 = SeqRecord(uniqueseq[1], id=str(i), description=inputf2+"_2")
    with open(outputf1, "w") as outfile:
        SeqIO.write(seq1, outfile, "fasta")
    with open(outputf2, "w") as outfile:
        SeqIO.write(seq2, outfile, "fasta")
