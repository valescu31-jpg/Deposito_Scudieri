import pandas as pd

import numpy as np

# ==========================================
# 1. CREAZIONE DEL DATAFRAME DI PARTENZA
# ==========================================
# Definiamo un dizionario contenente dati grezzi che includono:
# - Valori duplicati (es. le righe complete di 'Bob' e 'Carla' compaiono due volte)
# - Valori mancanti (None nella colonna 'Nome' e np.nan nella colonna 'Età')
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}

# Convertiamo il dizionario in un oggetto DataFrame di Pandas
df = pd.DataFrame(data)

# Visualizziamo a schermo il DataFrame così come è stato creato
print("=== DataFrame Originale ===")
print(df)
print("\n" + "="*40 + "\n")


# ==========================================
# 2. PULIZIA DEI DATI: RIMOZIONE DUPLICATI
# ==========================================
# Il metodo .drop_duplicates() analizza tutte le colonne del DataFrame
# e rimuove le righe che sono esattamente identiche ad altre già incontrate.
df = df.drop_duplicates()


# ==========================================
# 3. GESTIONE DEI DATI MANCANTI (APPROCCIO A: ELIMINAZIONE)
# ==========================================
# Creiamo un nuovo DataFrame (df_cleaned) applicando il metodo .dropna().
# .dropna() rimuove interamente qualsiasi riga che contenga almeno un 
# valore mancante (NaN o None).
df_cleaned = df.dropna()

# Stampiamo il risultato dopo l'eliminazione delle righe incomplete
print("=== DataFrame dopo la pulizia (con .dropna()) ===")
print("Nota: Le righe con valori mancanti o i duplicati rimasti sono stati eliminati.")
print(df_cleaned)
print("\n" + "="*40 + "\n")


# ==========================================
# 4. GESTIONE DEI DATI MANCANTI (APPROCCIO B: SOSTITUZIONE / IMPUTAZIONE)
# ==========================================
# Invece di buttare via intere righe, possiamo scegliere di riempire 
# i valori mancanti (NaN) con un valore stimato, come ad esempio la media.

# Calcoliamo la media della colonna 'Età' (Pandas ignora automaticamente i valori NaN nel calcolo)
media_eta = df['Età'].mean()
print(f"-> Info: La media calcolata dell'Età è {media_eta:.2f}\n")

# Sostituiamo i valori mancanti (NaN) nella colonna 'Età' usando il metodo .fillna().
# Nelle versioni recenti di Pandas, il modo raccomandato è riassegnare il risultato:
df['Età'] = df['Età'].fillna(media_eta)

# Nota storica sulle vecchie versioni di Pandas:
# Nelle versioni passate si usava l'argomento in-place:
# df['Età'].fillna(media_eta, inplace=True)


# ==========================================
# 5. STAMPA FINALE DEL DATAFRAME MODIFICATO
# ==========================================
# Stampiamo il DataFrame principale in cui i valori mancanti dell'Età 
# sono stati correttamente rimpiazzati dalla media precedentemente calcolata.
print("=== DataFrame con dati mancanti sostituiti (.fillna()) ===")
print(df)