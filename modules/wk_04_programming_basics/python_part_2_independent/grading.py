# Author: Kira Vasquez-Kapit
# Last Edited: Tuesday Feb. 10, 2026

### This script will grade your completed exercises. You may run this script as many times as you like. Once all tests pass, the assignment is complete and you may submit on Canvas.
### Do not change any of the code in this file. Changing the code in this file will not affect your grade on the assignment.

# Package imports, so I can use functions that someone else wrote and published. We will learn more about packages and functions next week.
import unittest
import assignment2


class TestLists(unittest.TestCase):

    def test_add(self):
        
        a = []
        self.assertEqual(assignment2.add_to_list(a, 5), [5])

        b = [1, 2, 3, 4]
        self.assertEqual(assignment2.add_to_list(b, 5), [5, 1, 2, 3, 4])

        c = ["cookie", "brownie", "cupcake", "pie"]
        self.assertEqual(assignment2.add_to_list(c, "ice cream"), ["ice cream", "cookie", "brownie", "cupcake", "pie"])

    def test_merge(self):

        a = [1, 2, 3]
        b = [4, 5, 6]
        self.assertEqual(assignment2.merge_lists(a, b), [1, 2, 3, 4, 5, 6])

        c = ["egg", "banana", "onion"]
        d = [3.14, 6.5, 7.9]
        self.assertEqual(assignment2.merge_lists(c, d), ["egg", "banana", "onion", 3.14, 6.5, 7.9])

    def test_remove(self):

        a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(assignment2.remove_from_list(a, 4), [1, 2, 3, 5, 6])

        b = ["dog", "cat", "fish", "snake", "bird", "alligator"]
        self.assertEqual(assignment2.remove_from_list(b, "alligator"), ["dog", "cat", "fish", "snake", "bird"])

        c = ["boat", "car", "car", "plane", "car", "train"]
        self.assertEqual(assignment2.remove_from_list(c, "car"), ["boat", "plane", "train"])

        d = [1, 1, 1, 1, 1, 1]
        self.assertEqual(assignment2.remove_from_list(d, 1), [])

        e = [3.2, 54.3, 1.0, 2.2, 7.3452, 98.342]
        self.assertEqual(assignment2.remove_from_list(e, 7), [3.2, 54.3, 1.0, 2.2, 7.3452, 98.342])


class TestDictionaries(unittest.TestCase):

    def test_dna_to_aa(self):

        a = ["ACU", "GAU", "CGA", "UCG", "UAG"]
        self.assertEqual(assignment2.get_protein_seq(a), ["T", "D", "R", "S", "*"])

        b = ["ACU", "GCG", "UUU", "GCG", "GGA", "UAC", "UCU", "UGA"]
        self.assertEqual(assignment2.get_protein_seq(b), ["T", "A", "F", "A", "G", "Y", "S", "*"])

        c = ["ACU", "GAU", "CGA", "UCG", "UAF"]
        self.assertEqual(assignment2.get_protein_seq(c), [])

        d = ["AMU", "GAU", "CGA", "UCG", "UAG"]
        self.assertEqual(assignment2.get_protein_seq(d), [])

class TestConditionals(unittest.TestCase):

    def test_b_grade(self):

        a = 84.0
        self.assertEqual(assignment2.check_if_b_grade(a), True)

        b = 90.0
        self.assertEqual(assignment2.check_if_b_grade(b), False)

        c = 89.9999999
        self.assertEqual(assignment2.check_if_b_grade(c), True)

        d = 80.0
        self.assertEqual(assignment2.check_if_b_grade(d), True)

        e = 47.0
        self.assertEqual(assignment2.check_if_b_grade(e), False)


class TestFileIO(unittest.TestCase):

    def test_count_word(self):
        
        self.assertEqual(assignment2.count_word_in_file("./file1.txt", "hence"), 1)
        self.assertEqual(assignment2.count_word_in_file("./file1.txt", "wood"), 2)
        self.assertEqual(assignment2.count_word_in_file("./file1.txt", "and"), 9)

    def test_write_file(self):
        
        assignment2.create_data_file(["sample_id", "num_cells", "treatment_group"], ["a837", "f85", "c975", "a292", "e399", "a21"], ["2345", "1345", "724", "2234", "0", "2356"], ["control", "A", "B", "control", "A", "B"])
        with open("./data.csv", "r") as file1:
            with open("./data.csv", "r") as file2:
                self.assertEqual(file1.read(), file2.read())

    def test_filter_data(self):

        assignment2.filter_data()
        with open("./tav.csv", "r") as file1:
            with open("./tav_solution.csv", "r") as file2:
                self.assertEqual(file1.read(), file2.read())
        with open("./andre.csv", "r") as file3:
            with open("./andre_solution.csv", "r") as file4:
                self.assertEqual(file3.read(), file4.read())


if __name__=="__main__":
    unittest.main()
