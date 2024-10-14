from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def ejecutar_clustering(X, num_clusters=3):
    """
    Ejecuta el algoritmo K-means en los datos proporcionados.
    
    :param X: Variables independientes (features) para el agrupamiento
    :param num_clusters: Número de clusters a generar
    :return: Etiquetas de los clusters asignados a cada dato
    """
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(X)
    return clusters

def visualizar_clusters(df, feature1, feature2, cluster_column):
    """
    Genera un gráfico de dispersión de los clusters.
    
    :param df: DataFrame con los datos y los clusters asignados
    :param feature1: Columna a usar en el eje X
    :param feature2: Columna a usar en el eje Y
    :param cluster_column: Columna que contiene los clusters
    """
    plt.scatter(df[feature1], df[feature2], c=df[cluster_column], cmap='viridis')
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.title('Agrupamiento de Datos')
    plt.show()
