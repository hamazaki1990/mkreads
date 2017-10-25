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


read = make_reads("test2.fa", "fasta", 5)

print(next(read))
print(next(read))
