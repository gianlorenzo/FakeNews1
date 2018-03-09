from DbConnection import DbConnection
import unicodedata
idUsers = DbConnection.takeUsersId()


def writeFile():
   for id in idUsers:
       i = 0
       file = open(str(id)+".txt","w+")
       tweet = DbConnection.takeText(id)
       while(i<len(tweet)):
           text = tweet[i]['Tweet']['text']
           newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
           file.write(newText+"\n")
           i=i+1
       file.close()



writeFile()






