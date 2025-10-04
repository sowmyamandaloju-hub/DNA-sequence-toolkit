
def count_nucleotides(seq):
    """Count A, T, G, C in a DNA sequence."""
    seq = seq.upper()
    return {n: seq.count(n) for n in "ATGC"}

def transcribe_dna(seq):
    """Transcribe DNA to RNA (T -> U)."""
    return seq.upper().replace("T", "U")

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complement[n] for n in reversed(seq.upper()))

def gc_content(seq):
    """Calculate GC content (%) of a DNA sequence."""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

def main():
    # Ask user for a DNA sequence
    dna_seq = input("Enter a DNA sequence: ").strip().upper()

    # Outputs
    counts = count_nucleotides(dna_seq)
    rna_seq = transcribe_dna(dna_seq)
    rev_comp = reverse_complement(dna_seq)
    gc = gc_content(dna_seq)

    print("\nResults:")
    print(f"Nucleotide counts: {counts}")
    print(f"Transcription (RNA): {rna_seq}")
    print(f"Reverse complement: {rev_comp}")
    print(f"GC content: {gc:.2f}%")

if __name__ == "__main__":
    main()
