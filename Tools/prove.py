import tagme
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer
tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"

rels = tagme.relatedness_title([("Barack_Obama", "Italy"),
                                ("Italy", "Germany"),
                                ("France", "Italy")])

#print(rels.relatedness[2])

lunch_annotations = tagme.annotate("via gaystarnew brief histori georg washington carver greatest bisexu black scientist time")
dictionary = {}
for ann in lunch_annotations.get_annotations(0.08):
    dictionary[ann.entity_title] = ann.score
print(dictionary.keys())

def stemmer(testo):
    #porter = PorterStemmer()
    #result = [porter.stem(i.lower()) for i in testo]
    snowball = SnowballStemmer("english")
    porter = PorterStemmer()
    result = porter.stem(testo)
    return result
x = " dgsfdg "
#print stemmer("via gaystarnew brief histori georg washington carver greatest bisexu black scientist time")
print(type(x))