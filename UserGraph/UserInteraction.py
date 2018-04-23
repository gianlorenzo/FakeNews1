from profilazioneUtente import UserProfiling
import pandas as pd

def entity2User(user1,user2):
    wordList1 = UserProfiling.getMostRecurrWords(user1)
    print(wordList1)
    wordList2 = UserProfiling.getMostRecurrWords(user2)
    print(wordList2)
    entityMatchList = wordListMatcher(wordList1,wordList2)
    print(entityMatchList)
    entity2user = pd.DataFrame({"UserA":user1,"UserB":user2,"Entities":entityMatchList})
    print(entity2user)
    print(entity2user["UserA"].loc[0])
    return entity2user




def wordListMatcher(list1,list2):
    result=[]
    for i in list1:
        if i in list2:
            if i not in result:
                result.append(i)
    return result