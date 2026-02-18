### This script is where you should input your solutions in the designated areas only. There is a space at the bottom of the file to do your own code testing.
### Run grading.py to grade your assignment. You may run this script as many times as you'd like; I will evaluate your submissions myself with this exact script.

# This dictionary of RNA codons to amino acid symbols may be useful for some exercises!
codon_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

# You will likely need this package for list_files()
import os


### PART 1: ANALYZING SEQUENCES ###

# This function determines whether two string sequences are equivalent: returns True if they are equivalent, and False if they are not.
def check_equivalence(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###

# This function takes two string sequences and returns a list of the positions where they differ. Returns an empty list if the sequences are identical.
# You may assume both sequences are the same length.
def get_variants(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###

    return variant_list

# This function takes a string sequence and returns the type of sequence it is: DNA, RNA, protein, or unknown.
# Note: Technically, there are some sequences that could match multiple types. You can ignore these edge cases for this exercise.
def get_seq_type(seq):

    # You may use these lists if you want to!
    dna_chars = ["A", "G", "C", "T"]
    rna_chars = ["A", "G", "C", "U"]
    aa_chars = codon_dict.values().unique()

    ### YOUR CODE BELOW HERE ###

    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###

    return seq_type

# This function has been written for you. You may use it in type_of_point_mutation() if you want to!
def split_rna_to_codons(rna_seq):
    codon_list = []
    for i in range(0, len(rna_seq), 3):
        codon_list.append(rna_seq[i:i+3])
    return codon_list

# This function takes two RNA string sequences and returns the type of point mutation that differentiates them: silent, missense, or nonsense. 
# Return "none" if the sequences are identical. You can assume there is at most one point mutation between the two sequences, and that the sequences are of equal length.
# Hint: You can use the functions you already wrote above, and/or get_protein_seq() from last week's assignment 2.
def type_of_point_mutation(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###

    return mutation_type


### PART 2: FILES ###

# This function returns the list of files in the current directory.
def list_files():

    ### YOUR CODE BELOW HERE ###

    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###

    return files_list

# This function returns a list of all the header lines (start with '>') in a given FASTA file.
def extract_fasta_headers(filepath):

    ### YOUR CODE BELOW HERE ###

    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###

    return header_list


### TEST YOUR CODE DOWN HERE (IF YOU WANT TO) ###