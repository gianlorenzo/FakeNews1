from nltk.tokenize import RegexpTokenizer
import re
from nltk.stem.snowball import SnowballStemmer
import stopwords

#restituisce una lista di parole ripulite
def pulisci(testo):
    tokens = tokenizer(testo)
    stopped = stopper(tokens)
    stemmed = stemmer(stopped)
    return " ".join(stemmed)

def tokenizer(testo):
    #match solo parole di 3+ caratteri
    tokenizer = RegexpTokenizer('\w{3,}')
    #elimino i numeri e i links
    result = re.sub(r"\d+","",re.sub(r"http\S+", "", testo))
    return tokenizer.tokenize(result)

def stopper(testo):
    stop_words = set(stopwords.get_stopwords('english'))
    result = [i.lower() for i in testo if i.lower() not in stop_words]
    return result

def stemmer(testo):
    snowball = SnowballStemmer("english")
    result = [snowball.stem(i.lower()) for i in testo]
    return result




