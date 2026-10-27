from sklearn.neighbors import KNeighborsClassifier 
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
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

X, y = load_breast_cancer(return_X_y=True)           #importa dataset cancer                         

X_cancer, X_test, y_cancer, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)                           # 3) divisione 75(x)/25(y)


knn = KNeighborsClassifier(n_neighbors=5)
modello.fit(X_cancer, y_cancer)      #addestramento  sul training                              
y_pred = modello.predict(X_test) #pred= predizione

#accuratezza
print("accuracy_score:", accuracy_score(y_test, y_pred))            # 7) valutazione
print("score:         ", modello.score(X_test, y_test))             
print(X_cancer.shape, X_test.shape)  


print("Numero di feature lette dal modello (n_features_in_):", modello.n_features_in_)
print("Classi del modello (classes_):", modello.classes_)





