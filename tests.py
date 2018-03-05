import unittest
import search

class SearchTest(unittest.TestCase):

    def test_must_find_the_content(self):
        content_to_find = "walt disney"
        search_result = search.search_content(content_to_find)
        self.assertTrue(len(search_result) == 53)

if __name__ == '__main__':
    unittest.main()
