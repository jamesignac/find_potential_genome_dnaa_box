# find_potential_genome_dnaa_box
Program to find potential DnaA boxes in a genome.

This is a program that examines an inputted genome of choice (assuming you have a full string for the genome). 

To find potential DnaA boxes, the program must find the genome's oriC.

It finds the position of the oriC by locating the index where the difference between Guanine and Cytosine is least. It then creates a 500-character window to search for 9-mers. For each 9-mer, it keeps track of its reverse complements and mismatches within d mismatches of the original 9-mer. It then stores the most frequent 9-mers in a list that is returned as potential DnaA boxes in the genome.
