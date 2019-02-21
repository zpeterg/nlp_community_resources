import unittest
from parsePhrase import parsePhrase, prepPhrase

phrase = 'I would like to hear about help with house rent in the Siloam area'
phrase2 = 'I would like to hear about help with house rent in the Siloam Springs area'


class TestParsePhrase(unittest.TestCase):
    def test_prep_phrase(self):
        res = ('would', 'like', 'hear', 'help', 'house', 'rent', 'siloam', 'area')
        self.assertEqual(res, prepPhrase(phrase))

    def test_parse_phrase(self):
        arr = ['housing assistance', 'Siloam Springs']
        res = {'count': 2, 'similarity': 3, 'lastCount': 1, 'lastSimilarity': 1}
        self.assertEqual(res, parsePhrase(arr, phrase))

    def test_parse_phrase_that_is_more_similar(self):
        arr = ['housing assistance', 'Siloam Springs']
        res = {'count': 2, 'similarity': 4, 'lastCount': 1, 'lastSimilarity': 2}
        self.assertEqual(res, parsePhrase(arr, phrase2))
