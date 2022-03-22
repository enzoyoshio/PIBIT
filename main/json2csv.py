import pandas as pd
import os
import json
import csv

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# create not a csv directly in files, create an element that represents
# a csv and then returns it? so we can have stuff
def json2csv(json_file, idd):
	# wont't check if it really is a json file, just pray that people will have sense

	questoes = len(json_file['result']['problems'])
	# for now lets ignore rows 'contest' and 'problems'
	times = json_file['result']['rows']
	#d = times[0]
	
	header = ['teamName', 'handle1', 'handle2', 'handle3', 'rank', 'points', 'penalty']
	for i in range(questoes):
		header.append(abc[i] + '_points')
		header.append(abc[i] + '_rejectedAttemptCount')
		header.append(abc[i] + '_bestSubmissionTimeSeconds')


	# for k, v in d.items():
	#	print(k, '\n', v, '\n\n')
	# do we need teamID?
	# do we need start time?
	# append none or the string none?
	with open(str(idd) + '.csv', 'w', encoding='UTF8') as f:
		writer = csv.writer(f)
		writer.writerow(header)

		for d in times:
			coisa = []

			if 'teamName' in d['party']:
				coisa.append(d['party']['teamName'])
			else:
				coisa.append('None')
			for m in d['party']['members']:
				coisa.append(m['handle'])
			while len(coisa) < 4:
				coisa.append('None')
			coisa.append(d['rank'])
			coisa.append(d['points'])
			coisa.append(d['penalty'])
			
			for k in d['problemResults']:
				coisa.append(k['points'])
				coisa.append(k['rejectedAttemptCount'])
				if 'bestSubmissionTimeSeconds' in k:
					coisa.append(k['bestSubmissionTimeSeconds'])
				else:
					coisa.append('None')
			writer.writerow(coisa)
	
