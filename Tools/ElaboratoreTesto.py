from nltk import *
import re

from nltk.corpus import stopwords
import stopwords

#restituisce una lista di parole ripulite
def pulisci(testo):
    tokens = tokenizer(testo)
    #print(tokens)
    stopped = stopper(tokens)
    #print(stopped)
    stemmed = stemmer(stopped)
    #print(stemmed)
    return " ".join(stemmed)

t = "Modernation !!! === ?!?! ,,,:;  Wheat Really Isn't Wheats 1000 At All https://t.co/Duy524oRNp ..."
t2 = "https://t.co/4FK2CniCk3 : 819dfb7f-7d6b-4b70-847c-071eb489a53c"

def tokenizer(text):
    #match solo parole di 3+ caratteri
    tokenizer = RegexpTokenizer('\w{3,}')
    #elimino i numeri e i links
    result = re.sub(r"\d+","",re.sub(r"http\S+", "", text))
    return tokenizer.tokenize(result)

def stopper(text):
    stop_words = set(stopwords.get_stopwords('english'))
    print(stop_words)
    result = [i.lower() for i in text if i.lower() not in stop_words]
    return result

def stemmer(text):
    porter = PorterStemmer()
    result = [porter.stem(i.lower()) for i in text]
    return result

