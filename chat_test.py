import unittest
from chat import match_to_list, Chat

resources = [
    {
        "name": "fishes",
        "keywords": ("fish seafood animal",),
        "phrase": "It looks like you're looking for fishes.",
        "options": "What kind of fishes are you looking for?",
        "children": (
            {
                "name": "deep sea fishes",
                "keywords": ("deep bottom-dwellers",),
                "phrase": "We have several fishes that swim deep.",
                "children": [
                    {
                        "name": "Angler Fish",
                        "keywords": ("Angler Lophiiformes",),
                        "info": ({"name": "It has a light"},),
                        "isLeaf": True
                    },
                    {
                        "name": "Sword Fish",
                        "keywords": ("Sword Xiphias",),
                        "info": ({"name": "Unusual characteristics", "value": "sword"},),
                        "isLeaf": True
                    }
                ]
            },
        )
    },
    {
        "name": "eels",
        "keywords": ("eel snake-like",),
        "phrase": "Are you looking for eels?",
        "options": "What kind of eels are you looking for?",
        "children": (
            {
                "name": "Synder's Moray",
                "keywords": ("Synder's finespot Moray",),
                "info": ({"name": "It was discovered in 1904"},),
                "isLeaf": True
            },
            {
                "name": "Zebra Moray",
                "keywords": ("Zebra striped Moray",),
                "info": ({"name": "Diet", "value": "Sea urchins, mollusks, and crustaceans."},),
                "isLeaf": True
            },
        )
    }
]


class TestChat(unittest.TestCase):
    def test_match_to_list(self):
        tup = (
            {'keywords': ('fish seafood animal',)},
            {'keywords': ('fish seafood animal', 'deep bottom-dwellers')},
            {'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Angler Lophiiformes')},
            {'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Sword Xiphias')},
        )
        res = {
            'count': 2,
            'similarity': 2,
            'value': tup[1],
        }
        phrase = 'fishs that swim down deep'
        returned = match_to_list(tup, phrase)
        self.assertEqual(returned, res)

    def test_chat_constructor(self):
        resources = [{'name': 'foo', 'keywords': ('foo man',)}]
        subject = ['bar']
        thisChat = Chat(resources, subject)
        self.assertEqual(resources, thisChat.resources)
        self.assertEqual([{'subject': ('foo',), 'keywords': ('foo man',)}], thisChat.flattened)
        self.assertEqual(subject, thisChat.subject)

    def test_chat_flatten(self):

        res = [
            {'subject': ('fishes',), 'keywords': ('fish seafood animal',), 'phrase': "It looks like you're looking for fishes.", 'options': 'What kind of fishes are you looking for?'},
            {'subject': ('fishes', 'deep sea fishes'), 'keywords': ('fish seafood animal', 'deep bottom-dwellers'), 'phrase': 'We have several fishes that swim deep.'},
            {'subject': ('fishes', 'deep sea fishes', 'Angler Fish'), 'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Angler Lophiiformes'), 'info': ({'name': 'It has a light'},), 'isLeaf': True},
            {'subject': ('fishes', 'deep sea fishes', 'Sword Fish'), 'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Sword Xiphias'), 'info': ({'name': 'Unusual characteristics', 'value': 'sword'},), 'isLeaf': True},
            {'subject': ('eels',), 'keywords': ('eel snake-like',), 'phrase': 'Are you looking for eels?', 'options': 'What kind of eels are you looking for?'},
            {'subject': ('eels', "Synder's Moray"), 'keywords': ('eel snake-like', "Synder's finespot Moray"), 'info': ({'name': 'It was discovered in 1904'},), 'isLeaf': True},
            {'subject': ('eels', 'Zebra Moray'), 'keywords': ('eel snake-like', 'Zebra striped Moray'), 'info': ({'name': 'Diet', 'value': 'Sea urchins, mollusks, and crustaceans.'},), 'isLeaf': True},
        ]
        thisChat = Chat(resources, ['foo'])
        thisChat.flatten()
        self.assertEqual(thisChat.flattened, res)

    def test_chat_match(self):
        searchStr = 'Angler'
        res = {
            'count': 1,
            'similarity': 1,
            'value': {'subject': ('fishes', 'deep sea fishes', 'Angler Fish'), 'keywords': ('fish seafood animal', 'deep bottom-dwellers', 'Angler Lophiiformes'), 'info': ({'name': 'It has a light'},), 'isLeaf': True},
            'certainty': 2
        }
        thisChat = Chat(resources, ['fishes', 'deep sea fishes'])
        thisChat.flatten()
        self.assertEqual(thisChat.match(searchStr), res)

    def test_chat_match_alternative(self):
        searchStr = 'Zebra'
        res = {
            'count': 1, 'similarity': 1, 'value': {'subject': ('eels', 'Zebra Moray'), 'keywords': ('eel snake-like', 'Zebra striped Moray'), 'info': ({'name': 'Diet', 'value': 'Sea urchins, mollusks, and crustaceans.'},), 'isLeaf': True},
            'certainty': 0
        }

        thisChat = Chat(resources, ['fishes', 'nothingthere'])
        thisChat.flatten()
        self.assertEqual(thisChat.match(searchStr), res)
