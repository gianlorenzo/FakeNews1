from CommunityDetection import UsersRecurrWord as urw
import collections


#metodo che trova i primi due utenti compatibili
def primaCompatibilita(df,id1,id2):
    primaComunita = []
    df = df.drop(index = 0).reset_index(drop = True)
    i = 0
    dropper = 0
    comunita = 1
    # mi metto da parte le colonne del df in entrata
    primaColonna = df.ix[:, 0].values.tolist()
    secondaColonna = df.ix[:, 1].values.tolist()

    for x1 in primaColonna:
        # se il prossimo elemento e id1 e il compagno e  id2 allora ho trovato un nuovo concetto in comune
        if (id1 == x1 and id2 == secondaColonna[i]):
            comunita = comunita + 1
            #aggiorno il df rimuovendo le coppie gia analizzate
            df = df.drop(index = dropper).reset_index(drop = True)
            #il reset dell index mi costringe a sottrarre una unita
            dropper=dropper-1
        i = i + 1
        dropper = dropper +1
    if (comunita > 2):
        primaComunita.append(id1)
        primaComunita.append(id2)
    #print comunita
    return primaComunita,df



def createFirstCommunity(df):
    listaComunita = []
    #mi creo la prima comunita data dalla prima coppia
    while len(listaComunita) < 1 and len(df)>0:
        primaC,df = primaCompatibilita(df,df.ix[0,0],df.ix[0,1])
        #primaC = primaCompatibilita(df,df.ix[0,0],df.ix[0,1])[0]
        if(len(primaC)>0):
            listaComunita.append(primaC)
    return df,listaComunita

#metodo che restituisce una lista di coppie di utenti che hanno buona compatibilita
def createUsersCompatibilityList():
    df = urw.twoUsers2Word().dropna().reset_index(drop=True)
    listaComunita = []
    # mi creo la prima comunita data dalla prima coppia
    while len(df) > 0:
        #gli viene passata la prima coppia di utenti del dataframe rimanente
        comunita, df = primaCompatibilita(df, df.ix[0, 0], df.ix[0, 1])
        #ogni volta la lista comunita aumenta e il dataframe si svuota, verra aggiunta una comunita se
        #il metodo prima compatibilita restituisce una lista non vuota
        #ovvero nella lista e stata aggiunta una coppia compatibile

        # primaC = primaCompatibilita(df,df.ix[0,0],df.ix[0,1])[0]
        if (len(comunita) > 0):
            listaComunita.append(comunita)
    return listaComunita

def createCommunity():
    usrCompList = createUsersCompatibilityList()
    print usrCompList
    communityList = []
    #lista di coppie da rimuovere
    removeList = []
    for c1 in usrCompList:
        #print c1
        for c2 in usrCompList:
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
                            for c3 in usrCompList:
                                if (collections.Counter(newMatch) == collections.Counter(c3)):
                                    #riempio la removing list
                                    #mi servira poi per rimuovere le coppie che hanno formato una nuova comunita
                                    removeList.append(newMatch)
                                    removeList.append(c1)
                                    removeList.append(c2)
                                    newMatch.append(elem1)
                                    communityList.append(newMatch)



                #print "fine del primo elem"
    #print communityList
    finalCommListOrd = []
    finalCommList=[]
    #sarebbe la lista che si riempira tolte le nuove coppie dalla vecchia lista
    commlistCleaned = []
    for i1 in communityList:
        finalCommListOrd.append(sorted(i1))
    #tolgo i duplicati ordinati diversamente
    for i2 in finalCommListOrd:
        if i2 not in finalCommList:
            finalCommList.append(i2)
    for i3 in usrCompList:
        if i3 not in removeList:
            commlistCleaned.append(i3)
    #rimetto insieme la lista di partenza e quella nuova con le comunita
    communities = finalCommList+commlistCleaned
    return (communities)



#print(createCommunity())




