from pymongo import MongoClient
import json, ast

def connectionDb():
    uri = "mongodb://127.0.0.1:27017"

    client = MongoClient(uri)
    database = client['FakeNews']
    collection = database['320_users']
    return collection

#Restituisce tutte le tuple
#def takeUsers():
 #   return connectionDb().find({})

#Restituisce i 321 id
def takeUsersId():
   return connectionDb().distinct("id_user")

def takeText(id):
    text = connectionDb().find({'id_user': id}, {"Tweet.text": 1})
    return list(text)






