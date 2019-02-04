from parsePhrase import parsePhrase

class Chat:
    def __init__(self, resources, subject):
        self.resources = resources
        self.flattened = []
        self.subject = subject
        self.flatten()

    def flatten(self):
        rtn = []

        def loop(level, parent_names):
            for item in level:
                subject = parent_names + (item['name'],)
                new_item = {
                    "subject": subject,
                }
                if 'keywords' in item:
                    new_item['keywords'] = item['keywords']
                if 'phrase' in item:
                    new_item['phrase'] = item['phrase']
                if 'options' in item:
                    new_item['options'] = item['options']
                if 'info' in item:
                    new_item['info'] = item['info']
                if 'isLeaf' in item:
                    new_item['isLeaf'] = item['isLeaf']
                # Add that item
                rtn.append(new_item)
                # Move into the children and loop them
                if 'children' in item:
                    loop(item['children'], subject)

        loop(self.resources, ())
        self.flattened = rtn

    def match(self, search_str):
        all_matching = []
        for item in self.flattened:
            # Merge subjects into strings, and look to see if the subject sought is in this item's subject
            if ''.join(self.subject) in ''.join(item['subject']):
                all_matching.append(item)

        # Return "none" if nothing matches
        # todo: add a backup here or elsewhere that tries to find other subjects that partially match with parsePhrase()
        if len(all_matching) == 0:
            return None
        # Only a single item matches (no children)
        if len(all_matching) == 1:
            return all_matching[0]

        highest_similarity = 0
        highest_similarity_item = all_matching[0]
        for item in all_matching:
            # parsePhrase() returns something like {'count': 2, 'similarity': 3}
            sim = parsePhrase(item['subject'], search_str)
            if highest_similarity < sim['count']:
                highest_similarity_item = item
                highest_similarity = sim['count']

        return highest_similarity_item
