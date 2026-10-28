#Obiettivo: su load_digits() addestra un KNN con k = 1 e calcola l'accuratezza su training e test (split 75/25). 
# Il modello è in overfitting? Motiva guardando i due numeri.



from sklearn.datasets import make_circles
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. Caricamento e preparazione dei dati
digits = load_digits()                                    # Carica il dataset in memoria
X, y = digits.data, digits.target                         # Corretto: assegniamo a X e y (coerenti con il resto del codice)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

# Addestramento KNN con k = 1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# Calcolo accuratezza
train_accuracy = knn.score(X_train, y_train)
test_accuracy = knn.score(X_test, y_test)

print(f"Accuratezza Training: {train_accuracy * 100:.2f}%")
print(f"Accuratezza Test: {test_accuracy * 100:.2f}%")




print("=====================MEDIO==============================")

#Obiettivo: su make_circles(n_samples=500, noise=0.25, factor=0.5, random_state=0)
#  crea una divisione 60/20/20 in training/validation/test, 
# scegli il miglior k tra 1 e 50 sul validation set e riporta l'accuratezza finale sul test.


X, y = make_circles(n_samples=500, noise=0.25, factor=0.5,  random_state=0) ## dati con molto rumore #factor segna disatnza tra i cerchi concentrici

#divisione 60/20/20; PRIMO SPLIT
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #Prende il dataset completo (X e y) e lo divide in due gruppi:

                                                                                        #Il 20% viene isolato e salvato come Test Set (X_test, y_test). Questo set verrà blindato e usato solo alla fine per valutare le performance finali del modello su dati mai visti.

                                                                                        #Il restante 80% viene temporaneamente salvato in X_temp e y_temp. Questo blocco contiene sia i dati per l'addestramento che quelli per la validazione.

#divisione 60/20/20; SECONDO SPLIT
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42) #Prende l'80% dei dati rimasti (X_temp, y_temp) e li divide a sua volta in due:

                                                                                                    #Assegna il 25% di questo sottoinsieme al Validation Set (X_val, y_val), usato durante l'addestramento per regolare gli iperparametri e monitorare l'overfitting.

                                                                                                    #Il restante 75% del sottoinsieme diventa il Training Set effettivo (X_train, y_train), usato per addestrare il modello.


#Perché la percentuale finale è 60 / 20 / 20?Matematicamente, 
# applicare un test_size=0.25 sul restante 80% significa:
# Validation= 25% di 80%= 0.25 x 0.80= 20% del totale;
#Training= restante 75% di 80%= 0.75 x 0.80= 60% del totale;
#Test= primo split ha isolato il 20%

# Ricerca del miglior k tra 1 e 50 sul validation set

migliore_k=1
migliore_val=0.0

for k in range(1, 51, 2 ):                                   # k da 1 a 50
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    val = knn.score(X_val, y_val)                           # la scelta si fa sul VALIDATION
    if val > migliore_val:
        migliore_k, migliore_val = k, val

print(f"Miglior k sul Validation Set: {migliore_k} (Accuratezza Val: {migliore_val * 100:.2f}%)")


# 4. Valutazione finale sul Test Set con il k ottimale
best_knn = KNeighborsClassifier(n_neighbors=migliore_k)
best_knn.fit(X_train, y_train)
test_accuracy = best_knn.score(X_test, y_test)

print(f"Accuratezza finale sul Test Set (con k={migliore_k}): {test_accuracy * 100:.2f}%")




