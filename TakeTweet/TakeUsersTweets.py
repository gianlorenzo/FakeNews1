from DbConnection import DbConnection
import time

from Tools import ElaboratoreTesto
import unicodedata

idUsers = DbConnection.takeUsersId()

def writeFile():
   start = time.time()
   for id in idUsers:
       i = 0
       file = open(str(id)+".txt","w+")
       tweet = DbConnection.takeText(id)
       while(i<len(tweet)):
           text = tweet[i]['Tweet']['text']
           newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
           testoRipulito = ElaboratoreTesto.pulisci(newText)
           file.write(testoRipulito+"\n")
           i=i+1
       file.close()
   end = time.time()
   print(end - start)


writeFile()






