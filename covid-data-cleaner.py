import json

with open('covid-data.json', 'r') as json_file:
	data = json.load(json_file)

matriz = []

for country in data:
	lastMonth = data[country]['data'][0]['date'][6]
	lastData = []
	for daysInformation in data[country]['data']:
		newMonth = daysInformation['date'][6]

		if lastMonth != newMonth:
			matriz.append(lastData)

		deaths = 0
		if 'total_deaths' in daysInformation:
			deaths = daysInformation['total_deaths']

		lastMonth = newMonth
		lastData = [ data[country]['location'], daysInformation['date'], deaths ]

print(matriz)
