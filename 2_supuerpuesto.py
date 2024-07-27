import csv
import numpy as np
import matplotlib.pyplot as plt

# Define file paths (replace with your actual paths)
eeg_file = 'data_carlos/baseline.dat'
blinking_file = 'data_carlos/pestaneos.dat'

# Load EEG data
eeg_results = []
with open(eeg_file) as inputfile:
    for row in csv.reader(inputfile):
        rows = row[0].split(' ')
        eeg_results.append(rows[1:])

eeg_data = np.asarray(eeg_results)
eeg_data = eeg_data.astype(int)
eeg = eeg_data[1:, 1]  # Extract EEG signal

# Load blinking data (assuming similar format)
blinking_results = []
with open(blinking_file) as inputfile:
    for row in csv.reader(inputfile):
        rows = row[0].split(' ')
        blinking_results.append(rows[1:])

blinking_data = np.asarray(blinking_results)
blinking_data = blinking_data.astype(int)
blinking = blinking_data[1:, 1]  # Extract blinking signal

# Assuming data lengths are compatible (adjust if needed)
filtered_eeg = eeg
filtered_blinking = blinking

# Create the plot
plt.figure(figsize=(12, 5))

# Plot EEG data (green line)
plt.plot(filtered_eeg, color="green", label="EEG")

# Plot blinking data (red line)
plt.plot(filtered_blinking, color="red", label="Blinking")

# Add labels and title
plt.ylabel("Amplitude", size=10)
plt.xlabel("Timepoints", size=10)
plt.title("EGG: baseline vs pestaneos (time: 4000 a 6000)", size=20)

# Add legend to differentiate lines
plt.legend()

# Adjust X-axis limit if necessary (assuming timestamps are in the first column)
if len(eeg) == len(blinking):
    # Use the same X-axis limits for both signals if data lengths match
    plt.xlim(0, max(eeg_data[:, 0]))  # Use timestamps from EEG data
else:
    # Handle potential differences in data length by setting appropriate limits
    # (You might need to adjust based on your specific data)
    plt.xlim(4000, 6000)  # Example limit

plt.show()
