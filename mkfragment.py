from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def make_fragment(file, format, fraglength):
    for seq_record in SeqIO.parse(file, format):
        i = 0
        while True:
            yield seq_record.seq[i:i+fraglength]
            i += 30


fragment = make_fragment("chr1.fa", "fasta", 100)

with open("fragment_chr1.fa", "w") as outfile:
    x = 0
    while True:
        seq = next(fragment)
        record = SeqRecord(seq, id=str(x), description="fragment")
        if len(seq) < 80:
            break
        elif float(seq.count("N")) < 20:
            SeqIO.write(record, outfile, "fasta")
        x += 1
