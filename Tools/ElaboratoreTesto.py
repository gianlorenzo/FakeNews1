
from nltk.tokenize import RegexpTokenizer
import re
from nltk.stem.porter import PorterStemmer
import stopwords

t = "Modernation !!! === ?!?! ,,,:;  Wheat Really Isn't Wheats 1000 At All https://t.co/Duy524oRNp ..."


#restituisce una lista di parole ripulite
def pulisci(testo):
    tokens = tokenizer(testo)
    #print(tokens)
    stopped = stopper(tokens)
    #print(stopped)
    stemmed = stemmer(stopped)
    #print(stemmed)
    return " ".join(stemmed)

def tokenizer(testo):
    #match solo parole di 3+ caratteri
    tokenizer = RegexpTokenizer('\w{3,}')
    #elimino i numeri e i links
    result = re.sub(r"\d+","",re.sub(r"http\S+", "", testo))
    return tokenizer.tokenize(result)

def stopper(testo):
    stop_words = set(stopwords.get_stopwords('english'))
    #print(stop_words)
    #stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    result = [i.lower() for i in testo if i.lower() not in stop_words]
    return result

def stemmer(testo):
    porter = PorterStemmer()
    result = [porter.stem(i.lower()) for i in testo]
    return result
#print((type(stemmer(t))))




