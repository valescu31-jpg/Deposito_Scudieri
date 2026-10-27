#Obiettivo: su load_wine() addestra un KNeighborsClassifier(n_neighbors=3) su tutto il dataset, 
# poi per il campione di indice 100 stampa i 3 vicini (indici, distanze, classi) con kneighbors 
# e la predizione finale.

from sklearn.datasets import  load_wine
from sklearn.neighbors import KNeighborsClassifier

X, y = load_wine(return_X_y=True)

modello = KNeighborsClassifier(n_neighbors=3)                       # 4) scelta del modello
modello.fit(X, y)                                       # 5) addestramento SOLO sul training

# 3. Selezione del campione di indice 100 (convertito in formato 2D)
campione = X[100].reshape(1, -1)

# 4. Estrazione dei 3 vicini più vicini (indici e distanze)
distanze, indici = modello.kneighbors(campione)

# Estraiamo i dati della prima (e unica) riga restituita
vicini_indici = indici[0]
vicini_distanze = distanze[0]
vicini_classi = y[vicini_indici] # Classi reali dei vicini nel dataset

# 5. Predizione finale del modello per il campione 100
predizione = modello.predict(campione)

# --- STAMPA DEI RISULTATI ---
print(f"Analisi del campione di indice 100:")
print(f"- Classe reale del campione: {y[100]}")
print(f"- Classe predetta dal modello: {predizione[0]}\n")

print("I 3 vicini più vicini trovati:")
for i in range(3):
    print(f"  * Vicino {i+1}:")
    print(f"    - Indice nel dataset: {vicini_indici[i]}")
    print(f"    - Distanza euclidea: {vicini_distanze[i]:.4f}")
    print(f"    - Classe del vicino: {vicini_classi[i]}")