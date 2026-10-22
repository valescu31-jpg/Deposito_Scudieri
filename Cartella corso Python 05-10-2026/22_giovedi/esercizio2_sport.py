import pandas as pd

print("Iscritti:")

df_scv_iscritti= pd.read_csv("Cartella corso Python 05-10-2026/22_giovedi/dataset_sport_dati_anagrafici.csv")

print(df_scv_iscritti.head()) #mod per visuaizzare le prime 5 righe

print(df_scv_iscritti.tail()) #mod per visualizzare le ultime 5 righe sfruttandolo metodo tail

print("pulizia dati:")

df_scv_iscritti = df_scv_iscritti.drop_duplicates() # Il metodo .drop_duplicates() analizza tutte le colonne del DataFrame
                                                    # e rimuove le righe che sono esattamente identiche ad altre già incontrate.

df_scv_iscritti_cleaned = df_scv_iscritti.fillna(0)  #sfruttare fillna() riempie gli spazi vuoti con na

print(df_scv_iscritti)

#  Aggiungere una nuova colonna 

df_scv_iscritti["Tipo_abbonamento"] = ["Base", "Premium", "Family", "Diamond", "Vip", "Avanzato", "Deluxe", "Pappa", "Pippo"]



print("Presenze:")

df_scv_presenze=pd.read_csv("Cartella corso Python 05-10-2026/22_giovedi/dataset_sport_registro.csv")

print(df_scv_presenze.head()) #mod per visuaizzare le prime 5 righe

print(df_scv_presenze.tail()) #mod per visualizzare le ultime 5 righe sfruttandolo metodo tail


#  Aggiungere una nuova colonna 

df_scv_iscritti["Yoga"]
df_scv_iscritti["Crossfit"]
df_scv_iscritti["Pilates"]
