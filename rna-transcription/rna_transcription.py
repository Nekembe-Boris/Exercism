def to_rna(dna_strand):
    nucleotide = {"G":"C", "C":"G", "T":"A", "A":"U"}
    return "".join([nucleotide[char] for char in dna_strand])

#alternative
# LOOKUP = str.maketrans("GCTA", "CGAU")

# def to_rna(dna_strand):
#     return dna_strand.translate(LOOKUP)
