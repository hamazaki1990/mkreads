from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def make_fragment(file, format, fraglength):
    for seq_record in SeqIO.parse(file, format):
        i = 0
        while True:
            yield seq_record.seq[i:i+fraglength]
            i += 1


fragment = make_fragment("test.fa", "fasta", 3)

with open("outputtest.fa", "w") as outfile:
    x = 0
    while True:
        record = SeqRecord(next(fragment), id=str(x), description="fragment")
        if len(record) < 2:
            break
        SeqIO.write(record, outfile, "fasta")
        x += 1
