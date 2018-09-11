from CommunityDetection import CommunityDetect as cd
import pandas as pd
from DbConnection import DbConnection as dbc

idUsers = dbc.takeUsersId()

dirFileDav = "/home/gianlorenzo/Scrivania/users3.csv"

dirFile = dirFileDav

def getUsersLabeledByFile(dirFile):
    dfUsr = pd.DataFrame.from_csv(dirFile,index_col=None)
    return dfUsr.ix[:,:]

def getListofUsers(dirFile):
    df = getUsersLabeledByFile(dirFile)
    users = df.ix[:,0]
    return users

def recuperaDf320Labeled(dirFile):
    usersList = getListofUsers(dirFile)
    index320 = []
    for id in idUsers:
        print "recuperando gli index dei labeled ..."
        i = 0
        for user in usersList:
            if(id == user):
                index320.append(i)
            i=i+1
    return index320


#ho creato la matrice che prende i nostri 320 users e li ricerca in users.csv
#escono fuori 50 users etichettati
#il dottorando aveva etichettato  250000 users, ma soltato 50 dei 320 che ci ha dato sono presenti nel csv
def getDf320():
    df = getUsersLabeledByFile(dirFile)
    index320 = recuperaDf320Labeled(dirFile)
    df320Labeled = pd.DataFrame(columns=["userId","label"])
    for i in index320:
        df320Labeled.loc[len(df320Labeled)]=[df.iloc[i][0],df.iloc[i][1]]
    return df320Labeled




#print recuperaDf320Labeled(dirFile)

#print((getListofUsers(dirFile)))

#print len(getUsersLabeledByFile(dirFile))

#print getDf320()