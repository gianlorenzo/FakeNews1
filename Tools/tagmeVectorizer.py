import tagme
from sklearn.metrics import jaccard_similarity_score

# Authorization token
tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"
def take_text_dy_id(id):
    dir = "C:\\Users\\NandG\\PycharmProjects\\FakeNews\\TakeTweet\\"+str(id)+".txt"
    file = open(dir, "r+")
    testo_utente = file.read()
    return testo_utente

def get_annotation(user_id):
    lunch_annotations = tagme.annotate(take_text_dy_id(user_id))
    # Print annotations with a score higher than 0.2
    for ann in lunch_annotations.get_annotations(0.2):
        print(ann)

#def get_jaccard_similarity(user_id1,user_id2):
    #return jaccard_similarity_score(get_annotation(user_id1),get_jaccard_similarity(user_id2))

#print(get_jaccard_similarity(153692738,21032566))

print(get_annotation(153692738))



