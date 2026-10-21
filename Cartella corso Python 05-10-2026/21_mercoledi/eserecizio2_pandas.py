import pandas as pd          #importo della libreria pandas 

df_scv_marvel= pd.read_csv("Cartella corso Python 05-10-2026/21_mercoledi/Marvel_Movies_Dataset (1).csv") #trasfarm filer csv in un dataframe

print(df_scv_marvel)

# ==========================================
# 2. PULIZIA DEI DATI: RIMOZIONE DUPLICATI
# ==========================================
# Il metodo .drop_duplicates() analizza tutte le colonne del DataFrame
# e rimuove le righe che sono esattamente identiche ad altre già incontrate.
df_scv_marvel = df_scv_marvel.drop_duplicates()


# 1. Creare la prima colonna aggiuntiva
df_scv_marvel['NuovaColonna1'] = None

# 2. Aggiungere una colonna con un valore fisso per tutti
df_scv_marvel['NuovaColonna2'] = 'Da verificare'

print(df_scv_marvel)



