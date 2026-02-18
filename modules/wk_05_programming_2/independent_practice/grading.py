# Author: Kira Vasquez-Kapit
# Last Edited: Tuesday Feb. 17, 2026

### This script will grade your completed exercises. You may run this script as many times as you like. Once all tests pass, the assignment is complete and you may submit on Canvas.
### Do not change any of the code in this file. Changing the code in this file will not affect your grade on the assignment.

# Package imports, so I can use functions that someone else wrote and published.
import unittest
import exercises


class TestSequences(unittest.TestCase):

    def test_equivalence(self):
        
        self.assertEqual(exercises.check_equivalence("ATCGATCGTATGCAT", "ATCGATCGTATCCAT"), False)

        self.assertEqual(exercises.check_equivalence("AUCGAUCGAUUACGCGC", "AUCGAUCGAUUACGCGC"), True)

    def test_variants(self):

        self.assertEqual(exercises.get_variants("AUCGAUCGAUUACGCGC", "AUCGAUCGAUUACGCGC"), [])

        self.assertEqual(exercises.get_variants("ATCGATCGTATGCAT", "ATCGATCGTATCCAT"), [11])

        self.assertEqual(exercises.get_variants("ATAGATCGTATGCAT", "ATCGATCGTATCCAT"), [2, 11])

        self.assertEqual(exercises.get_variants("TTAGATCGTATGCAT", "ATCGATCGTATCCAT"), [0, 2, 11])

    def test_seq_type(self):

        self.assertEqual(exercises.get_seq_type("TTAGATCGTATGCAT"), "DNA")

        self.assertEqual(exercises.get_seq_type("AUCGAUCGAUUACGCGC"), "RNA")

        self.assertEqual(exercises.get_seq_type("MSTNPKPQRKTKRNTNRRPQDVKFPGG"), "protein")

        self.assertEqual(exercises.get_seq_type("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "unknown")

    def test_point_mutation(self):

        self.assertEqual(exercises.type_of_point_mutation("AUCGAUCGAUUACGCGC", "AUCGAUCGAUUACGCGC"), "none")

        self.assertEqual(exercises.type_of_point_mutation("AUCGAUCGAUUACGCGC", "AUCGAUCGAUUGCGCGC"), "silent")

        self.assertEqual(exercises.type_of_point_mutation("AUCGAUCGAUUACGCGC", "AUCGAUCGAUUUCGCGC"), "missense")

        self.assertEqual(exercises.type_of_point_mutation("AUCGAUCGAUUACGCGC", "AUCGAUCGAUGACGCGC"), "nonsense")


class TestFiles(unittest.TestCase):

    def test_list_files(self):
        
        # If you are failing this test because you have a different set of files in your directory, don't worry about it! I will notice and give you credit.
        self.assertEqual(exercises.list_files(), ['exercise_solutions.py', 'grading.py', 'exercises.py'])

    def test_fasta(self):
        
        a = [">chr1", ">chr2", ">chr3", ">chr4", ">chr5"]
        self.assertEqual(exercises.extract_fasta_headers("fasta1.fa"), a)

        b = [">gene01|GENE1", ">gene02|GENE2", ">gene03|GENE3", ">gene04|GENE4", ">gene05|GENE5", ">gene06|GENE6", ">gene07|GENE7", ">gene08|GENE8", ">gene09|GENE9", ">gene10|GENE10",
            ">gene11|GENE11", ">gene12|GENE12", ">gene13|GENE13", ">gene14|GENE14", ">gene15|GENE15", ">gene16|GENE16", ">gene17|GENE17", ">gene18|GENE18", ">gene19|GENE19", ">gene20|GENE20",
            ">gene21|GENE21", ">gene22|GENE22", ">gene23|GENE23", ">gene24|GENE24", ">gene25|GENE25", ">gene26|GENE26", ">gene27|GENE27", ">gene28|GENE28", ">gene29|GENE29", ">gene30|GENE30",
            ">gene31|GENE31", ">gene32|GENE32", ">gene33|GENE33", ">gene34|GENE34", ">gene35|GENE35", ">gene36|GENE36", ">gene37|GENE37", ">gene38|GENE38", ">gene39|GENE39", ">gene40|GENE40"]
        self.assertEqual(exercises.extract_fasta_headers("fasta2.fa"), b)


if __name__=="__main__":
    unittest.main()
