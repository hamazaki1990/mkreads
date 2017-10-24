from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def make_fragment(file, format, fraglength):
    for seq_record in SeqIO.parse(file, format):
        i = 0
        while True:
            yield seq_record.seq[i:i+fraglength]
            i += 30


chroms = [str(i) for i in range(1, 23)]
chroms.extend(["X", "Y"])
print(chroms)

for i in chroms:
    inputf = "chr"+i+".fa"
    outputf = "fragment_chr"+i+".fa"
    fragment = make_fragment(inputf, "fasta", 100)

    with open(outputf, "w") as outfile:
        x = 0
        while True:
            seq = next(fragment)
            record = SeqRecord(seq, id=str(x), description=inputf+"fragment")
            if len(seq) < 80:
                break
            elif float(seq.count("N")) < 1:
                SeqIO.write(record, outfile, "fasta")
            x += 1
