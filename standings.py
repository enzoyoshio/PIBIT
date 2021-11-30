def getStrRand():
	string = ""
	for i in range(6):
		string += str(randint(0, 9))
	return string

# importando libs
import json
import urllib.request
import requests
import hashlib
from random import randint, seed
import time
from datetime import datetime
import calendar
import json2csv
seed()

# inicializando variaveis
key = input("Insira a API Key: ")								# cada um usa sua propria key e secret
secret = input("Insira a API Secret: ") 							
cfId = input("Insira o Id do contest (eh o numero que se encontra na url): ") 			# para o exemplo o Id eh 351460
tempo = calendar.timegm(datetime.utcnow().utctimetuple()) 
stringRand = getStrRand()
stringHash =  f'contest.standings?apiKey={key}&contestId={cfId}&time={tempo}#{secret}'
allHash = stringRand + '/' + stringHash
string =  stringRand + hashlib.sha512(allHash.encode("utf-8")).hexdigest()

request = requests.get(f"https://codeforces.com/api/contest.standings", params = {
	"contestId": 		cfId,
	"apiKey":		key,
	"time":			tempo,
	"apiSig":		string
	})

# print(json.dumps(request.json(), sort_keys=True, indent=4))

json2csv.json2csv(request.json())
