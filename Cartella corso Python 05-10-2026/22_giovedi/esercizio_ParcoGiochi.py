import matplotlib.pyplot as pl
import pandas as pd



#=======================================
  #CREAZIOME DATAFRAME DI PANDAS
#=====================================
df_scv_parco_giochi= pd.read_csv("Cartella corso Python 05-10-2026/22_giovedi/dataset_ParcoGiochi.csv", parse_dates=["Data"], index_col="Data")# parse_dates=['Data']: dice a Pandas di leggere la colonna 'Data' come date vere.
                                                                                                                                                # - index_col='Data': imposta la colonna 'Data' come indice (le etichette delle righe).



# PASSO 3: ANALISI DEI DATI (MEDIE E DEVIAZIONE STANDARD MENSILE)

media_mensile= df_scv_parco_giochi('Visitatori')['Data'].mean()


print("--- MEDIA MENSILE VISITATORI (per mese dall'1 al 12) ---")
print(media_mensile)
print("\n--- DEVIAZIONE STANDARD MENSILE ---")
print(dev_std_mensile)

#Avuto problemi con la  media, ho sfruttato un prompt per farmelo spiegare vedendo anche qualche passaggio, ma mi ha solo buggato, facendomi vedere robe piu difficili nonostante i miei continui filtri su esso.