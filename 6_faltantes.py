import pandas as pd

# Cargar el archivo con espacio como delimitador
file_path_new = 'data_carlos/probano.dat'
df_new = pd.read_csv(file_path_new, delimiter='\s+', header=None)

# Renombrar las columnas para una referencia más fácil
df_new.columns = ['Timestamp', 'Counter', 'Value1', 'Value2', 'Value3', 'Value4']

# Función revisada para encontrar números faltantes en la secuencia del contador
def verificar_secuencia_consecutiva(counter_series):
    """Verifica si una secuencia de números contiene interrupciones, excluyendo el salto de 99 a 0.

    Args:
        counter_series: Serie de contadores a verificar.

    Returns:
        Una lista de números faltantes en la secuencia.
    """
    counter_series = counter_series.sort_values().reset_index(drop=True)
    missing_numbers = []

    # Verificar números faltantes en la secuencia
    for i in range(1, len(counter_series)):
        if counter_series[i] != counter_series[i-1] + 1:
            missing_range = list(range(counter_series[i-1] + 1, counter_series[i]))
            missing_numbers.extend(missing_range)

    return missing_numbers

# Verificar las interrupciones en la secuencia del contador
missing_numbers = verificar_secuencia_consecutiva(df_new['Counter'])

if not missing_numbers:
    print("La secuencia de contadores es correcta.")
else:
    print(f"La secuencia de contadores contiene interrupciones: {missing_numbers}")
