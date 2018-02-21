from pymongo import MongoClient


def connectionDb():
    uri = "mongodb://127.0.0.1:27017"

    client = MongoClient(uri)
    database = client['FakeNews']
    collection = database['320_users']
    users = collection.find({})

    return users

