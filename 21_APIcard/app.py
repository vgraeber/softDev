from urllib.request import urlopen
import json

api = "https://opentdb.com/api.php?amount=1&category=18"

def test():
    call = urlopen(api)
    data_json = json.loads(call.read())
    print (data_json)
    return data_json

test()