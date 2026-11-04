#Obiettivo: genera make_blobs(n_samples=400, centers=3, cluster_std=1.0, random_state=7), applica K-Means con k = 3, 
# disegna punti e centroidi e calcola la silhouette media.
#  Ripeti con k = 2 e k = 5 e confronta le silhouette.

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=400, centers=3, cluster_std=1.0, random_state=7)


valori_k= [3,2,5]         # Lista dei valori di k (numero di cluster) che vogliamo testare                                     # fit + etichetta di ogni punto

# Dizionario per memorizzare i punteggi di silhouette per ogni k
punteggi_silhouette = {}

# Creiamo una figura con 3 spazi affiancati per disegnare i grafici
fig, assi = plt.subplots(1, 3, figsize=(18, 5))


# Creiamo una figura con 3 spazi affiancati per disegnare i grafici
fig, assi = plt.subplots(1, 3, figsize=(18, 5))

# Ripetiamo il procedimento per ogni valore di k scelto
for i, k in enumerate(valori_k):

  # Creiamo il modello K-Means dicendogli quanti gruppi (k) cercare
  modello_kmeans = KMeans(n_clusters=k, random_state=7, n_init=10)

  # Facciamo "imparare" il modello e assegniamo ogni punto a un cluster
  etichette_predette = modello_kmeans.fit_predict(X)

  # Troviamo le coordinate esatte dei centroidi (i centri dei cluster)
  centroidi = modello_kmeans.cluster_centers_

  # Calcoliamo la silhouette media per valutare la qualità del raggruppamento
  punteggio = silhouette_score(X, etichette_predette)

  # Salviamo il punteggio nel dizionario
  punteggi_silhouette[k] = punteggio

  # Disegniamo i punti colorati in base al cluster trovato
  assi[i].scatter(
      X[:, 0], X[:, 1], c=etichette_predette, cmap='viridis', s=30, alpha=0.6
  )

  # Disegniamo i centroidi sopra i punti usando una X rossa grande
  assi[i].scatter(
      centroidi[:, 0],
      centroidi[:, 1],
      c='red',
      marker='X',
      s=200,
      label='Centroidi',
  )


# Aggiungiamo un titoletto a ogni grafico con il valore di k e la silhouette
  assi[i].set_title(
      f'K-Means con k = {k}\nSilhouette Media: {punteggio:.3f}', fontsize=12
  )
  assi[i].legend()

# Ottimizziamo lo spazio tra i grafici e li mostriamo a schermo
plt.tight_layout()
plt.show()




print("=================================================================")

print("medio:")
#Obiettivo: su load_iris() standardizza le 4 feature e applica K-Means con k da 2 a 8.
#  Per ogni k salva l'inerzia e la silhouette media,
#  poi disegna i due grafici affiancati (gomito e silhouette). Quale k suggerisce ciascun criterio?
#  I due criteri concordano? Il valore scelto coincide con le 3 specie di iris?

import matplotlib.pyplot as plt                  # Importiamo la libreria per disegnare i grafici
from sklearn.datasets import load_iris           # Importiamo il dataset dei fiori Iris
from sklearn.preprocessing import StandardScaler # Importiamo lo strumento per standardizzare i dati
from sklearn.cluster import KMeans               # Importiamo l'algoritmo di clustering K-Means
from sklearn.metrics import silhouette_score     # Importiamo la funzione per calcolare la silhouette

# FASE 1: Caricamento del dataset Iris
iris = load_iris()                               # Carichiamo il dataset
X = iris.data                                    # Estraiamo le 4 colonne di misurazioni (feature)

# FASE 2: Standardizzazione delle 4 feature
scaler = StandardScaler()                        # Inizializziamo lo StandardScaler
X_scaled = scaler.fit_transform(X)               # Trasformiamo i dati azzerando la media e impostando varianza 1

# Liste vuote per salvare i risultati di ogni k
inerzie = []                                     # Lista che conterrà i valori di inerzia
silhouette_scores = []                           # Lista che conterrà i punteggi di silhouette
k_range = range(2, 9)                            # Intervallo di k che va da 2 a 8 inclusi



# FASE 3: Ciclo per testare K-Means con k da 2 a 8
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) # Creiamo il modello K-Means per il k corrente
    kmeans.fit(X_scaled)                                      # Addestriamo il modello sui dati standardizzati
    
    inerzie.append(kmeans.inertia_)                           # Salviamo l'inerzia del modello
    score = silhouette_score(X_scaled, kmeans.labels_)        # Calcoliamo la silhouette media
    silhouette_scores.append(score)                           # Salviamo il punteggio di silhouette



    # FASE 4: Disegno dei due grafici affiancati
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))         # Creiamo una figura con 2 grafici affiancati

# Primo grafico: Metodo del Gomito (Inerzia)
ax1.plot(k_range, inerzie, marker='o', color='blue')          # Tracciamo la curva dell'inerzia
ax1.set_title("Metodo del Gomito (Inerzia)")                  # Titolo del primo grafico
ax1.set_xlabel("Numero di cluster (k)")                       # Etichetta asse X
ax1.set_ylabel("Inerzia")                                     # Etichetta asse Y

# Secondo grafico: Silhouette Media
ax2.plot(k_range, silhouette_scores, marker='s', color='green') # Tracciamo la curva della silhouette
ax2.set_title("Silhouette Media")                             # Titolo del secondo grafico
ax2.set_xlabel("Numero di cluster (k)")                       # Etichetta asse X
ax2.set_ylabel("Silhouette Score")                            # Etichetta asse Y

plt.tight_layout()                                            # Ottimizziamo lo spazio tra i grafici
plt.show()                                                    # Mostriamo a schermo i grafici


# 1. Quale k suggerisce ciascun criterio?
#    - Il metodo del Gomito suggerisce k = 3 (il punto in cui la curva smette di scendere bruscamente).
#    - Il criterio della Silhouette suggerisce k = 2 (che ottiene il punteggio medio più alto) oppure k = 3.
# 2. I due criteri concordano?
#    - In parte sì: la silhouette dà il picco massimo a k=2 ma offre un valore molto alto e un buon compromesso anche a k=3, 
#      dove il gomito individua chiaramente il cambio di pendenza.
# 3. Il valore scelto coincide con le 3 specie di iris?
#    - Sì! Scegliendo k = 3, il modello riflette esattamente le 3 specie biologiche di fiori presenti nel dataset originale.