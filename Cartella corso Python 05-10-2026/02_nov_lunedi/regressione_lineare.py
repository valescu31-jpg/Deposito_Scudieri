import numpy as np
from sklearn.linear_model import LinearRegression

metri = np.array([[40], [55], [70], [85], [100], [120]])          # X in 2D: una colonna
prezzo = np.array([140_000, 185_000, 230_000, 270_000, 320_000, 380_000])

modello = LinearRegression().fit(metri, prezzo)
print("Coefficiente w:", round(modello.coef_[0]))                # € per ogni m² in più
print("Intercetta b:", round(modello.intercept_))                 # prezzo "base" con 0 m²
print("Previsione 90 m²:", round(modello.predict([[90]])[0]))

# Verifica a mano: ŷ = w·x + b
print("A mano:", round(modello.coef_[0] * 90 + modello.intercept_))




#Intermedio
#Cosa mostra: regressione multipla sul dataset Diabetes e lettura dei coefficienti.


import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = load_diabetes(as_frame=True)
X, y = data.data, data.target                        # y = progressione della malattia dopo un anno
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = LinearRegression().fit(X_train, y_train)

coefficienti = pd.Series(modello.coef_, index=X.columns).sort_values()
print(coefficienti.round(1))                         # effetto di ogni feature
print("R² sul test:", round(modello.score(X_test, y_test), 3))   # score dei regressori = R² (modulo 3.2)