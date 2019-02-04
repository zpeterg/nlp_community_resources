import unittest
from chat import Chat

resources = [
    {
        "name": "fishes",
        "keywords": ["fish seafood animal"],
        "phrase": "It looks like you're looking for fishes.",
        "options": "What kind of fishes are you looking for?",
        "children": [
            {
                "name": "deep sea fishes",
                "keywords": ["deep bottom-dwellers"],
                "phrase": "We have several fishes that swim deep.",
                "children": [
                    {
                        "name": "Angler Fish",
                        "keywords": ["Angler Lophiiformes"],
                        "info": [{"name": "It has a light"}],
                        "isLeaf": True
                    },
                    {
                        "name": "Sword Fish",
                        "keywords": ["Sword Xiphias"],
                        "info": [{"name": "Unusual characteristics", "value": "sword"}],
                        "isLeaf": True
                    }
                ]
            }
        ]
    }
]

class TestChat(unittest.TestCase):
    def test_chat_constructor(self):
        resources = [{'name': 'foo'}]
        subject = ['bar']
        thisChat = Chat(resources, subject)
        self.assertEqual(resources, thisChat.resources)
        self.assertEqual([{'subject': ('foo',)}], thisChat.flattened)
        self.assertEqual(subject, thisChat.subject)

    def test_chat_flatten(self):

        res = [
            {
                'subject': ('fishes',), 'phrase': "It looks like you're looking for fishes.",
                "keywords": ["fish seafood animal"],
                'options': 'What kind of fishes are you looking for?'
            },
            {
                'subject': ('fishes', 'deep sea fishes'),
                "keywords": ["deep bottom-dwellers"],
                'phrase': 'We have several fishes that swim deep.'
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Angler Fish'),
                "keywords": ["Angler Lophiiformes"],
                'info': [{'name': 'It has a light'}],
                'isLeaf': True
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Sword Fish'),
                "keywords": ["Sword Xiphias"],
                'info': [{'name': 'Unusual characteristics', 'value': 'sword'}],
                'isLeaf': True
            }
        ]
        thisChat = Chat(resources, ['foo'])
        thisChat.flatten()
        self.assertEqual(thisChat.flattened, res)

    def test_chat_match(self):
        searchStr = 'Angler'
        res = {
            'subject': ('fishes', 'deep sea fishes', 'Angler Fish'),
            "keywords": ["Angler Lophiiformes"],
            'info': [{'name': 'It has a light'}],
            'isLeaf': True
        }
        thisChat = Chat(resources, ['fishes', 'deep sea fishes'])
        thisChat.flatten()
        self.assertEqual(thisChat.match(searchStr), res)
