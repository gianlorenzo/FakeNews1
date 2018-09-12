from scipy.spatial.tests.test_kdtree import two_trees_consistency

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
    return df.drop_duplicates().dropna().reset_index(drop=True).to_csv("/home/gianlorenzo/Scrivania/xxx.csv",index=False)



print twoUsers2Word()