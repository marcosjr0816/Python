def to_rna(dna_strand):
    rna_seq = ""
    for dna in dna_strand:
        rna_seq += "G" if dna == "C" else ""
        rna_seq += "C" if dna == "G" else ""
        rna_seq += "A" if dna == "T" else ""
        rna_seq += "U" if dna == "A" else ""
    return rna_seq
