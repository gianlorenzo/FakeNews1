from DbConnection import DbConnection
import unicodedata
import time

from Tools import ElaboratoreTesto

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
           file.write(newText+"\n")
           i=i+1
       file.close()
   end = time.time()
   print(end - start)

def writeFile1():
   start = time.time()
   for id in idUsers[0:1]:
       i = 0
       text1 = ""
       file = open(str(id)+".txt","w+")
       tweet = DbConnection.takeText(id)
       while(i < 1):
           text = tweet[i]['Tweet']['text']
           testoRipulito = (ElaboratoreTesto.pulisci(text)
           newText = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
           file.write(newText+"\n")
           i=i+1
       file.close()
   end = time.time()
   print(end - start)


writeFile1()






