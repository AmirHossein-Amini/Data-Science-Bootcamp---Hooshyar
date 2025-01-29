dna_strand = "AAGAATTCGGAATTCCGGAATTC"
enzym = "GAATTC"

l = len(enzym)
fragments = dna_strand.split(enzym)  # Split DNA at enzyme site
filter_fragments = [frag for frag in fragments if frag] # filter null values

cut_positions = []
start = 0

i = 0
while i < dna_strand.count(enzym):  # Loop through all occurrences of enzyme
    cut_idx = dna_strand.find(enzym, start)  # Correctly find next occurrence
    cut_positions.append(f"{cut_idx} - {cut_idx + l - 1}")
    start = cut_idx + l  # Move forward to find the next occurrence
    i += 1

# Output
print("Cut Positions:", ", ".join(cut_positions))
print("DNA Fragments:", filter_fragments)