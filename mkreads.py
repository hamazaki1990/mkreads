from Bio import SeqIO
import pysam


def collect_kmers(file, k):
    for seq_record in SeqIO.parse(file, "fasta"):
        i = 0
        while True:
            yield seq_record.seq[i:i+k]
            i += 1


kmers = collect_kmers("test.fa", 3)


header = { 'HD': {'VN': '1.0'},
            'SQ': [{'LN': 1575, 'SN': 'chr1'},
                   {'LN': 1584, 'SN': 'chr2'}] }

testseq=[["read_28833_29006_6945", "AGCTTAGCTAGCTACCTATATCTTGGTCTTGGCCG"],
          ["read_28833_29006_6946", "AGCTTAGCTAGCTACCTATATCTTGGTCTTGGGGG"]]

with pysam.AlignmentFile("test.bam", "wb", header=header) as outf:
    for i in testseq:
        a = pysam.AlignedSegment()
        a.query_name = i[0]
        a.query_sequence=i[1]
        a.flag = 99
        a.reference_id = 1
        a.reference_start = 32
        a.mapping_quality = 20
        a.cigar = ((0,10), (2,1), (0,25))
        a.next_reference_id = 0
        a.next_reference_start=199
        a.template_length=167
        a.query_qualities = pysam.qualitystring_to_array("I"*35)
        a.tags = (("NM", 1),
                  ("RG", "L1"))
        outf.write(a)
