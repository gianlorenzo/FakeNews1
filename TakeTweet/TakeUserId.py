from DbConnection import DbConnection

users = DbConnection.connectionDb()

def takeUsersId():
    id = []
    for user in users[:10000]:
        id.append(user['id_user'])
    id = list(set(id))
    idInt = [int(i) for i in id]

    idStr = str(idInt)

    return idStr




