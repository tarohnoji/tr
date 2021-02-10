import pya3rt

def create_reply(user_text):
    apikey = "DZZaQUy1OTXJyfwe15vF4XQ8a2LiVUag"
    client = pya3rt.TalkClient(apikey)

    res = client.talk(user_text)
    return res['results'][0]['reply']

