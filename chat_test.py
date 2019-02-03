import unittest
from chat import Chat

resources = [
    {
        "name": "fishes",
        "phrase": "It looks like you're looking for fishes.",
        "options": "What kind of fishes are you looking for?",
        "children": [
            {
                "name": "deep sea fishes",
                "phrase": "We have several fishes that swim deep.",
                "children": [
                    {
                        "name": "Anger Fish",
                        "info": [{"name": "It has a light"}],
                        "isLeaf": True
                    },
                    {
                        "name": "Sword Fish",
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
                'options': 'What kind of fishes are you looking for?'
            },
            {
                'subject': ('fishes', 'deep sea fishes'),
                'phrase': 'We have several fishes that swim deep.'
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Anger Fish'),
                'info': [{'name': 'It has a light'}],
                'isLeaf': True
            },
            {
                'subject': ('fishes', 'deep sea fishes', 'Sword Fish'),
                'info': [{'name': 'Unusual characteristics', 'value': 'sword'}],
                'isLeaf': True
            }
        ]
        thisChat = Chat(resources, ['foo'])
        thisChat.flatten()
        self.assertEqual(thisChat.flattened, res)

    def test_chat_match(self):
        searchStr = 'Anger'
        res = {
            'subject': ('fishes', 'deep sea fishes', 'Anger Fish'),
            'info': [{'name': 'It has a light'}],
            'isLeaf': True
        }
        thisChat = Chat(resources, ['fishes', 'deep sea fishes'])
        thisChat.flatten()
        self.assertEqual(thisChat.match(searchStr), res)
