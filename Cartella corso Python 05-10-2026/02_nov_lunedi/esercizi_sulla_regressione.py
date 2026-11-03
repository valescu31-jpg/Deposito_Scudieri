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




print("INTERMEDIO:")

# Importiamo le librerie necessarie per gestire i dati, il modello e la scala
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 1. Carichiamo il dataset California Housing in formato DataFrame
housing = fetch_california_housing(as_frame=True)
X = housing.data  # Le feature (le variabili indipendenti)
y = housing.target  # Il target (il prezzo medio delle case)

# 2. Dividiamo i dati in training (80%) e test (20%) con un seed fisso per la riproducibilità
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# CASO 1: REGRESSIONE LINEARE SENZA StandardScaler
# ==========================================

# Creiamo l'oggetto del modello di regressione lineare
model_raw = LinearRegression()

# Addestriamo il modello usando i dati di training non scalati
model_raw.fit(X_train, y_train)

# Creiamo un DataFrame per abbinare ogni feature al suo coefficiente calcolato
df_coef_raw = pd.DataFrame({
    'Feature': X.columns,
    'Coefficiente': model_raw.coef_
})

# Aggiungiamo una colonna con il valore assoluto per ordinare l'importanza indipendentemente dal segno (+ o -)
df_coef_raw['Abs'] = df_coef_raw['Coefficiente'].abs()
df_coef_raw = df_coef_raw.sort_values(by='Abs', ascending=False).drop(columns='Abs')

print("--- COEFFICIENTI SENZA StandardScaler ---")
print(df_coef_raw)
print("\n" + "="*40 + "\n")

# ==========================================
# CASO 2: REGRESSIONE LINEARE CON StandardScaler
# ==========================================

# Inizializziamo lo scaler per normalizzare le variabili
scaler = StandardScaler()

# Facciamo il fit (calcolo media/deviazione standard) e il transform sul training set
X_train_scaled = scaler.fit_transform(X_train)

# Facciamo SOLO il transform sul test set (usando i parametri calcolati sul training per evitare data leakage)
X_test_scaled = scaler.transform(X_test)

# Creiamo un nuovo modello di regressione lineare
model_scaled = LinearRegression()

# Addestriamo il modello usando i dati di training scalati
model_scaled.fit(X_train_scaled, y_train)

# Creiamo un DataFrame con i coefficienti ottenuti dai dati scalati
df_coef_scaled = pd.DataFrame({
    'Feature': X.columns,
    'Coefficiente': model_scaled.coef_
})

# Ordiniamo anche questi in base al valore assoluto
df_coef_scaled['Abs'] = df_coef_scaled['Coefficiente'].abs()
df_coef_scaled = df_coef_scaled.sort_values(by='Abs', ascending=False).drop(columns='Abs')

print("--- COEFFICIENTI CON StandardScaler ---")
print(df_coef_scaled)

