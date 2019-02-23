from fragIt import fragIt
from cleanIt import cleanIt
from synomize import synomize
from similarity import similarity


def prepPhrase(phrase):
    return cleanIt(fragIt(phrase))

def parsePhrase(arr, phrase):
    rtn = {'count': 0, 'similarity': 0, 'lastCount': 0, 'lastSimilarity': 0, 'matching': ()}
    synomized_phrase = synomize(prepPhrase(phrase), True)
    last_count = 0
    last_similarity = 0
    # prep each piece of comparison array
    for x in arr:
        sim = similarity(x, synomized_phrase)
        # get count of matching phrases
        rtn['similarity'] += sim['count']
        last_similarity = sim['count']
        # get total similarity (can match multiple parts of each phrase in 'arr'
        if sim['count'] > 0:
            rtn['count'] += 1
            last_count = 1
            rtn['matching'] += sim['matching']
        else:
            last_count = 0
    rtn['lastCount'] = last_count
    rtn['lastSimilarity'] = last_similarity
    return rtn
