from nltk.corpus import wordnet


def synomize(arr):
    rtn = []
    for word in arr:
        wordSet = {word}
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                wordSet.add(l.name())
        rtn.append(wordSet)
    return rtn

