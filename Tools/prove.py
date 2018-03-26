import tagme
tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"

rels = tagme.relatedness_title([("Barack_Obama", "Italy"),
                                ("Italy", "Germany"),
                                ("France", "Italy")])

#print(rels.relatedness[2])

lunch_annotations = tagme.annotate("via")
dictionary = {}
for ann in lunch_annotations.get_annotations(0):
    dictionary[ann.entity_title] = ann.score
print(dictionary.keys())