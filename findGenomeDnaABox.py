def min_skew_position(genome):
    skew = 0
    min_skew = 0
    min_skew_pos = [0]

    for i in range(len(genome)):
        if genome[i] == 'C':
            skew -= 1
        elif genome[i] == 'G':
            skew += 1

        if skew < min_skew:
            min_skew = skew
            min_skew_pos = [i + 1]
        elif skew == min_skew:
            min_skew_pos.append(i + 1)

    return min_skew_pos

def hamming_distance(str1, str2):
    ham_dist = 0
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")

    for i in range(len(str1)):
         if str1[i] != str2[i]:
              ham_dist+=1
         else:
             ham_dist+=0
    return ham_dist

def reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(pattern))

def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return set(nucleotides)

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in nucleotides:
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood

def find_dnaa_boxes(genome, k=9, d=1):
    dnaa_boxes = set()

    for i in range(len(genome) - k + 1):
        pattern = genome[i:i + k]
        pattern_neighbors = neighbors(pattern, d)  # Use the neighbors function to find potential boxes

        for neighbor in pattern_neighbors:
            dnaa_boxes.add(neighbor)

    return dnaa_boxes

# Function to find DnaA boxes in a specified window after the minimum skew position
def find_dnaa_boxes_in_window(genome, start_pos, window_size, k=9, d=1):
    window_end = min(start_pos + window_size, len(genome))
    window = genome[start_pos:window_end]
    print("Extracted Window:", window)  # Print the extracted window for verification

    dnaa_boxes = []
    for i in range(len(window) - k + 1):
        pattern = window[i:i + k]
        print("Pattern in Window:", pattern)  # Print the current pattern within the window

        pattern_neighbors = neighbors(pattern, d)  # Use the neighbors function to find potential boxes

        for neighbor in pattern_neighbors:
            dnaa_boxes.append(neighbor)

    return dnaa_boxes

#MAIN

genome_text = input("Enter genome: ")
salmonella_genome_text = genome_text.replace('\n', '').replace(' ', '')

# Find the position where the skew is at its minimum
min_skew_positions = min_skew_position(genome_text)
print(min_skew_positions)

min_skew_pos = min_skew_positions[0]  # Using the first minimum skew position found

    # Define a window size of 500 bases after the minimum skew position
window_size = 500

    # Search for DnaA boxes in the specified window after the minimum skew position
dnaa_boxes_in_window = find_dnaa_boxes_in_window(genome_text, min_skew_pos, window_size)

    # Print the identified potential DnaA boxes in the specified window
print("Identified potential DnaA boxes in the specified window after minimum skew position:")
for box in dnaa_boxes_in_window:
    print(box)
