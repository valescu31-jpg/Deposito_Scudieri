import pandas as pd

import numpy as np


df_scv_nintendo= pd.read_csv("Cartella corso Python 05-10-2026/21_mercoledi/Esercizio_giochi_dataset.csv") #trasfarm filer csv in un dataframe

print(df_scv_nintendo)


# ==========================================
# 2. PULIZIA DEI DATI: RIMOZIONE DUPLICATI
# ==========================================
# Il metodo .drop_duplicates() analizza tutte le colonne del DataFrame
# e rimuove le righe che sono esattamente identiche ad altre già incontrate.
df_scv_nintendo = df_scv_nintendo.drop_duplicates()
df_scv_nintendo_cleaned = df_scv_nintendo.dropna()


# =====================================================================
# SCELTA LOGICA 3: Conversione dell'ESRB Rating in numeri
# Metodi usati: un dizionario di mappatura, .map() e .fillna()
# Pensiero logico: La colonna "esrb_rating" contiene lettere (es. 'E', 'T'). 
# La matematica non si può fare con le lettere, quindi la scelta logica 
# è tradurle in numeri usando un dizionario e il metodo .map(). 
# Se per caso c'è un valore strano o vuoto avanzato, usiamo .fillna(1) 
# per metterci un valore di sicurezza ed evitare che il programma crashi.
# =====================================================================
mappa_esrb = {'E': 1, 'E10+': 2, 'T': 3, 'RP': 1}
df_scv_nintendo['esrb_numerico'] = df_scv_nintendo['esrb_rating'].map(mappa_esrb).fillna(1)


# =====================================================================
# SCELTA LOGICA 4: Creazione della colonna "voto_utente" con numeri randomici
# Metodi usati: np.random.randint() e np.random.seed()
# Pensiero logico: L'esercizio chiede di generare voti randomici. 
# Usiamo NumPy con `np.random.randint(1, 11)` per creare numeri interi da 1 a 10 
# per ogni riga rimasta. Usiamo anche `np.random.seed(42)`: questo serve a 
# "bloccare" la casualità in modo che i numeri casuali siano sempre gli stessi 
# ogni volta che avvii il codice, così puoi fare i tuoi test senza sorprese.
# =====================================================================
np.random.seed(42)
df_scv_nintendo["voto_utente"] = np.random.randint(1, 11, size=len(df_scv_nintendo))
print(" ")


# =====================================================================
# SCELTA LOGICA 5: Moltiplicazione tra voto utente e rating ESRB
# Operatore usato: il segno di moltiplicazione matematica (*)
# Pensiero logico: Per soddisfare la richiesta, creiamo una nuova colonna 
# moltiplicando direttamente l'intera colonna "voto_utente" per la colonna 
# "esrb_numerico". Pandas esegue questa operazione riga per riga in automatico.
# =====================================================================
df_scv_nintendo["risultato_moltiplicazione"] = df_scv_nintendo["voto_utente"] * df_scv_nintendo["esrb_numerico"]
print("")

# =====================================================================
# SCELTA LOGICA 6: Creazione della colonna "goty" per il valore più alto
# Metodi usati: np.where() e .max()
# Pensiero logico: L'obiettivo finale è dare il "goty" (scrivendo "Sì") solo 
# al valore più alto uscito dalla moltiplicazione. Per farlo, troviamo il numero 
# massimo di tutta la colonna con `.max()`. Poi usiamo `np.where()` che dice: 
# "Se il valore di questa riga è uguale al massimo, scrivi 'Sì', altrimenti 'No'".
# =====================================================================

df_scv_nintendo["goty"] = np.where(
    df_scv_nintendo["risultato_moltiplicazione"] == df_scv_nintendo["risultato_moltiplicazione"].max(), 
    "Sì", 
    "No")

# 7. Stampiamo il risultato finale
print(df_scv_nintendo)


# 7. FILTRO DI CONTROLLO: Stampiamo SOLO il gioco (o i giochi) che ha vinto il GOTY!
gioco_vincitore = df_scv_nintendo[df_scv_nintendo["goty"] == "Si"]
print(gioco_vincitore[[ "voto_utente", "esrb_numerico", "risultato_moltiplicazione", "goty"]])