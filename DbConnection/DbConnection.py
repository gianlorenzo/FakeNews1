from pymongo import MongoClient


def connectionDb():
    uri = "mongodb://127.0.0.1:27017"

    client = MongoClient(uri)
    database = client['FakeNews']
    collection = database['320_users']
    return collection

def takeUsersId():
    id_users = connectionDb().distinct("id_user")
    for i in id_users:
        idInt = [int(i) for i in id_users]
    return idInt

print(takeUsersId())


