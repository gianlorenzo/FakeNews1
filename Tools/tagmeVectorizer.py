import tagme
import math
import unicodedata

# Authorization token
tagme.GCUBE_TOKEN = "8a0bd46c-6638-493f-bd49-82e9965473ff-843339462"

dirNand = "/home/gianlorenzo/PycharmProjects/FakeNews1/"
dirDav = "/home/davben/git/FakeNews1/"

def take_text_by_id_of_cleanedFile(user_id,dirX):
    dir = dirX+"TakeTweet/CleanedFile/"+str(user_id)+".txt"
    file = open(dir, "r+")
    user_text = file.read()
    return user_text

def get_annotation_of_cleanedFile(user_id,score,dirX):
    lunch_annotations = tagme.annotate(take_text_by_id_of_cleanedFile(user_id,dirX))
    # Print annotations with a score higher than 0.2
    dictionary = {}
    for ann in lunch_annotations.get_annotations(score):
        dictionary[ann.entity_title] = ann.score
    return dictionary

def writeFileCleanedAnnotation(user_id,score,dirX):
    dict = get_annotation_of_cleanedFile(user_id,score,dirX)
    print(len(dict))
    file = open(dirX+"Tools/CleanedAnnotation/"+str(user_id)+".txt","w+")
    i = 0
    while(i<len(dict)):
        file.write(unicodedata.normalize('NFKD',dict.keys()[i]).encode('ascii', 'ignore')+"="+repr(dict.values()[i])+"\n")
        i = i+1
    file.close()


def take_text_by_id_of_noCleanedFile(user_id,dirX):
    dir = dirX+"TakeTweet/NoCleanedFile/"+str(user_id)+".txt"
    file = open(dir, "r+")
    user_text = file.read()
    return user_text

def get_annotation_of_noCleanedFile(user_id,score,dirX):
    lunch_annotations = tagme.annotate(take_text_by_id_of_noCleanedFile(user_id,dirX))
    # Print annotations with a score higher than 0.2
    dictionary = {}
    for ann in lunch_annotations.get_annotations(score):
        dictionary[ann.entity_title] = ann.score
    return dictionary


def writeFileNoCleanedAnnotation(user_id,score,dirX):
    dict = get_annotation_of_noCleanedFile(user_id,score,dirX)
    print len(dict)
    file = open(dirX+"Tools/NoCleanedAnnotation/"+str(user_id)+".txt","w+")
    i = 0
    while(i<len(dict.keys())):
        file.write(unicodedata.normalize('NFKD',dict.keys()[i]).encode('ascii', 'ignore')+"="+repr(dict.values()[i])+"\n")
        i = i+1

    file.close()

def get_cosine_similarity1(dict1,dict2):
    intersection = set(dict1.keys()) & set(dict2.keys())
    numerator = sum([dict1[x]*dict2[x] for x in intersection])

    sum1 = sum([dict1[x]**2 for x in dict1.keys()])
    sum2 = sum([dict2[x]**2 for x in dict2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator



