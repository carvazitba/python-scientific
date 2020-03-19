"""
==================
STEM Blinking Counter
==================

Contador de pestañeos.

Fs = 128

"""
print(__doc__)

import csv
import numpy as np


results = []

# Esta primera linea, abre el archivo 'blinking.dat' que se grabó
# al establecerse la conexión con el servidor.
with open('data/blinking.dat') as inputfile:
    for row in csv.reader(inputfile):
        rows = row[0].split(' ')
        results.append(rows[1:])

print ('Longitud del archivo:'+str(len(results)))

# Convert the file into numpy array of ints.
results = np.asarray(results)
results = results.astype(int)

# Strip from the signal anything you want


# La primer columna corresponde a el largo del archivo a considerar
# en relación a las muestras (1:100 serian las muestras) representante
# del tiempo.
# La segunda columna, corresponde a: eeg, attention y meditation.
eeg = results[1:,1]

print (eeg)

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(eeg,'r', label='EEG')
plt.legend(loc='upper left');
plt.show()


# El threshold corresponde al limite en amplitud a considerar para discriminar
# que es un pestañeo de qué no lo es.
signalthreshold = 420

# Primero filtramos los valores de la señal que superan un umbral hardcoded
boolpeaks = np.where( eeg > signalthreshold  )
print (boolpeaks)

# Por otro lado, calculamos la derivada de la señal.
dpeaks = np.diff( eeg )
print (dpeaks)

# De la derivada, identificamos los valores positivos que corresponden a las curvas crecientes
pdpeaks = np.where( dpeaks > 0)
print (pdpeaks)
print (pdpeaks != 0)

# boolpeaks y pdpeaks son indices. Por lo tanto vemos cuales de los indices de los picos, 
# son a su vez valores que superan el umbral.
finalresult = np.in1d(pdpeaks,boolpeaks)
print (finalresult)
blinkings = finalresult.sum()

print ('Blinkings: %d' % blinkings)

import matplotlib.pyplot as plt
from scipy.signal import find_peaks

peaks, _ = find_peaks(eeg, height=200)
plt.plot(eeg)
plt.plot(peaks, eeg[peaks], "x")
plt.plot(np.zeros_like(eeg), "--", color="gray")
plt.show()