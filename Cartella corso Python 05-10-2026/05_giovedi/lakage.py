#Obiettivo: trova e correggi l'errore in questo codice: X = MinMaxScaler().fit_transform(X) 
# seguito da X_train, X_test, y_train, y_test = train_test_split(X, y). 
# Riscrivilo nella versione corretta su load_digits().


from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""""
X = MinMaxScaler().fit_transform(X) 
 X_train, X_test, y_train, y_test = train_test_split(X, y)  
"""""
#L'errore sta della regola fondametnale del data leakage, essendo che non abiamo diviso prima il dataset in train e test, compromettendo l'indipendenza del test e del train stesso



#RISCRITTO CORRETTAMENTE:
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# 1. Carichiamo il dataset delle cifre
digits = load_digits()
X, y = digits.data, digits.target

# 2. Prima dividiamo il dataset in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Inizializziamo il MinMaxScaler
scaler = MinMaxScaler()

# 4. Facciamo il fit e la trasformazione ESCLUSIVAMENTE sul training set
X_train_scaled = scaler.fit_transform(X_train)

# 5. Sul test set applichiamo SOLAMENTE il transform (usando i min/max imparati dal train)
X_test_scaled = scaler.transform(X_test)


print("Intermedio:")

#Obiettivo: su load_breast_cancer() addestra un KNN con scaling fatto nei due modi (sbagliato e corretto). 
# Ripeti per 10 valori di random_state dello split e confronta la media delle accuratezze ottenute nei due casi.


import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Carichiamo il dataset dei tumori al seno
dati = load_breast_cancer()
X = dati.data
y = dati.target

# Creiamo due liste vuote per salvare le accuratezze dei 10 esperimenti
accuratezze_sbagliate = []
accuratezze_corrette = []

# 2. Ripetiamo l'esperimento per 10 valori diversi di random_state (da 0 a 9)
for r_state in range(10):
    
    # --- MODO SBAGLIATO (Con Data Leakage) ---
    # ERRORE: Scaliamo TUTTA la X PRIMA di dividerla in train e test.
    # Lo scaler calcola la media e la deviazione standard usando ANCHE il test set,
    # passando informazioni nascoste al training set.
    scaler_err = StandardScaler()
    X_scaled_err = scaler_err.fit_transform(X) # ERRORE: fit sull'intero dataset!
    
    # Dividiamo i dati dopo averli scalati insieme
    X_train_err, X_test_err, y_train_err, y_test_err = train_test_split(
        X_scaled_err, y, test_size=0.2, random_state=r_state
    )
    
    # Addestriamo il modello KNN e calcoliamo l'accuratezza errata
    knn_err = KNeighborsClassifier()
    knn_err.fit(X_train_err, y_train_err)
    y_pred_err = knn_err.predict(X_test_err)
    accuratezze_sbagliate.append(accuracy_score(y_test_err, y_pred_err))
    
    
    # --- MODO CORRETTO (Senza Data Leakage) ---
    # 1. Prima dividiamo i dati grezzi in Train e Test
    X_train_corr, X_test_corr, y_train_corr, y_test_corr = train_test_split(
        X, y, test_size=0.2, random_state=r_state
    )
    
    # 2. Creiamo lo scaler e facciamo il "fit" SOLO sul training set
    scaler_corr = StandardScaler()
    X_train_corr_scaled = scaler_corr.fit_transform(X_train_corr) # Impara solo dal train
    
    # 3. Trasformiamo il test set usando SOLO le regole imparate dal train
    X_test_corr_scaled = scaler_corr.transform(X_test_corr) # Non impara dal test!
    
    # Addestriamo il modello KNN e calcoliamo l'accuratezza corretta
    knn_corr = KNeighborsClassifier()
    knn_corr.fit(X_train_corr_scaled, y_train_corr)
    y_pred_corr = knn_corr.predict(X_test_corr_scaled)
    accuratezze_corrette.append(accuracy_score(y_test_corr, y_pred_corr))

# 3. Calcoliamo la media delle accuratezze ottenute nei 10 tentativi
media_errata = np.mean(accuratezze_sbagliate)
media_corretta = np.mean(accuratezze_corrette)

# Stampiamo i risultati finali per il confronto
print(f"Media accuratezza (MODO SBAGLIATO con Data Leakage): {media_errata:.4f}")
print(f"Media accuratezza (MODO CORRETTO): {media_corretta:.4f}")


