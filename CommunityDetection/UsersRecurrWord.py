from DbConnection  import DbConnection as dc
from UserProfiling import UserProfiling as up
import pandas as pd
import collections
import random
import string

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
        wordList = up.getMostRecurrWords(id)[0:30]
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
    return df.drop_duplicates().dropna().reset_index(drop=True)#.to_csv("/home/bigbrothers/Scrivania/xxx.csv",index=False)

#print(twoUsers2Word())


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
    #for i in range(3):
    #    df = df.drop(index = i)
    #return loc.index[0]
    #return str(df["UserB"].iloc[loc.index[0]])
    #return wordlist[0:len(wordlist)-1]
    #return df.reset_index().ix[0,1]
#print(prova().ix[:,2].values.tolist())
    lista1 = ["ciao","scopi","rimorchi"]
    lista2 = ["scopi","rimorchi","ciao"]

    i = 5#genera id random alfanumerici di lunghezza 3
def id_generator(size=3, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def openCsv():
    file = open("/home/gianlorenzo/Scrivania/prova.csv","r")
    text = open("/home/gianlorenzo/Scrivania/prova1.txt","w+")
    for line in file.readlines()[1:]:
        text.write(str(line))
    file.close()

def createNeo4jQueries():
    text = open("/home/gianlorenzo/Scrivania/prova1.txt","r")
    lines = []
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
    while i:
        print i
        i=i+1
    return
#(prova())
def chechUguali():
    lista1 = ["ciao", "scopi", "rimorch"]
    lista2 = ["scopi", "rimorchi", "ciao","scopi"]
    lista3 = ['153692738', '153692738', '153692738', '73251704']
    lista4=[]
    matc = lista1+lista2
    for i in lista3:
        if(i !='153692738'):
            lista4.append(i)
    #if(collections.Counter(lista1) == collections.Counter(lista2)):
    #    return "si"
    return lista4
#print(chechUguali())

def createCommunity():
    lista3 = [['153692738', '21032566'], ['153692738', '73251704'], ['21032566', '312149882'],
              ['73251704', '562346664'], ['312149882', '437642826'], ['312149882', '17643749'],
              ['153692738', '312149882'], ['312149882', '1933259448'], ['312149882', '3374126201'],
              ['437642826', '562346664'], ['153692738', '437642826'], ['21032566', '437642826'],
              ['437642826', '3374126201'], ['437642826', '1933259448'], ['437642826', '17643749'],
              ['21032566', '17643749'], ['153692738', '17643749'], ['17643749', '1933259448'],
              ['153692738', '1933259448'], ['21032566', '1933259448'], ['1933259448', '3374126201'],
              ['21032566', '562346664'], ['312149882', '562346664'], ['17643749', '562346664'],
              ['1933259448', '562346664'], ['153692738', '562346664'], ['17643749', '3374126201'],
              ['562346664', '3374126201'], ['21032566', '3374126201'], ['153692738', '3374126201']]

    lista6 =  [['A', 'B'], ['A', 'C'], ['B', 'D'],
              ['C', 'E'], ['D', 'F'], ['D', 'G'],
              ['A', 'D'], ['D', 'H'], ['D', 'I'],['F','B']]

    communityList = []
    for c1 in lista6:
        #print c1
        for c2 in lista6:
            #print c2
        # se non sto guardando la stessa coppia
            if not (collections.Counter(c1) == collections.Counter(c2)):
                for elem1 in c1:
                    #print elem1
                    for elem2 in c2:
                        if elem1 == elem2:
                            matcList = c1 + c2
                            #print matcList
                            newMatch = []
                            for elemToRm in matcList:
                                if not (elemToRm == elem1):
                                    newMatch.append(elemToRm)
                            #print newMatch
                            #print "------------------------------------"
                            for c3 in lista6:
                                if (collections.Counter(newMatch) == collections.Counter(c3)):

                                    newMatch.append(elem1)
                                    communityList.append(newMatch)


                #print "fine del primo elem"
        return communityList

print(createCommunity())

#genera id random alfanumerici di lunghezza 3
def id_generator(size=3, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def openCsv():
    file = open("/home/gianlorenzo/Scrivania/prova.csv","r")
    text = open("/home/gianlorenzo/Scrivania/prova1.txt","w+")
    for line in file.readlines()[1:]:
        text.write(str(line))
    file.close()

def createNeo4jQueries():
    text = open("/home/gianlorenzo/Scrivania/prova1.txt","r")
    lines = []
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

