#Prezidentiale 2019

import matplotlib.pyplot as plt
import pandas as pd
import sys

if len(sys.argv) < 3:
	print("Utilizare: " + sys.argv[0] + " -f <nume fisier CSV>")
	sys.exit()

if sys.argv[1] != "-f":
	print("Utilizare: " + sys.argv[0] + " -f <nume fisier CSV>")
	sys.exit()

try: 
	df = pd.read_csv(sys.argv[2])
except:
	sys.exit("Eroare: Fisierul nu a fost gasit.")

#dfs = pd.read_csv('rezs.csv')

suma = df.sum(axis = 0, skipna = True)

altii = suma["g6"] + suma["g7"] + suma["g8"] + suma["g9"] + suma["g11"] + suma["g12"] + suma["g13"] + suma["g14"]

#rezultate = [suma["g1"], suma["g2"], suma["g3"], suma["g4"], suma["g5"], suma["g6"], suma["g7"], suma["g8"], suma["g9"], suma["g10"], suma["g11"], suma["g12"], suma["g13"], suma["g14"]]
rezultate = [suma["g1"], suma["g2"], suma["g3"], suma["g4"], suma["g5"], suma["g10"], altii]
candidati = ['Iohannis', 'Paleologu', 'Barna', 'Hunor', 'Dancila', 'Diaconu', 'Altii']
colors = ['y', 'orange', 'cyan', 'g', 'r', 'm','w']

total_voturi_numarate = suma["g1"] + suma["g2"] + suma["g3"] + suma["g4"] + suma["g5"] + suma["g6"] + suma["g7"] + suma["g8"] + suma["g9"] + suma["g10"] + suma["g11"] + suma["g12"] + suma["g13"] + suma["g14"]

total_voturi = 8683688
plt.title('Voturi numarate: ' + str(total_voturi_numarate) + ' din ' + str(total_voturi))

plt.pie(rezultate, labels=candidati, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()

'''suma = dfs.sum(axis = 0, skipna = True)

altii = suma["g6"] + suma["g7"] + suma["g8"] + suma["g9"] + suma["g11"] + suma["g12"] + suma["g13"] + suma["g14"]

rezultate = [suma["g1"], suma["g2"], suma["g3"], suma["g4"], suma["g5"], suma["g10"], altii]
candidati = ['Iohannis', 'Paleologu', 'Barna', 'Hunor', 'Dancila', 'Diaconu', 'Altii']
colors = ['y', 'orange', 'cyan', 'g', 'r', 'm','w']

total_voturi_numarate = suma["g1"] + suma["g2"] + suma["g3"] + suma["g4"] + suma["g5"] + suma["g6"] + suma["g7"] + suma["g8"] + suma["g9"] + suma["g10"] + suma["g11"] + suma["g12"] + suma["g13"] + suma["g14"]

plt.title('Voturi numarate: ' + str(total_voturi_numarate) + ' (DIASPORA)')

plt.pie(rezultate, labels=candidati, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()'''