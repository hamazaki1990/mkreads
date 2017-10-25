from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import random


def make_reads(file, format, readlength):
    for seq_record in SeqIO.parse(file, format):
        reclength = len(seq_record)
        while True:
            start1 = random.randint(0, reclength-1)
            end1 = start1 + readlength
            space = random.randrange(3, 5)
            start2 = end1 + space
            end2 = start2 + readlength
            if end1 > reclength:
                seq1 = seq_record.seq[start1:]+seq_record.seq[:end1-reclength]
                seq2 = seq_record.seq[start2-reclength:end2-reclength]
            elif start2 > reclength:
                seq1 = seq_record.seq[start1:end1]
                seq2 = seq_record.seq[start2-reclength:end2-reclength]
            elif end2 > reclength:
                seq1 = seq_record.seq[start1:end1]
                seq2 = seq_record.seq[start2:]+seq_record.seq[:end2-reclength]
            else:
                seq1 = seq_record.seq[start1:end1]
                seq2 = seq_record.seq[start2:end2]
            yield [seq1, seq2]


inputf = "test2.fa"
read = make_reads(inputf, "fasta", 5)
outputf1 = "test2_1.fastq"
outputf2 = "test2_2.fastq"
x = 0
while x < 10:
    paired = next(read)
    print(pairedreads)
    rec1 = SeqRecord(paired[0], id="read_"+str(x), description=inputf+"_1")
    rec2 = SeqRecord(paired[1], id=+"read_"+str(x), description=inputf+"_2")
    rec1.letter_annotations["phred_quality"] = [40] * len(pairedreads[0])
    rec2.letter_annotations["phred_quality"] = [40] * len(pairedreads[1])
    print([rec1, rec2])

    with open(outputf1, "a") as outfile:
        SeqIO.write(rec1, outfile, "fastq")
    with open(outputf2, "a") as outfile:
        SeqIO.write(rec2, outfile, "fastq")
    x += 1
