from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)       # data e target diventano oggetti pandas
df = wine.frame                       # DataFrame unico: feature + colonna "target"

print(df.shape)                                       # (178, 14)
print(df["target"].value_counts())                    # quanti campioni per classe
print(df.groupby("target")[["alcohol", "color_intensity"]].mean())   # medie per classe



print("==================================================================================")

import matplotlib.pyplot as plt  # Importa la libreria Matplotlib per la visualizzazione grafica dei dati
from sklearn.datasets import (
    make_blobs,
    make_classification,
    make_moons,
)  # Importa tre funzioni da scikit-learn per generare dataset sintetici di prova

# Genera un dataset di 300 campioni suddivisi in 3 cluster (nuvole) con distribuzione gaussiana e deviazione standard 0.8
X1, y1 = make_blobs(
    n_samples=300, centers=3, cluster_std=0.8, random_state=42
)  # 3 nuvole

# Genera un dataset di 300 campioni a forma di due mezze lune intersecate, aggiungendo un livello di rumore (noise) pari a 0.2
X2, y2 = make_moons(
    n_samples=300, noise=0.2, random_state=42
)  # 2 mezzelune

# Genera un dataset sintetico per la classificazione con 300 campioni, 2 feature totali, entrambe informative e 0 ridondanti
X3, y3 = make_classification(
    n_samples=300,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=42,
)  # 2 classi generiche

# Crea una figura (finestra di disegno) contenente una griglia di sotto-grafici (subplots) disposti in 1 riga e 3 colonne, con dimensioni di 12x4 pollici
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Avvia un ciclo 'for' che scorre contemporaneamente ciascun asse grafico (ax) e la tupla di dati corrispondente (X, y, titolo)
for ax, (X, y, titolo) in zip(
    axes,
    [
        (X1, y1, "make_blobs"),
        (X2, y2, "make_moons"),
        (X3, y3, "make_classification"),
    ],
):
    # Crea un grafico a dispersione (scatter plot): usa la prima colonna di X come asse X e la seconda come asse Y.
    # Il parametro 'c=y' colora i punti in base alla classe di appartenenza, 'cmap' sceglie la palette di colori e 's=15' definisce la dimensione dei punti.
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=15)  # colore = classe

    # Assegna il titolo specifico al sotto-grafico corrente basandosi sul nome della funzione generatrice
    ax.set_title(titolo)

# Visualizza a schermo la figura completa con i tre grafici affiancati
plt.show()

#Ogni funzione make_* restituisce direttamente X, y.
#X[:, 0] e X[:, 1] sono la prima e la seconda colonna: le usiamo come assi x e y del grafico.
#noise e cluster_std regolano quanto i gruppi sono "sporchi" e sovrapposti: più alti → problema più difficile.