#Obiettivo: su load_wine() disegna la curva di accuratezza training/test al variare di k (da 1 a 60). Poi ripeti lo split con 5 valori diversi di random_state e disegna le 5 curve di test sullo stesso grafico:
#  quanto cambia la stima?
#  Scrivi tre righe su cosa implica questo per l'affidabilità di un singolo split (anticipazione della cross-validation).


import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


wines = load_wine()                                    # Carica il dataset in memoria
X, y = wines.data, wines.target

k_range= range(1, 61)

#Curva di accuratezza training/test per un singolo split (random_state=42)

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42)

# Liste vuote per memorizzare i punteggi di accuratezza per ogni k

train_acc=[]
test_acc= []

#Ciclo su ogni valore di k
for k in k_range:
    # Inizializzazione del classificatore KNN con k vicini
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Addestramento del modello sui dati di training
    knn.fit(X_train, y_train)
    
    # Calcolo e salvataggio dell'accuratezza sul training set
    train_acc.append(knn.score(X_train, y_train))
    
    # Calcolo e salvataggio dell'accuratezza sul test set
    test_acc.append(knn.score(X_test, y_test))



#RIPETIZIONE CON 5 RANDOM_STATE

# Definizione di 5 diversi semi casuali per lo split dei dati
random_states=[10, 33, 44, 55, 89] 
test_acc_collettiva= [] # Lista per raccogliere i risultati di tutti i test

# Ciclo su ogni valore di random_state

for rs in random_states: 
    # Esegue un nuovo split del dataset usando il random_state corrente
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=rs)

accuratezze=[]
    # Per ogni split, calcola l'accuratezza sul test set al variare di k
for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        accuratezze.append(knn.score(X_test, y_test))





#CREAZIONE GRAFICO


plt.figure(figsize=(9, 5))               # Dimensione della finestra del grafico


#Per ogni random_state, calcoliamo i punti e li disegniamo
for rs in random_states:
    # Divide i dati in modo diverso ad ogni giro
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=rs)
    
    accuratezze = [] # Lista dove salviamo i punti per questo random_state
    
    # Calcola l'accuratezza per ogni valore di k
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        accuratezze.append(knn.score(X_test, y_test)) # Salva il punto Y
        
    # Disegna la linea per questo specifico random_state
    plt.plot(k_range, accuratezze, label=f'random_state = {rs}')

# 5. Personalizziamo il grafico
plt.title('Accuratezza di Test con 5 `random_state` Diversi') # Titolo in alto
plt.xlabel('Valore di k')                                    # Testo asse X (in basso)
plt.ylabel('Accuratezza')                                    # Testo asse Y (a sinistra)
plt.legend()                                                 # Legenda per i 5 colori
plt.grid(True)                                               # Attiva i quadretti di sfondo

# 6. Mostra il grafico finale
plt.show()                                                   # Apri la finestra del grafico