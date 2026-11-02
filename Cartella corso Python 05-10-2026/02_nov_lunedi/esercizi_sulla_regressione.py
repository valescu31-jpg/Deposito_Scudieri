#Obiettivo: con i dati temperatura = [18, 21, 24, 27, 30, 33] e gelati_venduti = [120, 150, 190, 230, 260, 310],
#  addestra una regressione lineare, stampa coefficiente e intercetta e scrivi in italiano cosa significa il coefficiente.
#  Prevedi le vendite a 29 °C.


import numpy as np
from sklearn.linear_model import LinearRegression

temperatura = np.array ([[18], [21], [24], [27], [30], [33]])

gelati_venduti = np.array ([[120], [150], [190], [230], [260], [310]])

# Addestramento del modello
modello = LinearRegression().fit(temperatura, gelati_venduti)

# Salvataggio di w e b in variabili per comodità
w = modello.coef_[0][0]
b = modello.intercept_[0]

# Stampa coefficiente e intercetta
print("Coefficiente w:", round(w, 2))
print("Intercetta b:", round(b, 2))

# Spiegazione del coefficiente in italiano (come richiesto)
print("\n--- Significato del coefficiente ---")
print(f"Il coefficiente w = {round(w, 2)} indica che, per ogni aumento di 1 °C della temperatura, "
      f"ci si attende un incremento medio di circa {round(w, 2)} gelati venduti.")

# Previsione a 29 °C
previsione = modello.predict([[29]])[0][0]
print("\nPrevisione vendite 29 °C:", round(previsione))

