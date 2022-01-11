"""
ideias de como parsear:

1. escrever algo na descrição 	(talvez criar uma hash? contra: nao pode esquecer de adicionar a descrição no contest XD)
2. parsear pelo nome do contest (contra: todos os contests do grupo deveriam ter pelo menos uma palavra em comum)
3. Autor 			(contra: apenas uma pessoa pode preparar os contests)
4. school/city/country 		(contra: usar tres filtros para parsear de forma "otima")
5. websiteUrl 			(poderia usar o site do cic? contra: mesmo do numero 1)

"""
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

def getUserContests(key, secret, gym):

	tempo = calendar.timegm(datetime.utcnow().utctimetuple()) 
	stringRand = getStrRand()
	stringHash =  f'contest.list?apiKey={key}&gym={gym}&time={tempo}#{secret}'
	allHash = stringRand + '/' + stringHash
	string =  stringRand + hashlib.sha512(allHash.encode("utf-8")).hexdigest()

	request = requests.get(f"https://codeforces.com/api/contest.list", params = {
		"gym": 		gym,
		"apiKey":		key,
		"time":			tempo,
		"apiSig":		string
		})
	
	# print(json.dumps(request.json(), sort_keys=True, indent=4))
	return request.json()	

def getFilteredContests(key, secret, gym, field):
	allContests = getUserContests(key, secret, gym)
	res = allContests["result"]
	
	for con in res:
		print(con, "\n\n")

def getStandings(key, secret, cfId):
	seed()

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

	print(json.dumps(request.json(), sort_keys=True, indent=4))

	json2csv.json2csv(request.json())


with open("senhas.txt", "r") as f:
	lista = f.readlines()
	getStandings(lista[1].strip(), lista[3].strip(), 329742)
	# getFilteredContests(lista[1].strip(), lista[3].strip(), 1, "description")
