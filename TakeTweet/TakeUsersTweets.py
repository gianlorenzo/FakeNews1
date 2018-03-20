from DbConnection import DbConnection
import unicodedata
from Tools import ElaboratoreTesto

idUsers = DbConnection.takeUsersId()

def writeFile():
   for id in idUsers[0:2]:
       i = 0
       file = open(str(id)+".txt","w+")
       tweet = DbConnection.takeText(id)
       while(i < len(tweet)):
           text = tweet[i]['Tweet']['text']
           newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
           finalText = ElaboratoreTesto.pulisci(newText)
           file.write(finalText+"\n")
           i=i+1
       file.close()

writeFile()






