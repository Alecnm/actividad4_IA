import pandas as pd
import os
from clustering import ejecutar_clustering, visualizar_clusters

working_dir = current_directory = os.getcwd()
# Cargar los datos
df = pd.read_csv(current_directory + '/data/transporte.csv')

# Convertir variables categóricas a numéricas
df['rutas'] = df['rutas'].astype('category').cat.codes
df['clima'] = df['clima'].astype('category').cat.codes
df['congestion'] = df['congestion'].astype('category').cat.codes

# Seleccionar características para el agrupamiento
X = df[['rutas', 'pasajeros', 'tiempo_viaje', 'clima', 'congestion']]

# Ejecutar clustering
df['cluster'] = ejecutar_clustering(X, num_clusters=3)

# Visualizar resultados
visualizar_clusters(df, 'pasajeros', 'tiempo_viaje', 'cluster')
