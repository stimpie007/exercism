def to_rna(dna_strand):
    """
    Returns the RNA for a DNA strand

    :param
    dna_strand: string

    :return:
    RNA: string
    """
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))