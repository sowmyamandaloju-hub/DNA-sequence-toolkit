
from dna_toolkit import validate_sequence, get_nucleotide_count

dna_seq = "ATCGGATCGAAGCT"
if validate_sequence(dna_seq):
    print("Valid DNA sequence.")
    print("Nucleotide Counts:", get_nucleotide_count(dna_seq))
else:
    print("Invalid DNA sequence.")
