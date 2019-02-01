from fragIt import fragIt
from cleanIt import cleanIt
from synomize import synomize
from similarity import similarity


def prepPhrase(phrase):
    return cleanIt(fragIt(phrase))

def parsePhrase(arr, phrase):
    rtn = {'count': 0, 'similarity': 0}
    synomizedPhrase = synomize(prepPhrase(phrase))
    # prep each piece of comparison array
    for x in arr:
        preppedArr = prepPhrase(x)
        sim = similarity(preppedArr, synomizedPhrase)
        # get count of matching phrases
        rtn['similarity'] += sim
        # get total similarity (can match multiple parts of each phrase in 'arr'
        if sim > 0:
            rtn['count'] += 1
    return rtn
