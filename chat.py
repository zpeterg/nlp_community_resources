from parsePhrase import parsePhrase

def match_to_list(tup, search_str):
    highest_similarity = {'similarity': 0, 'count': 0, 'lastCount': 0, 'lastSimilarity': 0}
    highest_similarity_item = tup[0]
    for item in tup:
        # parsePhrase() returns something like {'count': 2, 'similarity': 3, 'lastCount': 0, 'lastSimilarity': 0}
        sim = parsePhrase(item['keywords'], search_str)
        # only count as highest similarity if has highest match, AND matches on the last item
        if highest_similarity['count'] < sim['count'] and sim['lastCount'] > 0:
            highest_similarity_item = item
            highest_similarity = sim
    return {
        'count': highest_similarity['count'],
        'similarity': highest_similarity['similarity'],
        'value': highest_similarity_item,
        'lastCount': highest_similarity['lastCount'],
        'lastSimilarity': highest_similarity['lastSimilarity'],
    }


class Chat:
    def __init__(self, resources, subject, language=0):
        self.resources = resources
        self.flattened = []
        self.subject = subject
        self.language = language
        self.flatten()

    def flatten(self):
        rtn = []

        def loop(level, parent_names, parent_keywords):
            for item in level:
                subject = parent_names + (item['name'],)
                keywords = parent_keywords + (item['keywords'][self.language],)
                new_item = {
                    "subject": subject,
                    "keywords": keywords,
                }
                if 'phrase' in item:
                    new_item['phrase'] = item['phrase']
                if 'options' in item:
                    new_item['options'] = item['options']
                if 'info' in item:
                    new_item['info'] = item['info']
                if 'isLeaf' in item:
                    new_item['isLeaf'] = item['isLeaf']
                if 'children' in item:
                    children = ()
                    for c in item['children']:
                        children += (c['phrase'][self.language],)
                    new_item['children'] = children
                # Add that item
                rtn.append(new_item)
                # Move into the children and loop them
                if 'children' in item:
                    loop(item['children'], subject, keywords)

        loop(self.resources, (), ())
        self.flattened = rtn


    def match(self, search_str):
        all_matching = []
        most_sim = None
        # certainty is 0-2
        certainty = 2
        for item in self.flattened:
            # Merge subjects into strings, and look to see if the subject sought is in this item's subject
            if ''.join(self.subject) in ''.join(item['subject']):
                all_matching.append(item)

        # Return "none" if nothing matches
        if len(all_matching) == 0:
            certainty = 0
        else:
            # Match to items that share subject (sub-tree)
            most_sim = match_to_list(all_matching, search_str)

        # if nothing matches, look everywhere
        if not most_sim or most_sim['count'] <= 0:
            most_sim = match_to_list(self.flattened, search_str)

        # Adjust certainty on match count
        if (most_sim['count'] < 1):
            certainty = 0
        else:
            certainty = 1

        if most_sim:
            most_sim['certainty'] = certainty
        return most_sim
