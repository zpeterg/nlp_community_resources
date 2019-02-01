from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

ps = PorterStemmer()

def cleanIt(arr):
    rtn = []
    for word in arr:
        # clean up the word
        word = word.strip().lower()
        # Add it to the list if it's not a 'stop word'
        if word not in stopwords.words('english'):
            rtn.append(format(wordnet_lemmatizer.lemmatize(word, pos="v")))
    return rtn

