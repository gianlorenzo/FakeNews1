import pandas
import tagme
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics import jaccard_similarity_score
from DbConnection import DbConnection

from Tools import tfIdfVectorizer, tagmeVectorizer

tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"

rels = tagme.relatedness_title([("Barack_Obama", "Italy"),
                                ("Italy", "Germany"),
                                ("New York", "America")])

#print(rels.relatedness[2])
dirDav = "/home/davben/git/FakeNews1/"
def get_annotation_of_cleanedFile(user_id,score):
    lunch_annotations = tagme.annotate(tfIdfVectorizer.take_text_by_file(user_id))
    # Print annotations with a score higher than 0.2
    dictionary = {}
    for ann in lunch_annotations.get_annotations(score):
        dictionary[ann.entity_title] = ann.score
    return dictionary

def creaFileAnnotati(listaUtenti):
    for i in listaUtenti:
        tagmeVectorizer.writeFileNoCleanedAnnotation(i,0.2,dirDav)

#creaFileAnnotati(DbConnection.takeUsersId()[:100])
#print(pandas.DataFrame(get_annotation_of_cleanedFile(12345,0.08).items()).sort_values([1]))

#(id,raws,min_df,max_df,ngram_range)
#x = (cVec_fitter_termOcc(73251704,100,1,0.7,(1,2)))
#x = cVec_fitter_termWeight(12345,100,1,0.7,(1,2))
#print((x))
