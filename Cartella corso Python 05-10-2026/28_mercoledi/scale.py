import numpy as np
from sklearn.preprocessing import StandardScaler

# Definizione della matrice X con 3 campioni e 2 feature su scale numeriche molto diverse
X = np.array([[1000, 0.5],
              [1500, 0.2],
              [ 500, 0.8]])             

# Inizializzazione dello scaler per la standardizzazione (media = 0, deviazione standard = 1)
scaler = StandardScaler()

# Calcolo di media e deviazione standard sui dati e successiva trasformazione (z-score)
X_std = scaler.fit_transform(X)         

# Stampa delle medie calcolate per ciascuna delle due colonne: [1000.0, 0.5]
print("Medie imparate:", scaler.mean_)        

# Stampa delle deviazioni standard arrotondate a 3 decimali (circa [408.248, 0.245])
print("Dev. standard:", scaler.scale_.round(3))

# Stampa della matrice standardizzata arrotondata a 2 decimali:
# [[ 0.    0.  ]   -> (1000-1000)/408.25, (0.5-0.5)/0.245
#  [ 1.22 -1.22]   -> (1500-1000)/408.25, (0.2-0.5)/0.245
#  [-1.22  1.22]]  -> (500-1000)/408.25,  (0.8-0.5)/0.245
print(X_std.round(2))                     

# Verifica che le nuove medie lungo le colonne siano 0.0 (con tolleranza macchina)
print("Nuove medie:", X_std.mean(axis=0).round(2))   # Output: [0. 0.]

# Verifica che le nuove deviazioni standard lungo le colonne siano pari a 1.0
print("Nuove dev. std:", X_std.std(axis=0).round(2)) # Output: [1. 1.]














print("==================================================================================")

#NORMALIZAZZIONE E STANDARDIZAZZIONE
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

stipendi = np.array([[1800], [2100], [2400], [2000], [25000]])   # l'ultimo è un outlier

minmax = MinMaxScaler().fit(stipendi)
standard = StandardScaler().fit(stipendi)

print("MinMax:  ", minmax.transform(stipendi).ravel().round(3))     # i "normali" finiscono vicino a 0
print("Standard:", standard.transform(stipendi).ravel().round(3))

originali = minmax.inverse_transform(minmax.transform(stipendi))    # torniamo indietro
print("Ricostruiti:", originali.ravel())
#MinMax:   [0.    0.013 0.026 0.009 1.   ] 0 valore minimo e 1 valore massimo, quelli in mezzo sono valori per arrivare al valore massimo
#Standard: [-0.53  -0.497 -0.464 -0.508  2.   ] quanto i singoli valori variano dalla media, ma media essendo 0 solo 2 sara soprs lamedia ed e' uguale a 25k
#Ricostruiti: [ 1800.  2100.  2400.  2000. 25000.]




print("APPLICATO ALLO SCILEARN")

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Caricamento del dataset "Wine" (contiene proprietà chimiche di diversi vini e la loro classe)
X, y = load_wine(return_X_y=True)

# Divisione del dataset: 80% dei dati per l'addestramento (train) e 20% per il test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 1. MODELLO SENZA SCALING (Dati Grezzi)
# ==========================================
# Inizializzazione del classificatore KNN (k=5 vicini) e fit diretto sui dati non scalati
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)

# Calcolo e stampa dell'accuratezza sul test set senza scaling (risultato: 0.72 / 72%)
# Spiegazione: Senza scaling, le feature con valori numerici grandi (es. magnesio o proline) 
# dominano il calcolo delle distanze geometriche del KNN, penalizzando le feature con valori piccoli.
print("Senza scaling:", round(knn.score(X_test, y_test), 2))      # 0.72


# ==========================================
# 2. MODELLO CON STANDARDIZZAZIONE (StandardScaler)
# ==========================================
# Creazione dello StandardScaler e fit SOLO sul training set (fondamentale per evitare il "Data Leakage")
scaler = StandardScaler().fit(X_train)

# Applicazione della trasformazione al training set (centratura a media 0 e deviazione standard 1)
X_train_s = scaler.transform(X_train)

# Applicazione della stessa trasformazione al test set 
# NOTA BENE: Il test set viene trasformato usando le statistiche (media e dev. standard) del training, 
# per simulare scenari reali in cui i dati futuri non devono influenzare il modello.
X_test_s = scaler.transform(X_test)                                

# Addestramento del KNN utilizzando i dati standardizzati
knn_s = KNeighborsClassifier(n_neighbors=5).fit(X_train_s, y_train)

# Calcolo e stampa dell'accuratezza con i dati standardizzati (risultato: 0.94 / 94%)
# Spiegazione della normalizzazione/standardizzazione: portando tutte le feature sulla stessa scala, 
# il KNN calcola le distanze in modo equo, permettendo un salto netto dell'accuratezza (+22%).
print("Con scaling (Standardizzazione Z-score):  ", round(knn_s.score(X_test_s, y_test), 2))   # 0.94
