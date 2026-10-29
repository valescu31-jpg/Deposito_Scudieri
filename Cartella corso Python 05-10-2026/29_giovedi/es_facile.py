# Importiamo la funzione per caricare il dataset integrato dei tumori al seno da scikit-learn
from sklearn.datasets import load_breast_cancer

# Importiamo la libreria pandas per organizzare i dati in una tabella leggibile (DataFrame)
import pandas as pd

# Importiamo il MinMaxScaler che serve a ridimensionare i dati portandoli tutti nell'intervallo tra 0 e 1
from sklearn.preprocessing import MinMaxScaler

# 1. CARICAMENTO E PREPARAZIONE DEI DATI
# Carichiamo il dataset grezzo (che è un dizionario)
dataset = load_breast_cancer()

# Convertiamo i dati numerici in un DataFrame Pandas, usando i nomi delle feature come intestazioni delle colonne
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# 2. STAMPA DI MINIMO E MASSIMO (E ANALISI DELLE SCALE)
# Stampiamo le statistiche descrittive del DataFrame per visualizzare il minimo ('min') e il massimo ('max') di ogni feature
print("--- 1. STATISTICHE INIZIALI (MIN E MAX) ---")
print(df.describe().loc[['min', 'max']])

# SPIZZATA LOGICA SULLE SCALE:
# Osservando l'output di describe(), notiamo che le feature hanno scale completamente diverse:
# - La feature con la scala PIÙ GRANDE è 'mean area' (ha valori che arrivano a migliaia, es. ~2500).
# - La feature con la scala PIÙ PICCOLA è 'mean smoothness' o gli 'error' (hanno valori decimali vicini a 0, es. 0.001).
# Senza scaling, l'algoritmo di Machine Learning darebbe molta più importanza a 'mean area' solo perché i numeri sono più grandi!

# 3. APPLICAZIONE DEL MINMAXSCALER
# Creiamo l'oggetto MinMaxScaler (la formula matematica che trasforma ogni valore in base a min e max: (x - min) / (max - min))
scaler = MinMaxScaler()

# Applichiamo il calcolo sui nostri dati: 'fit' impara minimo e massimo di ogni colonna, 'transform' applica la formula
dati_scalati = scaler.fit_transform(df)

# Poiché il risulatato dello scaler è un array numerico di NumPy, lo riconvertiamo in DataFrame pandas per comodità
df_scalato = pd.DataFrame(dati_scalati, columns=dataset.feature_names)

# 4. VERIFICA FINALE
# Stampiamo di nuovo il minimo e il massimo dei dati scalati per dimostrare che ora tutte le feature vanno da 0 a 1
print("\n--- 2. VERIFICA FINALE DOPO MINMAXSCALER (TUTTO DA 0 A 1) ---")
print(df_scalato.describe().loc[['min', 'max']])