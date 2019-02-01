import unittest
from synomize import synomize


class TestSynomize(unittest.TestCase):
    def test_synomize(self):
        arr = ['fish', 'taste', 'like', 'dozen', 'cat']
        res = [
            {'Fish', 'Pisces', 'Pisces_the_Fishes', 'fish', 'angle'},
            {'try_out', 'preference', 'gustatory_modality', 'discernment', 'predilection', 'perceptiveness', 'smack',
             'tasting', 'sense_of_taste', 'taste_perception', 'appreciation', 'gustatory_perception', 'penchant',
             'taste_sensation', 'try', 'taste', 'mouthful', 'gustatory_sensation', 'savour', 'gustation', 'savor',
             'sample'},
            {'wish', 'the_likes_of', 'similar', 'comparable', 'corresponding', 'ilk', 'the_like', 'care', 'same',
             'like', 'alike'},
            {'dozen', 'xii', 'twelve', 'XII', '12'},
            {'qat', 'bozo', 'CT', 'disgorge', 'computed_axial_tomography', 'cat', 'CAT', 'barf', 'big_cat', 'cast',
             'computerized_tomography', 'sick', 'throw_up', "cat-o'-nine-tails", 'computed_tomography', 'upchuck',
             'Caterpillar', 'Arabian_tea', 'puke', 'kat', 'spew', 'African_tea', 'khat', 'chuck', 'purge', 'quat',
             'regorge', 'regurgitate', 'retch', 'be_sick', 'guy', 'honk', 'hombre', 'vomit', 'spue', 'vomit_up',
             'true_cat', 'computerized_axial_tomography'},
        ]
        self.assertEqual(res, synomize(arr))

