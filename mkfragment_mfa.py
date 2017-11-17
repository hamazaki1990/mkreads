from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


rec_iter = SeqIO.parse("test.fa", "fasta")

def make_fragment(cdna, fraglength):
        i = 0
        while True:
            yield cdna.seq[i:i+fraglength]
            i += 3


outputf = "fragment_from_mfa_test.fa"

with open(outputf, "w") as outfile:
    while True:
        cdna = next(rec_iter)
        x = 0
        fragment = make_fragment(cdna, 10)
        while True:
            seq = next(fragment)
            record = SeqRecord(seq, id=cdna.id, description=cdna.description+str(x))
            if len(seq) < 5:
                break
            elif float(seq.count("N")) < 1:
                SeqIO.write(record, outfile, "fasta")
            x += 1

