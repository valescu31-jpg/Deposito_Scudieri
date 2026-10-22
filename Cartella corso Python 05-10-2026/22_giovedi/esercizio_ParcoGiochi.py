import matplotlib.pyplot as pl
import pandas as pd



#=======================================
  #CREAZIOME DATAFRAME DI PANDAS
#=====================================
df_scv_parco_giochi= pd.read_csv("Cartella corso Python 05-10-2026/22_giovedi/dataset_ParcoGiochi.csv", parse_dates=["Data"], index_col="Data")# parse_dates=['Data']: dice a Pandas di leggere la colonna 'Data' come date vere.
                                                                                                                                                # - index_col='Data': imposta la colonna 'Data' come indice (le etichette delle righe).

# TRCCO DI SICUREZZA: Forziamo l'indice a diventare una data vera al 100%
df_scv_parco_giochi.index = pd.to_datetime(df_scv_parco_giochi.index)

# PASSO 3: ANALISI DEI DATI (MEDIE E DEVIAZIONE STANDARD MENSILE)

media_mensile= df_scv_parco_giochi['Visitatori'].groupby(df_scv_parco_giochi.index.month).mean()

dev_std_mensile= df_scv_parco_giochi['Visitatori'].groupby(df_scv_parco_giochi.index.month).std()


print("--- MEDIA MENSILE VISITATORI (per mese dall'1 al 12) ---")
print(media_mensile)
print("\n--- DEVIAZIONE STANDARD MENSILE ---")
print(dev_std_mensile)
