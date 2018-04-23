from DbConnection import DbConnection
import unicodedata
from Tools import ElaboratoreTesto

idUsers = DbConnection.takeUsersId()

dirNand = "/home/gianlorenzo/PycharmProjects/FakeNews1/TakeTweet/"
dirDav = "/home/davben/git/FakeNews1/TakeTweet/"

def writeFile():
    for id in idUsers[0:40]:
        i = 0
        file = open(dirDav+"NoCleanedFile/"+str(id)+".txt", "w+")
        tweet = DbConnection.takeText(id)
        while (i < len(tweet)):
            text = tweet[i]['Tweet']['text']
            newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
            file.write(newText + "\n")
            i = i + 1
        file.close()


def writeCleanFile():
   for id in idUsers[0:40]:
       i = 0
       file = open(dirDav+"CleanedFile/"+str(id)+".txt","w+")
       tweet = DbConnection.takeText(id)
       while(i < len(tweet)):
           text = tweet[i]['Tweet']['text']
           newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
           finalText = ElaboratoreTesto.pulisci(newText)
           file.write(finalText+"\n")
           i=i+1
       file.close()

writeFile()





