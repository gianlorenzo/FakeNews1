import TakeUserId

def writeInFile():
    idUsers = TakeUserId.takeUsersId()
    f = open("idUsers","w+")
    for id in idUsers:
        f.write(id)
    f.close()

writeInFile()


