import tagme

def take_text_dy_id(id):
    dir = "C:\\Users\\NandG\\PycharmProjects\\FakeNews\\TakeTweet\\"+str(id)+".txt"
    file = open(dir, "r+")
    testo_utente = file.read()
    return testo_utente


