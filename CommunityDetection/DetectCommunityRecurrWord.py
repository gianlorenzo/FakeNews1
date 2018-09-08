from DbConnection  import DbConnection as dc
from UserProfiling import UserProfiling as up
import pandas as pd
import string
import random

idUsers = dc.takeUsersId()

#il metodo scorre la colonna words della matrice:
#utente per utente si prendono le sue top words
#si scorre la lista di parole di ogni utente
#   se non e presente quella parola si appende alla lista:
#       si aggiunge quindi l id dell utente alla prima colonna e si scrive null alla seconda colonna
#   se e presente :
 #   si vede se c e un posto libero, se si si riempie il posto con l id dell utente e si forma una coppia
 #  se non e prensente un posto libero allora gia esiste quella coppia con quella parola:
 #          si creano in coda 2 nuove coppie (utente che si sta scorrendo,primo utente della coppia gia esistente)
 #             (utenteche si sta scorrendo , secondo utente della coppia gia esistente)
# si continua a scorrere la matrice se esiste un altra coppia si procede come riga sopra

#metodo che mi restituisce tutte le locazioni di quella parola nel df
def findAllLocs(colonnaParole,word):
    locazioni = []
    i=0
    for x in colonnaParole:
        if(x == word):
            locazioni.append(i)
        i= i+1
    return locazioni

def twoUsers2Word():
    df = pd.DataFrame(columns=["UserA","UserB","Word"])
    for id in idUsers[0:10]:
        wordList = up.getMostRecurrWords(id)[0:10]
        print wordList
        for word in wordList:
            currentWords= df["Word"].values.tolist()
            #se la parola  non e gia nella colonna words la aggiungo e aggiungo un utente
            if word not in currentWords:
                df.loc[len(df)] = [str(id),None,str(word)]
            #se la parola e nella lista
            else:
                #loc = getLocByFrame(df["Word"],word)
                #se lo spazio non e vuoto mi prendo tutte le locazioni della parola
                #if(df["UserB"].iloc[loc] != None):
                listaLocazioni = findAllLocs(currentWords,word)
                    #se l ultima locazione ha gia userB allora creo ogni coppia per quell user e associo quella parola
                if(df["UserB"].iloc[listaLocazioni[-1]] != None):
                    for l in listaLocazioni:
                            #mi prendo l utenteA e l utente B situato in quella locazione
                        idUserALoc = df["UserA"].iloc[l]
                        idUserBLoc = df["UserB"].iloc[l]
                        df.loc[len(df)]=[str(idUserALoc),str(id),word]
                        df.loc[len(df)] = [str(idUserBLoc), str(id), word]
                    df.drop_duplicates()

                else :
                        #quindi l ultima locazione e da riempire perche era stato trovato per la prima volta una coppia di un solo utente
                    df["UserB"].iloc[listaLocazioni[-1]] = str(id)
        file = open("/home/gianlorenzo/Scrivania/prova.txt","w+")
        file.write(str(df))
        file.close()
    return file




def openCsv():
    file = open("/home/gianlorenzo/Scrivania/prova.csv","r")
    text = open("/home/gianlorenzo/Scrivania/prova1.txt","w+")
    for line in file.readlines()[1:]:
        text.write(str(line))
    file.close()

def id_generator(size=3, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def openTxt():
    text = open("/home/gianlorenzo/Scrivania/prova1.txt","r")
    lines = []
    id = []
    for line in text.readlines()[1:]:
        lines.append(line.split(",")[1:])
    queryCreate = open("/home/gianlorenzo/Scrivania/queryCreate.txt","w+")
    queryRel = open("/home/gianlorenzo/Scrivania/queryRel.txt", "w+")

    for i in range(0,len(lines)):
        y = id_generator()
        x = id_generator()
        if lines[i][1]=="":
            queryCreate.write("create("+str(y)+":User{id1U:"+str(lines[i][0])+"})"+"\n")
        else:
            queryCreate.write("create("+str(y)+":User{idU:"+str(lines[i][0])+"})"+"\n")
            queryCreate.write("create("+str(x)+":User{idU:"+str(lines[i][1])+"})"+"\n")
            queryRel.write("match("+str(y)+":User{idU:"+str(lines[i][0])+"}),("+str(x)+":User{idU:"+str(lines[i][1])+"})"+"\n")
            queryRel.write("create("+str(y)+")-[r:"+str(lines[i][2])+"]->("+str(x)+")"+"\n")
    queryCreate.close()
    queryRel.close()


openTxt()

#metodo che mi prende la posizione di un elemento in un series
def getLocByFrame(colonna,parola):
    serie = pd.Series(colonna)
    loc = serie[serie == parola]
    return loc.index[0]


def prova():
    df = pd.DataFrame(columns=["UserA", "UserB", "Word"])
    wordlist = ["a","b","c","d","a"]
    for word in wordlist:
        currentWords = df["Word"].values.tolist()
        #if word not in currentWords:
            #df.append({"UserA":"a","UserB":None,"Word":str(word)})
        df.loc[len(df)] = ["a","V",str(word)]
        myseries = pd.Series(df["Word"])
        loc = myseries[myseries == "c"]
    #return loc.index[0]
    #return str(df["UserB"].iloc[loc.index[0]])
    #return wordlist[0:len(wordlist)-1]
    return df.drop_duplicates()
#print(prova())
#print(twoUsers2Word())