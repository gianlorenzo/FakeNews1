from DbConnection import DbConnection

users = DbConnection.connectionDb()

def takeUsersId():
    id = []
    for user in users[:10000]:
        id.append(user['id_user'])
    id = list(set(id))

    return id

print(takeUsersId())
