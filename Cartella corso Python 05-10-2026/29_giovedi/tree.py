# Descrizione dell'obiettivo dello script: 
# addestrare un albero di decisione e visualizzarne le regole logiche in formato testo.
#Cosa mostra: addestrare un albero e leggerne le regole in formato testo.

# Importa la funzione per caricare il dataset di esempio 'Iris' (fiori) da scikit-learn
from sklearn.datasets import load_iris

# Importa l'algoritmo di classificazione ad albero di decisione (DecisionTreeClassifier) 
# e la funzione export_text per stampare le regole decisionali in formato testuale
from sklearn.tree import DecisionTreeClassifier, export_text

# Carica il dataset Iris in una variabile; l'oggetto contiene dati, etichette e metadati
iris = load_iris()

# Inizializza il modello di classificazione ad albero:
# - max_depth=2: limita l'albero a un massimo di 2 livelli di profondità (2 domande in sequenza)
# - random_state=42: fissa il generatore casuale per garantire risultati riproducibili a ogni esecuzione
albero = DecisionTreeClassifier(max_depth=2, random_state=42)   

# Addestra (fit) l'albero sui dati storici:
# - iris.data: la matrice con le caratteristiche numeriche dei fiori (es. lunghezza sepalo/petalo)
# - iris.target: l'etichetta corretta associata a ciascun fiore (la classe della specie)
albero.fit(iris.data, iris.target)

# Genera e stampa la rappresentazione testuale delle regole apprese dall'albero:
# - export_text trasforma la struttura dell'albero in un diagramma testuale ad-hoc
# - feature_names=iris.feature_names sostituisce gli indici numerici con i nomi reali delle caratteristiche
print(export_text(albero, feature_names=iris.feature_names))     

# Esegue una previsione su un nuovo campione di dati non visti dal modello:
# 1. albero.predict([[5.0, 3.0, 4.8, 1.5]]) restituisce l'indice numerico della classe predetta (es. 0, 1 o 2)
# 2. iris.target_names[...] mappa l'indice numerico nel nome testuale della specie di fiore
# 3. Stampa a schermo la stringa descrittiva con il risultato della predizione
print("Predizione:", iris.target_names[albero.predict([[5.0, 3.0, 4.8, 1.5]])])