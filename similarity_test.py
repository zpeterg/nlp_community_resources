import unittest
from similarity import similarity


class TestSimilarity(unittest.TestCase):
    def test_similar(self):
        arr = ['dozen', 'cat']
        synoArr = [
            {'cat', 'lion', 'tiger'},
            {'12', 'dozen'},
            {'anchovies', 'fish'},
        ]
        res = 2
        self.assertEqual(res, similarity(arr, synoArr))
