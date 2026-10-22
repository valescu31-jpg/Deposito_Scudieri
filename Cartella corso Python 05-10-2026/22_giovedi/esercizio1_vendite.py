import pandas as pd

df_scv_vendite= pd.read_csv("Cartella corso Python 05-10-2026/22_giovedi/dataset_vendite.csv") #trasfarm file csv in un dataframe




# Creazione della tabella pivot

pivot_df = df_scv_vendite.pivot_table(values='Vendite_EUR', index='Prodotto', columns='Città', aggfunc='mean')  #values='Vendite_EUR': La metrica numerica su cui viene fatto il calcolo (l'importo delle vendite).

                                                                                                            #index='Prodotto': Le righe della tabella finale, che corrisponderanno ai tre prodotti presenti nel dataset (es. Laptop, Smartphone, Cuffie).

                                                                                                            #columns='Città': Le colonne della tabella finale, che corrisponderanno alle tre città (es. Milano, Roma, Napoli).

                                                                                                            #aggfunc='mean': La funzione di aggregazione applicata, ovvero la media.

print(pivot_df)


print("Utilizzo group by")
#groupby su vendite

vendite_totali = df_scv_vendite.groupby('Città')['Vendite_EUR'].sum().reset_index   #per le vendite totali nelle citta' , bsasta prendere la colonna di partenza 'citta' racchiusa in una parentesi tonda e poi applicarla alle vendite racchiusein quadre
                                                                                    #.sum()Funzionalità: funzione di aggregazione. Utilizzo: calcola la somma aritmetica di tutti i valori di vendita all'interno di ciascun gruppo.
                                                                                    ## (.reset_index) Funzionalità: riconverte il risultato. Utilizzo: trasforma la Series risultante in un nuovo DataFrame pulito, rendendo l'indice nuovamente numerico e sequenziale.
print("le vendite totali sono:")
print(vendite_totali)


