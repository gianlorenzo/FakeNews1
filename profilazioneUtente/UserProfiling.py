import tagme
from sklearn.metrics import jaccard_similarity_score
from Tools import tfIdfVectorizer
# Authorization token
tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"


def getMostRecurrWords(id_user):
    matrix = tfIdfVectorizer.cVec_fitter_termOcc(id_user,None,None,None,None)['term']
    lun = (len(matrix))
    soglia = lun/100
    topX = matrix.head(soglia)
    return (topX)

print((getMostRecurrWords(17643749)))