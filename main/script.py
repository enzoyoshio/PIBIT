"""
o que acabou sendo -> webscrap/crawler

ideias de como parsear:

1. escrever algo na descrição 	(talvez criar uma hash? contra: nao pode esquecer de adicionar a descrição no contest XD)
2. parsear pelo nome do contest (contra: todos os contests do grupo deveriam ter pelo menos uma palavra em comum)
3. Autor 			(contra: apenas uma pessoa pode preparar os contests)
4. school/city/country 		(contra: usar tres filtros para parsear de forma "otima")
5. websiteUrl 			(poderia usar o site do cic? contra: mesmo do numero 1)

"""
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
from standings import getStandings

cfKey = ""
cfSecret = ""

with open("../senhas.txt", "r") as f:
	linhas = f.readlines()
	cfKey = linhas[3].strip()
	cfSecret = linhas[5].strip()

with open("contests_ids.txt", "r") as f:
	lista = f.readlines()
	for ids in lista:
		getStandings(cfKey, cfSecret, ids.strip())
	# getFilteredContests(lista[1].strip(), lista[3].strip(), 1, "description")
