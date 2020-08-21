#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import sys

if len(sys.argv) < 4:
	print("Utilizare: " + sys.argv[0] + " -f <nume fisier CSV> ALEGERI")
	print("ALEGERI pot fi '2019euro', '2019tur1' sau '2019tur2'")
	sys.exit()

if sys.argv[1] != "-f":
	print("Utilizare: " + sys.argv[0] + " -f <nume fisier CSV> ALEGERI")
	print("ALEGERI pot fi '2019euro', '2019tur1' sau '2019tur2'")
	sys.exit()

try: 
	df = pd.read_csv(sys.argv[2])
	if sys.argv[3] == '2019euro' or sys.argv[3] == '2019tur1' or sys.argv[3] == '2019tur2':
		mod = sys.argv[3]
	else:
		sys.exit("Eroare: Numele alegerilor trebuie sa fie '2019euro', '2019tur1' sau '2019tur2'")
except:
	sys.exit("Eroare: Fisierul nu a fost gasit.")

def mod_2019tur1(df):
	suma = df.sum(axis = 0, skipna = True)

	altii = suma["g6"] + suma["g7"] + suma["g8"] + suma["g9"] + suma["g11"] + suma["g12"] + suma["g13"] + suma["g14"]

	rezultate = [suma["g1"], suma["g2"], suma["g3"], suma["g4"], suma["g5"], suma["g10"], altii]
	candidati = ['Iohannis', 'Paleologu', 'Barna', 'Hunor', 'Dancila', 'Diaconu', 'Altii']
	colors = ['y', 'orange', 'blue', 'g', 'r', 'm','w']

	plt.pie(rezultate, labels=candidati, colors=colors, startangle=90, autopct='%.1f%%')
	plt.show()
    
def mod_2019tur2(df):
	suma = df.sum(axis = 0, skipna = True)

	rezultate = [suma["g1"], suma["g2"]]
	candidati = ['Iohannis', 'Dancila']
	colors = ['y', 'r']

	plt.pie(rezultate, labels=candidati, colors=colors, startangle=90, autopct='%.1f%%')
	plt.show()

def mod_2019euro(df):
	suma = df.sum(axis = 0, skipna = True)

	altii = suma["g7"] + suma["g9"] + suma["g10"] + suma["g11"] + suma["g12"] + suma["g13"] + suma["g14"] + suma["g15"] + suma["g16"]

	rezultate = [suma["g1"], suma["g2"], suma["g3"], suma["g4"], suma["g5"], suma["g6"], suma["g8"], altii]
	candidati = ['PSD', 'USR-PLUS', 'Pro Romania', 'UDMR', 'PNL', 'ALDE', 'PMP', 'Altii']
	colors = ['r', 'blue', 'orange', 'green', 'yellow', 'm', 'olive', 'w']

	plt.pie(rezultate, labels=candidati, colors=colors, startangle=90, autopct='%.1f%%')
	plt.show()

def mod_2019tur2(df):
	suma = df.sum(axis = 0, skipna = True)

	rezultate = [suma["g1"], suma["g2"]]
	candidati = ['Iohannis', 'Dancila']
	colors = ['y', 'r']

	plt.pie(rezultate, labels=candidati, colors=colors, startangle=90, autopct='%.1f%%')
	plt.show()

if mod == '2019tur1':
	mod_2019tur1(df)
elif mod == '2019tur2':
	mod_2019tur2(df)
elif mod == '2019euro':
	mod_2019euro(df)
