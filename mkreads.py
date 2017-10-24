from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import random


def make_reads(file, format, readlength):
    for seq_record in SeqIO.parse(file, format):
        reclength = len(seq_record)
        while True:
            start1 = random.randint(0, reclength-1)
            end1 = start1 + readlength
            space = random.randrange(200, 500, 50)
            start2 = start1 + space
            end2 = start2 + readlength
            if end1 > reclength:
                seq1 = seq_record.seq[start1:]+seq_record.seq[:end1-reclength]
                seq2 = seq_record.seq[start2:end2]
            elif start2 :
                seq1 = seq_record.seq[start:start+readlength]
            yield [seq1, seq2]


fragment = make_read(test1.fa, "fasta", 5)

    with open(outputf, "w") as outfile:
        x = 0
        while True:
            seq = next(fragment)
            record = SeqRecord(seq, id=str(x), description=inputf+"fragment")
            if len(seq) < 80:
                break
            elif float(seq.count("N")) < 1:
                SeqIO.write(record, outfile, "fastq")
            x += 1
