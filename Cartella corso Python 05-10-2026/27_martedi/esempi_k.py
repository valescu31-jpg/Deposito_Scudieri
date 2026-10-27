from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(iris.data, iris.target)                     # memorizza i 150 fiori

nuovo = [[6.0, 2.8, 4.9, 1.6]]                      # misure di un fiore mai visto
distanze, indici = knn.kneighbors(nuovo)            # chi sono i 3 vicini?

print("Distanze:", distanze.round(2))
print("Classi dei vicini:", iris.target[indici])    # le loro specie
print("Predizione:", iris.target_names[knn.predict(nuovo)]) #prendero gli 0/1 o 2
print("Probabilità:", knn.predict_proba(nuovo))     # frazione di voti per classe= percentuali delle classificazione



#INTERMEDIO

import numpy as np                                            # Importa la libreria NumPy per il calcolo scientifico e manipolazione di array
from sklearn.datasets import load_iris                        # Importa la funzione per caricare il dataset Iris
from sklearn.neighbors import KNeighborsClassifier            # Importa l'algoritmo K-Nearest Neighbors (KNN) per la classificazione

X, y = load_iris(return_X_y=True)                             # Carica le caratteristiche (X) e le etichette (y) del dataset Iris
nuovo = np.array([6.1, 2.9, 4.6, 1.45])                       # Definisce un nuovo campione (un fiore con 4 feature specifiche) sotto forma di array NumPy

distanze_manuali = np.sqrt(((X - nuovo) ** 2).sum(axis=1))      # Calcola manualmente la distanza euclidea (Pitagora) tra il nuovo punto e tutte le righe di X
indici_vicini = np.argsort(distanze_manuali)[:5]              # Ordina le distanze in modo crescente e seleziona i primi 5 indici (i 5 vicini più vicini)
print("Vicini (manuale):", indici_vicini, distanze_manuali[indici_vicini].round(3)) # Stampa gli indici dei 5 vicini calcolati manualmente e le loro distanze arrotondate a 3 decimali

knn = KNeighborsClassifier(n_neighbors=5).fit(X, y)             # Inizializza il modello KNN impostando k=5 e lo addestra (fit) sui dati X e y
dist, ind = knn.kneighbors([nuovo])                           # Usa il metodo nativo di scikit-learn per trovare le distanze (dist) e gli indici (ind) dei 5 vicini del nuovo punto
print("Vicini (sklearn):", ind[0], dist[0].round(3))            # Stampa i risultati trovati da scikit-learn (indici e distanze arrotondate a 3 decimali)        # stessi punti, stesse distanze





#DIFFICLE K GRANDE E K PICCOLO

import matplotlib.pyplot as plt                 # Importa la libreria per la creazione di grafici
from sklearn.datasets import load_iris          # Importa la funzione per caricare il dataset Iris
from sklearn.neighbors import KNeighborsClassifier # Importa l'algoritmo di classificazione K-Nearest Neighbors (KNN)
from sklearn.inspection import DecisionBoundaryDisplay # Importa lo strumento per visualizzare i confini di decisione del modello

X, y = load_iris(return_X_y=True)               # Carica il dataset Iris separando le caratteristiche (X) dalle etichette/classi (y)
X2 = X[:, [0, 1]]                              # Seleziona solo le prime 2 feature (lunghezza e larghezza sepalo) per poter tracciare un grafico 2D

fig, axes = plt.subplots(1, 2, figsize=(11, 4))   # Crea una figura con due sottografici (axes) affiancati di dimensioni 11x4 pollici
for ax, k in zip(axes, [1, 30]):                # Esegue un ciclo iterando su ciascun grafico e su due valori diversi di k (1 e 30)
    knn = KNeighborsClassifier(n_neighbors=k).fit(X2, y) # Inizializza il modello KNN con il valore corrente di k e lo addestra sui dati X2, y
    DecisionBoundaryDisplay.from_estimator(     # Colora lo sfondo del piano cartesiano in base alla classe prevista dal modello
        knn, X2, response_method="predict", alpha=0.4, ax=ax)
    ax.scatter(X2[:, 0], X2[:, 1], c=y, edgecolor="k", s=20) # Disegna i punti reali dei dati sul grafico, colorandoli in base alla classe effettiva (c=y)
    ax.set_title(f"k = {k}")                    # Imposta il titolo del sottografico mostrando il valore corrente di k
    ax.set_xlabel("lunghezza sepalo"); ax.set_ylabel("larghezza sepalo") # Etichetta rispettivamente l'asse X e l'asse Y con i nomi delle feature
plt.show()                                      # Mostra a schermo la figura finale con i grafici generati



#Con k = 1 il confine è frastagliato e crea "isole" attorno a singoli punti: il modello insegue il rumore.
#Con k = 30 il confine è molto più liscio: il modello è più stabile ma può perdere dettagli.
#DecisionBoundaryDisplay prova il modello su una griglia di punti e colora ciascuno con la classe prevista.