from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np


#Obiettivo: carica load_breast_cancer() e stampa numero di campioni, numero di feature, i nomi delle due classi e i nomi delle prime 5 feature.

print("FACILE:")

#Obiettivo: carica load_breast_cancer() e stampa numero di campioni, numero di feature, i nomi delle due classi e i nomi delle prime 5 feature.

cancer = load_breast_cancer()                    # oggetto Bunch
# 2. Numero di campioni e numero di feature (e' binaria)
num_samples = cancer.data.shape[0]  # Numero di righe (pazienti/campioni)
num_features = cancer.data.shape[1]  # Numero di colonne (caratteristiche misurate)

print(f"Numero di campioni: {num_samples}")
print(f"Numero di feature: {num_features}")

# 3. Nomi delle due classi (target)
# Solitamente: 'malignant' (maligno) e 'benign' (benigno)
print(f"Nomi delle classi: {list(cancer.target_names)}")

# 4. Nomi delle prime 5 feature
print(f"Prime 5 feature: {list(cancer.feature_names[:5])}")


print("INTERMEDIO:")

#Obiettivo: carica load_digits(), stampa la forma di X,
#  visualizza le prime 10 immagini con plt.imshow(digits.images[i], cmap="gray") con la cifra corretta come titolo,
#  e crea un grafico a barre con il numero di campioni per ciascuna cifra.

digits = load_digits() #caricamento dataset



#Stampiamo la forma (shape) di X
# La X maiuscola rappresenta la matrice dei dati (le righe sono le immagini, le colonne sono i pixel)
print("La forma (shape) di X e':", digits.data.shape) #riprendiamo digits essenndo il dataset e data per rifornirci delle informazioni da dare a X


#Visualizziamo le prime 10 immagini
plt.figure(figsize= (12,3)) # Creiamo una finestra orizzontale per metterle tutte di fila con 12= larghezza e 3= altezza  

for i in range(10): #10 sta per il numero di immagini, i che sarebbe il contatore ogni volte che cicla crea l'immagine
# Prepariamo lo spazio per mettere le immagini una di fianco all'altra

    plt.subplot(1, 10, i+1)  #plt.subplot serve a dividere la finestra del grafico in una griglia,
                             #permettendoti di mettere più immagini o grafici tutti insieme nella stessa schermata, invece di aprirli uno alla volta.

# Disegniamo l'immagine in bianco e nero (scala di grigi)
    plt.imshow(digits.images[i], cmap= "gray")

# Mettiamo il numero corretto come titoletto sopra l'immagine
    plt.title(digits.target[i])   


#stampa tutte le 10 immagini
plt.show()


#Creiamo un grafico a barre semplice per contare i numeri
# Contiamo quanti campioni ci sono per ogni cifra da 0 a 9

#il cartellino con la risposta esatta per ogni singolo disegno.
#                            |
conteggi = np.bincount(digits.target) #np.bincount(digits.target), digits.target è l'elenco completo di tutte le risposte corrette di tutte le immagini del dataset.
                                      #Passando questo elenco a np.bincount, 
                                      # il programma conta in automatico quanti zeri ci sono, quanti uno, quanti due e così via, per poter disegnare le colonne del grafico finale.



# Disegniamo il grafico a barre
plt.bar(range(10), conteggi) #Questa riga prende i numeri da 0 a 9 e li mette in basso sull'asse orizzontale,
                             #poi guarda l'elenco dei conteggi e alza ogni singola barra all'altezza giusta in base a quanti campioni di quel numero sono presenti nel dataset!


plt.title("Quanti campioni per ogni cifra")
plt.show()









print("COMPLESSO:")


