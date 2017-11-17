from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import random


def make_reads(file, format, readlength):
    for seq_record in SeqIO.parse(file, format):
        reclength = len(seq_record)
        while True:
            start1 = random.randrange(0, reclength)
            end1 = start1 + readlength
            insert = random.randrange(100, 501, 20)
            end2 = start1 + insert
            start2 = end2 - readlength
            pairedend = []
            if end1 > reclength:
                seq1 = seq_record.seq[start1:]+seq_record.seq[:end1-reclength]
            else:
                seq1 = seq_record.seq[start1:end1]
            pairedend.append(seq1)
            if start2 > reclength:
                seq2 = seq_record.seq[start2-reclength:end2-reclength]
            elif end2 > reclength:
                seq2 = seq_record.seq[start2:]+seq_record.seq[:end2-reclength]
            else:
                seq2 = seq_record.seq[start2:end2]
            pairedend.append(seq2.reverse_complement())
            yield pairedend

for i in range(1,10):
    inputf = "D1Z5_peri_5end_3.fa"
    read = make_reads(inputf, "fasta", 100)
    outputf1 = "%s_D1Z5_peri3_artificial_shortread_1.fastq" %i
    outputf2 = "%s_D1Z5_peri3_artificial_shortread_2.fastq" %i
    x = 0
    while x < 1000000:
        pairedr = next(read)
        rec1 = SeqRecord(pairedr[0], id="read_"+str(x), description=inputf+"_1")
        rec2 = SeqRecord(pairedr[1], id="read_"+str(x), description=inputf+"_2")
        rec1.letter_annotations["phred_quality"] = [40] * len(pairedr[0])
        rec2.letter_annotations["phred_quality"] = [40] * len(pairedr[1])
        if x == 0:
            with open(outputf1, "w") as outfile:
                SeqIO.write(rec1, outfile, "fastq")
            with open(outputf2, "w") as outfile:
                SeqIO.write(rec2, outfile, "fastq")
        else:
            with open(outputf1, "a") as outfile:
                SeqIO.write(rec1, outfile, "fastq")
            with open(outputf2, "a") as outfile:
                SeqIO.write(rec2, outfile, "fastq")
        x += 1
