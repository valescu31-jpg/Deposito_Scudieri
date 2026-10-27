from sklearn.neighbors import KNeighborsClassifier 
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd



#Obiettivo: crea un mini dataset di 8 animali con feature [peso_kg, altezza_cm] ed etichetta "cane" o "gatto",
#  addestra un KNeighborsClassifier(n_neighbors=3) e predici la classe di due animali nuovi a tua scelta.

print("FACILE:")

peso_KG_altezza_CM= [[5, 0.3], [6, 0.4], [2, 0.5], [4, 0.6], [6, 0.8], [7, 0.6], [8, 0.9], [9, 1]]
animale= ['gatto', 'cane', 'gatto', 'cane', 'criceto', 'cane', 'gatto', 'pantegana' ]

modello = KNeighborsClassifier(n_neighbors=3) #iperparametro
modello.fit(peso_KG_altezza_CM, animale) #addestramento

print(modello.predict([[6, 0.8], [9, 1]]))  # 3) predizione -> ['criceto' 'pantegana']
print(modello.classes_)  



print("=========================================================================")

print("MEDIO:")

#Obiettivo: su load_breast_cancer() esegui il workflow completo con test_size=0.25 e random_state=0: addestra un KNN, 
# calcola l'accuratezza sia con accuracy_score sia con score e verifica che coincidano.
#  Stampa anche n_features_in_ e classes_.

# 1. Caricamento dei dati
X, y = load_breast_cancer(return_X_y=True)                 # Carica il dataset separando subito X (la matrice delle feature) e y (il vettore target)

# 2. Divisione del dataset in train (75%) e test (25%)
X_cancer, X_test, y_cancer, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)                  # Divide i dati: 75% per l'addestramento e 25% per il test. random_state=0 garantisce che la divisione casuale sia sempre identica

# 3. Inizializzazione e Addestramento del modello KNN
modello = KNeighborsClassifier(n_neighbors=5)              # Crea il classificatore KNN impostando K=5 (il modello valuterà i 5 vicini più vicini)
modello.fit(X_cancer, y_cancer)                            # "Addestra" il modello memorizzando i dati di training (X_cancer e y_cancer)

# 4. Fase di previsione
y_pred = modello.predict(X_test)                           # Usa il modello addestrato per prevedere le etichette dei dati di test (X_test) mai visti prima

# 5. Valutazione e confronto delle metriche di accuratezza
print("accuracy_score:", accuracy_score(y_test, y_pred))   # Calcola e stampa l'accuratezza confrontando y_test e y_pred tramite la funzione esterna
print("score:         ", modello.score(X_test, y_test))    # Calcola e stampa l'accuratezza usando il metodo integrato nel modello (deve coincidere con il precedente)
print("Forme (Train, Test):", X_cancer.shape, X_test.shape) # Stampa le dimensioni (numero di righe e colonne) delle matrici di train e test

# 7. Ispezione degli attributi appresi dal modello
print("Numero di feature lette dal modello (n_features_in_):", modello.n_features_in_) # Restituisce il numero totale di colonne/feature su cui si è allenato (es. 30)
print("Classi del modello (classes_):", modello.classes_)   # Mostra l'array con le classi distinte che il modello riconosce (nel dataset breast cancer: 0 e 1)


print("======================================================================================")
print("DIFFICILE:")

#Obiettivo: su load_digits() confronta KNeighborsClassifier, DecisionTreeClassifier e RandomForestClassifier con un ciclo. 
# Poi ripeti il confronto con tre valori diversi di random_state nello split e stampa una tabella (DataFrame pandas) con modello × random_state. 
# La classifica dei modelli cambia?

#caricamento dataset

# 1. Caricamento e preparazione dei dati
digits = load_digits()                                    # Carica il dataset in memoria
X, y = digits.data, digits.target                         # Corretto: assegniamo a X e y (coerenti con il resto del codice)

# Esempio di split singolo iniziale (opzionale ma corretto nella sintassi)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
) 

# 2. Modelli da confrontare
modelli = {
    "KNeighbors": KNeighborsClassifier(),                 # Istanza del modello KNN
    "DecisionTree": DecisionTreeClassifier(random_state=0), # Albero decisionale
    "RandomForest": RandomForestClassifier(random_state=0)# Random forest
}

# 3. Configurazione dei parametri e della struttura dati per i risultati
random_states = [10, 42, 99]                              # Lista dei diversi valori di random_state da testare

# Inizializziamo il dizionario dei risultati in modo corretto (chiavi basate sui nomi dei modelli)
risultati = {
    "KNeighbors": {},
    "DecisionTree": {},
    "RandomForest": {}
}

# 4. Cicli di addestramento e valutazione per ogni random_state
for rs in random_states:
    # Suddivide il dataset con il seed corrente (rs) e test_size al 20%
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=rs
    )
    
    # Per ogni modello nel dizionario, addestra e calcola l'accuratezza
    for nome, modello in modelli.items():
        modelli[nome].fit(X_train, y_train)                # Addestra il modello sui dati correnti
        y_pred = modelli[nome].predict(X_test)             # Predice i valori sul test set
        acc = accuracy_score(y_test, y_pred)               # Calcola l'accuratezza

        risultati[nome][rs] = acc                          # Salva il risultato nel dizionario strutturato [modello][random_state]



