#Obiettivo: su load_wine() addestra un KNeighborsClassifier(n_neighbors=3) su tutto il dataset, 
# poi per il campione di indice 100 stampa i 3 vicini (indici, distanze, classi) con kneighbors 
# e la predizione finale.

from sklearn.datasets import  load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, cross_val_score # Per suddividere i dati e fare la CV

X, y = load_wine(return_X_y=True)

modello = KNeighborsClassifier(n_neighbors=3)                       # 4) scelta del modello
modello.fit(X, y)                                       # 5) addestramento SOLO sul training

# 4. Estrazione del campione 100 e trasformazione in matrice 2D (1 riga, N colonne) richiesta da scikit-learn
campione = X[100].reshape(1, -1)

# 5. Ricerca dei 3 vicini più vicini: restituisce una tupla con (matrice_distanze, matrice_indici)
distanze, indici = modello.kneighbors(campione)

# 6. Estrazione dei dati relativi all'unica riga analizzata (indice [0])
vicini_indici = indici[0]        # Array 1D contenente i 3 indici dei vicini nel dataset
vicini_distanze = distanze[0]    # Array 1D con le rispettive distanze euclidee
vicini_classi = y[vicini_indici] # "Advanced indexing" di NumPy: recupera le classi reali dei 3 vicini

# 7. Esecuzione della predizione finale per il campione 100 basata sulla maggioranza dei vicini
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



print("====================================================================================")
#Obiettivo: su load_diabetes() (regressione) usa KNeighborsRegressor con k = 1, 5, 20 e con weights "uniform" e "distance".
#  Dividi i dati 80/20 e stampa score sul test per tutte e 6 le combinazioni ( lo score di un regressore vale 1 se perfetto, si abbassa al peggiorare e può diventare negativo).
#  Quale combinazione funziona meglio?

print("Difficile")

from sklearn.datasets import  load_diabetes


X, y = load_diabetes(return_X_y=True)

# 2. Divisione in Training e Test set (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definizione dei parametri da testare
k_values = [1, 5, 20]                               # Lista dei valori di k (numero di vicini) da provare
weights_values = ['uniform', 'distance']            # Tipologie di pesatura dei vicini

# Liste per memorizzare i risultati delle metriche
results = []
cv_results = []
