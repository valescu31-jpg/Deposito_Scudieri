from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split #divide i dataset
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)                                   # 1) dati

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)                           # 3) divisione 80(x)/20(y)

modello = KNeighborsClassifier(n_neighbors=3)                       # 4) scelta del modello
modello.fit(X_train, y_train)                                       # 5) addestramento SOLO sul training
y_pred = modello.predict(X_test)                                    # 6) predizione sul test

print("accuracy_score:", accuracy_score(y_test, y_pred))            # 7) valutazione
print("score:         ", modello.score(X_test, y_test))             # stesso valore
print(X_train.shape, X_test.shape)  