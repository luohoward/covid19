import requests
import numpy
import matplotlib.pyplot as plt

url = 'https://pomber.github.io/covid19/timeseries.json'
r = requests.get(url)
totalCases = r.json()

country = input('Enter a valid country name: ')

if country not in totalCases:
    raise KeyError(country + ' is not valid')
else:
    cases = totalCases[country]

    deaths = []
    confirmed = []
    recovered = []

    totalDays = []
    total = 0

    for case in cases:
        totalDays.append(total)
        
        if case['deaths'] != None:
            deaths.append(case['deaths'])
        else:
            deaths.append(deaths[-1])

        if case['confirmed'] != None:
            confirmed.append(case['confirmed'])
        else:
            confirmed.append(confirmed[-1])

        if case['recovered'] != None:
            recovered.append(case['recovered'])
        else:
            recovered.append(recovered[-1])

        total += 1

    plt.title(country + ' Coronavirus total people vs time')
    plt.xlabel('Time (days since first outbreak on ' + cases[0]['date'] + ')')
    plt.ylabel('Total People')

    plt.plot(totalDays, deaths, label='deaths')
    plt.plot(totalDays, confirmed, label='confirmed')
    plt.plot(totalDays, recovered, label='recovered')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.show()
