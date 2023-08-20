import unittest
from word_search import get_content, search

class TestGetContent(unittest.TestCase): 
    def test_default_file_retrieval_works(self):
        f_content = get_content("file.txt")
        expected = "A world of dew,\nAnd within every dewdrop\nA world of struggle."

        self.assertEqual(f_content, expected)

    def test_empty_file_retrieval_works(self):
        f_content = get_content("empty_file.txt")
        self.assertEqual(f_content, "")

class TestSearchWord(unittest.TestCase):
    def test_search_empty_word_not_found_in_other_word(self):
        result = search("", "made up string")
        self.assertFalse(result)

    def test_search_empty_word_on_empty_word(self):
        result = search("", "")
        self.assertFalse(result)

    def test_search_word_on_same_word(self):
        result = search("lindsay", "lindsay")
        self.assertTrue(result)

    def test_search_substring_of_word(self):
        result = search("linds", "lindsay")
        self.assertTrue(result)

    def test_search_word_on_substring_of_itself(self):
        result = search("lindsay", "linds")
        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()