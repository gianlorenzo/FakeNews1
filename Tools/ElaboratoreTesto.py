#pip install nltk

from nltk.tokenize import RegexpTokenizer
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#restituisce una lista di parole ripulite
def pulisci(testo):
    tokens = tokenizer(testo)
    #print(tokens)
    stopped = stopper(tokens)
    #print(stopped)
    stemmed = stemmer(stopped)
    #print(stemmed)
    for(text += stemmed[i] for i in stemmed)
    return stemmed

t = "Modernation !!! === ?!?! ,,,:;  Wheat Really Isn't Wheats 1000 At All https://t.co/Duy524oRNp ..."
t2 = "https://t.co/4FK2CniCk3 : 819dfb7f-7d6b-4b70-847c-071eb489a53c"

def tokenizer(testo):
    #match solo parole di 3+ caratteri
    tokenizer = RegexpTokenizer('\w{3,}')
    #elimino i numeri e i links
    result = re.sub(r"\d+","",re.sub(r"http\S+", "", testo))
    return tokenizer.tokenize(result)

def stopper(testo):
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    #stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    result = [i.lower() for i in testo if i.lower() not in stop_words]
    return result

def stemmer(testo):
    porter = PorterStemmer()
    result = [porter.stem(i.lower()) for i in testo]
    return result
#print((type(stemmer(t))))

print(pulisci(t))




#stemmer di porter
#stemmer di krovetz
#POS tagging
#n-grams