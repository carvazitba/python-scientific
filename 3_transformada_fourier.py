import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Cargar el dataset
file_path = 'data_carlos/baseline.dat'  # Actualiza con la ruta correcta
data = pd.read_csv(file_path, delimiter=' ', header=None)

# Extraer la tercera columna
third_column = data.iloc[:, 2].values

# Número de puntos de muestra
N = len(third_column)

# Espaciado de muestras (suponiendo una frecuencia de muestreo de 40Hz)
T = 1.0 / 40.0  

# Calcular la transformada de Fourier
yf = fft(third_column)
xf = fftfreq(N, T)[:N//2]

# Filtrar frecuencias entre 1 Hz y 39 Hz
freq_min = 0
freq_max = 50
mask = (xf >= freq_min) & (xf <= freq_max)

# Aplicar la máscara a las frecuencias y transformada
xf_filtered = xf[mask]
yf_filtered = np.abs(yf[:N//2])[mask]

# Filtrar valores en el eje Y mayores a 35000
y_value_limit = 35000
yf_filtered = np.where(yf_filtered > y_value_limit, y_value_limit, yf_filtered)

# Graficar la transformada de Fourier
plt.figure(figsize=(10, 6))
plt.plot(xf_filtered, yf_filtered)
plt.title('Transformada de Fourier de la Tercera Columna')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid()
plt.show()
