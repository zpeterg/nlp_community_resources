from nltk.corpus import wordnet
from spellchecker import SpellChecker

spell = SpellChecker()


def spell_suggest(words):
    # find those words that may be misspelled
    misspelled = spell.unknown(words)
    rtn = ()
    for word in words:
        cands = spell.candidates(word)
        rtn += tuple(cands)
    return rtn


###################### todo: working on adding spelling check below
def synomize(arr):
    rtn = []

    arr = spell_suggest(tuple(arr))
    arr = list(set(arr))

    for word in arr:
        wordSet = {word}
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                wordSet.add(l.name())
        rtn.append(wordSet)
    return rtn

