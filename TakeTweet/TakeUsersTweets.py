from DbConnection import DbConnection
import unicodedata
from Tools import ElaboratoreTesto
import os

idUsers = DbConnection.takeUsersId()

dirNand = "/home/gianlorenzo/PycharmProjects/FakeNews1/TakeTweet/"
dirDav = "/home/davben/git/FakeNews1/TakeTweet/"

def writeFile():
    os.mkdir(dirNand+"NoCleanedFile")
    for id in idUsers[0:40]:
        i = 0
        file = open(dirNand+"NoCleanedFile/"+str(id)+".txt", "w+")
        tweet = DbConnection.takeText(id)
        while (i < len(tweet)):
            text = tweet[i]['Tweet']['text']
            newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
            file.write(newText + "\n")
            i = i + 1
        file.close()


def writeCleanFile():
    os.mkdir(dirNand + "CleanedFile")
    for id in idUsers[0:40]:
       i = 0
       file = open(dirNand+"CleanedFile/"+str(id)+".txt","w+")
       tweet = DbConnection.takeText(id)
       while(i < len(tweet)):
           text = tweet[i]['Tweet']['text']
           newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
           finalText = ElaboratoreTesto.pulisci(newText)
           file.write(finalText+"\n")
           i=i+1
       file.close()





writeCleanFile()
