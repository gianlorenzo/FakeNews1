#http://www.ultravioletanalytics.com/blog/tf-idf-basics-with-pandas-scikit-learn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd

#fitter in input prende
# 1. directory doc passandogli un id(da modificare),
# 2. numero dei termini ordinati per occorrenze(da modificare)
# 3.,4.,5. : http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

def take_text_by_file(id_user):
    dir = "/home/davben/git/FakeNews1/TakeTweet/"+str(id_user)+".txt"
    file = open(dir,"r+")
    testo_utente = file.read()
    return testo_utente

#cVec_fitter(153692738,20,1,.5,(1,2))
def cVec_fitter_termOcc(id,raws,min_df,max_df,ngram_range):
    testo_utente = take_text_by_file(id)
    cvec = CountVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range)
    cvec.fit((testo_utente.split()))
    cvec_counts = cvec.transform(testo_utente.split())
    term_occurr(cvec_counts, cvec,raws)

def term_occurr(cvec_counts,cvec,raws):
    occ = np.asarray(cvec_counts.sum(axis=0)).ravel().tolist()
    counts_df = pd.DataFrame({'term': cvec.get_feature_names(), 'occurrences': occ})
    print(counts_df.sort_values(by='occurrences', ascending=False).head(raws))

def cVec_fitter_termWeight(id,raws,min_df,max_df,ngram_range):
    testo_utente = take_text_by_file(id)
    cvec = CountVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range)
    cvec.fit((testo_utente.split()))
    cvec_counts = cvec.transform(testo_utente.split())
    term_weights(cvec_counts, cvec,raws)

def term_weights(cvec_counts, cvec,raws):
    transformer = TfidfTransformer()
    transformed_weights = transformer.fit_transform(cvec_counts)
    weights = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
    weights_df = pd.DataFrame({'term': cvec.get_feature_names(), 'weight': weights})
    print(weights_df.sort_values(by='weight', ascending=False).head(raws))



#(id,raws,min_df,max_df,ngram_range)
cVec_fitter_termOcc(153692738,20,1,0.7,(1,2))
cVec_fitter_termWeight(153692738,20,1,.5,(1,2))
