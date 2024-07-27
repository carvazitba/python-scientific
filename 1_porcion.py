import csv
import numpy as np
import matplotlib.pyplot as plt

results = []

# Open blinking.dat file.
with open('data_carlos/inhalar.dat') as inputfile:
    for row in csv.reader(inputfile):
        rows = row[0].split(' ')
        results.append(rows[1:])

# Convert the file into a numpy array of ints.
results = np.asarray(results)
results = results.astype(int)

# Pick the EEG signal.
eeg = results[1:, 1]

# Assuming eeg is a 1D array (adjust if necessary)
filtered_eeg = eeg

plt.figure(figsize=(12, 5))
plt.plot(filtered_eeg, color="green")
plt.ylabel("Amplitude", size=10)
plt.xlabel("Timepoints", size=10)
plt.title("Serie temporal de eeg", size=20)
plt.xlim(0, 5000)  # Set X-axis limit to display only up to timestamp 5000
plt.show()
