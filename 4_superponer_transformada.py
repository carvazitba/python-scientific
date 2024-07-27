import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Cargar los datos EEG del primer archivo
file_path_1 = 'data_carlos/baseline.dat'  # Ajusta la ruta si es necesario
data_eeg_1 = pd.read_csv(file_path_1, delimiter=' ', header=None)

# Extraer la señal EEG del primer archivo (suponiendo que está en la tercera columna)
signal_eeg_1 = data_eeg_1.iloc[:, 2].values

# Cargar los datos EEG del segundo archivo
file_path_2 = 'data_carlos/pestaneos.dat'  # Ajusta la ruta si es necesario
data_eeg_2 = pd.read_csv(file_path_2, delimiter=' ', header=None)

# Extraer la señal EEG del segundo archivo (suponiendo que está en la tercera columna)
signal_eeg_2 = data_eeg_2.iloc[:, 2].values

# Parámetros de la señal
fs = 512  # Frecuencia de muestreo (Hz)

# Crear función para calcular el espectro de potencia
def calculate_power_spectrum(signal, fs):
    T = len(signal) / fs  # Duración total de la señal (s)
    t = np.linspace(0, T, len(signal), endpoint=False)

    # Aplicar ventana (opcional, para reducir efectos de borde)
    window = np.hamming(len(signal))
    signal = signal.astype(np.float64) * window.astype(np.float64)

    # Calcular la Transformada Rápida de Fourier (FFT)
    fft_result = fft(signal)

    # Obtener las frecuencias correspondientes
    freqs = fftfreq(len(signal), 1/fs)

    # Filtrar para frecuencias positivas (tomar la mitad del espectro)
    positive_freqs = freqs[:len(freqs)//2]
    fft_result = fft_result[:len(fft_result)//2]

    # Calcular el espectro de potencia
    power_spectrum = np.abs(fft_result)**2

    # Filtrar valores de frecuencia entre 0 y 15 Hz
    mask = (positive_freqs >= 0) & (positive_freqs <= 15)
    filtered_freqs = positive_freqs[mask]
    filtered_power_spectrum = power_spectrum[mask]

    return filtered_freqs, filtered_power_spectrum

# Calcular el espectro de potencia para ambos archivos
filtered_freqs_1, filtered_power_spectrum_1 = calculate_power_spectrum(signal_eeg_1, fs)
filtered_freqs_2, filtered_power_spectrum_2 = calculate_power_spectrum(signal_eeg_2, fs)

# Visualizar el espectro de potencia superpuesto con límite en el eje Y
plt.plot(filtered_freqs_1, filtered_power_spectrum_1, label='baseline')
plt.plot(filtered_freqs_2, filtered_power_spectrum_2, label='pestaneo')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Espectro de Potencia')
plt.title('Espectro de Potencia de la Señal EEG (0-15 Hz)')
plt.xlim(0, 15)  # Ajustar el rango de frecuencias según sea necesario
plt.ylim(60000000, 26100000000)  # Limitar el eje Y a valores entre 0 y 3
plt.grid(True)
plt.legend()
plt.show()
