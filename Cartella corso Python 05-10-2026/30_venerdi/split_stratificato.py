#Obiettivo: su load_digits() addestra un DecisionTreeClassifier(max_depth=8) con split stratificato. 
# Stampa il classification_report, disegna la matrice di confusione con ConfusionMatrixDisplay 
# e individua le due cifre confuse più spesso tra loro.

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np


# 1. Carichiamo i dati delle cifre scritte a mano
dati = load_digits()
X, y = dati.data, dati.target

# 2. Dividiamo i dati in modo stratificato (80% allenamento, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# 3. Creiamo e alleniamo l'Albero Decisionale con profondità massima 8
modello = DecisionTreeClassifier(max_depth=8, random_state=42)
modello.fit(X_train, y_train)

# 4. Facciamo fare le previsioni sui dati di test
y_pred = modello.predict(X_test)

#CREAZIONE E ADDESTRAMENTO DEL MODELLO (DecisionTreeClassifier)
# Creiamo il nostro albero decisionale. 'max_depth=8' significa che per riconoscere 
# un numero il computer può fare una serie di massimo 8 domande a bivio consecutive 
# (es. "Il pixel centrale è scuro?" -> Sì -> "E quello in basso a destra?" -> No...).
modello = DecisionTreeClassifier(
    max_depth=8,         # Limite massimo di 8 livelli di domande
    random_state=42
)

# Il comando '.fit()' è il momento in cui il computer "studia" intensamente 
# usando le immagini e le risposte corrette del blocco di allenamento.
modello.fit(X_train, y_train)

# 5. PREVISIONE SUI DATI DI TEST (L'esame)
# Ora diamo al computer le immagini del test (X_test) ma *senza* dirgli che numeri sono.
# Lui compila il suo foglio di risposte stimate chiamate 'y_pred'.
y_pred = modello.predict(X_test)

# 6. STAMPA DEL REPORT DI CLASSIFICAZIONE (classification_report)
# Questo comando stampa una "pagella" dettagliata. Ci mostra quanto è preciso 
# e accurato il modello nel riconoscere ogni singola cifra da 0 a 9.
print("=== 1. CLASSIFICATION REPORT (LA PAGELLA) ===")
print(classification_report(y_test, y_pred))

# 7. CREAZIONE DELLA MATRICE DI CONFUSIONE (ConfusionMatrixDisplay)
# La matrice di confusione è una tabella a griglia:
# - Sulle righe ci sono i numeri REALI.
# - Sulle colonne ci sono i numeri INDOVINATI dal computer.
# I numeri sulla diagonale principale sono le risposte giuste (vero = predetto).
# I numeri FUORI dalla diagonale sono gli errori commessi dal computer.
fig, ax = plt.subplots(figsize=(8, 8))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, 
    ax=ax, 
    cmap=plt.cm.Blues,   # Sfumatura di blu per leggere meglio le quantità
    colorbar=False
)
plt.title("Matrice di Confusione (Dove sbaglia il modello?)")
plt.show()

# 8. INDIVIDUAZIONE DELLE DUE CIFRE PIÙ CONFUSE TRA LORO
# Logica passo-passo per trovare la coppia di numeri scambiata più spesso:
# A) Calcoliamo i numeri della matrice di confusione pura.
cm = confusion_matrix(y_test, y_pred)

# B) Mettiamo a zero la diagonale principale (perché le risposte corrette non sono errori di confusione).
np.fill_diagonal(cm, 0)

# C) Troviamo la posizione (riga e colonna) con il valore più alto rimasto nella tabella.
riga_vera, colonna_predetta = np.unravel_index(cm.argmax(), cm.shape)
numero_errori = cm[riga_vera, colonna_predetta]

print("\n=== 2. ANALISI DEGLI ERRORI ===")
print(f"Le due cifre confuse più spesso tra loro sono:")
print(f"La cifra reale '{riga_vera}' scambiata erroneamente per '{colonna_predetta}' ben {numero_errori} volte.")

