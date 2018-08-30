import tagme
from sklearn.metrics import jaccard_similarity_score
from Tools import tfIdfVectorizer, tagmeVectorizer

# Authorization token
tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"
dirNand = "/home/gianlorenzo/PycharmProjects/FakeNews1/"
dirDav = "/home/davben/git/FakeNews1/"

#prende le parole piu significative
def getMostRecurrWords(id_user):
    matrix = tfIdfVectorizer.cVec_fitter_termOcc(id_user,None,None,None,None)['term']
    lun = (len(matrix))
    soglia = lun/100
    topX = matrix.head(soglia)
    return (list(topX))
#x = getMostRecurrWords(17643749)
#print((getMostRecurrWords(17643749)))

#trasforma una lista di parole in una dizionario parola:peso
def getEntities(wordList):
    dictionary={}
    annotationsText = (" ").join(wordList)
    print((str(annotationsText)))
    annotation = tagme.annotate((annotationsText))
    for ann in annotation.get_annotations(0.08):
        dictionary[ann.entity_title] = ann.score
    return dictionary

#restituisce un dizionario delle entita raccolte da tweet non ripuliti
def getEntitiesNoCleaned(id,score,dir):
    dict = tagmeVectorizer.get_annotation_of_noCleanedFile(id,score,dir)
    return dict

#x = getEntitiesNoCleaned(17643749,0.2,dirDav).keys()
#print(getEntities(x))

