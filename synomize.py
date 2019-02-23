from nltk.corpus import wordnet
from spellchecker import SpellChecker

spell = SpellChecker()


def spell_suggest(words):
    # find those words that may be misspelled
    rtn = ()
    for word in words:
        print(words)
        print('spell-checking ', word)
        cands = spell.candidates(word)
        print('done')
        # always include the original word
        rtn += (word,)
        # add each candidate word, if not already there
        for c in cands:
            if c not in rtn:
                rtn += (c,)
    return tuple(sorted(rtn))


def synomize(arr, no_spell=True):
    rtn = ()
    if not no_spell:
        arr = spell_suggest(arr)

    for word in arr:
        word_set = (word,)
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                # only add if not a duplicate
                if l.name() not in word_set:
                    word_set += (l.name(),)
        rtn += (tuple(sorted(word_set)),)
    return rtn

