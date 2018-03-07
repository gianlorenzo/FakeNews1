from DbConnection import DbConnection
import unicodedata
users = DbConnection.takeUsers()
idUsers = DbConnection.takeUsersId()


def provaId():
    for id in idUsers:
        for user in users[:5000]:
            if user['id_user'] == id:
                tweet = user['Tweet']
                textTweet = []
                textTweet.append(tweet['text'])
        file = open(str(id) + ".txt", "w+")
        for text in textTweet:
            newTweet = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
            file.write(newTweet+"\n")
    file.close()

provaId()