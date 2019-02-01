import unittest
from similarity import similarity


class TestSynomize(unittest.TestCase):
    def test_similarity(self):
        arr = ['dozen', 'cat']
        synoArr = [
            {'cat', 'lion', 'tiger'},
            {'12', 'dozen'},
            {'anchovies', 'fish'},
        ]
        res = 2
        self.assertEqual(res, similarity(arr, synoArr))

