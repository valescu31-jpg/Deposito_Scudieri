
 #Obiettivo: su load_breast_cancer() confronta l'accuratezza di test di un KNN (k=5) con: 
 # nessuno scaling, StandardScaler, MinMaxScaler, RobustScaler. 
 # Ripeti lo stesso confronto con un DecisionTreeClassifier(random_state=0) 
 # e spiega perché per l'albero i risultati non cambiano.




# Importiamo le librerie necessarie per lavorare con i dati, 
# creare i modelli di machine learning e misurare l'accuratezza.
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# ==========================================
# PASSO 1: Caricamento e preparazione dei dati
# ==========================================

# Carichiamo il dataset del tumore al seno di esempio di scikit-learn
dati = load_breast_cancer()

# Assegniamo le caratteristiche (numeri misurati sui campioni) a X
X = dati.data     

# Assegniamo le etichette (0 = tumore maligno, 1 = tumore benigno) a y
y = dati.target   

# Dividiamo i dati in due gruppi: 
# - Training set (80%): serve al modello per imparare
# - Test set (20%): serve al modello per essere testato su dati che non ha mai visto
# random_state=0 serve a bloccare la casualità in modo che la divisione sia sempre uguale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# ==========================================
# PASSO 2: Definizione dei diversi tipi di Scaling
# ==========================================

# Creiamo un dizionario per provare facilmente i diversi metodi:
# 1. Nessuno scaling: i dati restano così come sono, con le loro scale originali.
# 2. StandardScaler: trasforma i dati centrando la media a 0 e la deviazione standard a 1 (sensibile agli outlier/valori estremi).
# 3. MinMaxScaler: sposta tutti i valori in un intervallo compreso tra 0 e 1.
# 4. RobustScaler: usa la mediana e l'intervallo interquartile(diffusione della metà centrale dei tuoi dati.), ed è perfetto se ci sono valori anomali (outlier) perché non si fa spaventare da essi.
scalers = {
    "Nessuno scaling": None,
    "StandardScaler": StandardScaler(),
    "MinMaxScaler": MinMaxScaler(),
    "RobustScaler": RobustScaler()
}



# Ciclo principale: scorre il dizionario 'scalers' prendendo la chiave (il nome testuale dello scaler) 
# e il valore (l'oggetto dello scaler vero e proprio, oppure None per il caso senza modifiche)
for nome, scaler in scalers.items():
    
    # Controllo condizionale: se lo scaler è None (cioè siamo nel giro "Nessuno scaling"), 
    # evitiamo di applicare formule e passiamo direttamente i dati originali grezzi
    if scaler is None:
        X_train_scaled = X_train
        X_test_scaled = X_test
    else:
        # Se invece lo scaler esiste, usiamo 'fit_transform' sul training set per calcolare 
        # le regole statistiche (es. media/varianza) e applicarle subito
        X_train_scaled = scaler.fit_transform(X_train)
        
        # Sul test set usiamo SOLO 'transform' per applicare le STESSE identiche regole 
        # calcolate prima sul train, evitando di imbrogliare (data leakage)
        X_test_scaled = scaler.transform(X_test)
    
    # Inizializziamo il primo modello di classificazione (es. KNN con 5 vicini)
    knn = KNeighborsClassifier(n_neighbors=5)
    
    # Addestriamo il modello passando i dati attuali (che siano scalati o originali)
    knn.fit(X_train_scaled, y_train)
    
    # Facciamo fare le previsioni sul test set e calcoliamo l'accuratezza confrontandole con la realtà (y_test)
    acc_knn = accuracy_score(y_test, knn.predict(X_test_scaled))
    
    # Inizializziamo il secondo modello (es. Decision Tree con random_state fisso per risultati stabili)
    tree = DecisionTreeClassifier(random_state=0)
    
    # Addestriamo il secondo modello usando gli STESSI identici dati preparati in questo giro del ciclo
    tree.fit(X_train_scaled, y_train)
    
    # Calcoliamo l'accuratezza anche per questo secondo modello
    acc_tree = accuracy_score(y_test, tree.predict(X_test_scaled))
    
    # Stampiamo a schermo il nome dello scaling che stiamo testando in questo momento
    print(f"Scaling: {nome}")
    
    # Stampiamo il risultato numerico ottenuto dal KNN
    print(f" -> Accuratezza KNN: {acc_knn:.4f}")
    
    # Stampiamo il risultato numerico ottenuto dal Decision Tree sullo stesso blocco di dati
    print(f" -> Accuratezza Decision Tree: {acc_tree:.4f}\n")