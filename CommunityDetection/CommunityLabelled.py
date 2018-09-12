from CommunityDetection import FakeLabeling as fl
from CommunityDetection import CommunityDetect as cd
import pandas as pd

#mi scorro la lista delle comunita, per ciascuna comunita verifico se l utente lo posso trovare nella matrice dei labeled
#se lo trovo ricreo la comunita aggiungendolo con l etichetta [comunitylist[coommunity1[[id,label],community2[..,..,..],..,],..]
#altrimenti lo ricreo mettendo l'etichetta uknown
def communityLabelling():
    communityList = cd.createCommunity()
    df = fl.getDf320()
    users51= df.ix[:,0].values.tolist()
    newcCommList=[]
    for comm in communityList:
        newComm = []
        for user in comm:
            newUser=[]
            if (int(user) in users51):
                series = pd.Series(df["userId"])
                loc = series[series == int(user)]
                userRecord = df.iloc[loc.index[0]]
                newUser.append(userRecord[0])
                newUser.append(userRecord[1])
            else:
                newUser.append(user)
                newUser.append('uknown')
            newComm.append(newUser)
        newcCommList.append(newComm)
    community = open("/home/gianlorenzo/Scrivania/community.txt","w+")
    community.write(str((newcCommList)))
    community.close()
    return community






