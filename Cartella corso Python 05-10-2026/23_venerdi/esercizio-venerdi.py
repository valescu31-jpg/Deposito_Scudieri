import pandas as pd
import matplotlib.pyplot as plt

df_scv_CandyData= pd.read_csv("Cartella corso Python 05-10-2026/23_venerdi/candy-data.csv") #creazione del dataframe con importazione del file da cui prenderemo i dati delle candy



df_scv_CandyVendite= pd.read_csv("Cartella corso Python 05-10-2026/23_venerdi/candy-vendite.csv") #creazione del dataframe con importazione del file da cui prenderemo i dati delle vendite delle candy


# ==========================================
# 2. PULIZIA DEI DATI: RIMOZIONE DUPLICATI
# ==========================================
# Il metodo .drop_duplicates() analizza tutte le colonne del DataFrame
# e rimuove le righe che sono esattamente identiche ad altre già incontrate.
df_scv_CandyData_duplicati = df_scv_CandyData.drop_duplicates()

df_scv_CandyVendite=df_scv_CandyVendite.drop_duplicates()



# ==========================================
# 3. GESTIONE DEI DATI MANCANTI (APPROCCIO A: ELIMINAZIONE)
# ==========================================
# Creiamo un nuovo DataFrame (df_cleaned) applicando il metodo .dropna().
# .dropna() rimuove interamente qualsiasi riga che contenga almeno un 
# valore mancante (NaN o None).
df_cleaned_CandyData = df_scv_CandyData.dropna() 

# 1. Pulisci completamente i nomi delle colonne rimuovendo spazi e tabulazioni nascoste
df_cleaned_CandyData.columns = df_cleaned_CandyData.columns.str.strip().str.replace(' ', '')


df_cleaned_CandyVendite = df_scv_CandyVendite.dropna()


#=========================================================
# 3.ESPLORAZIONE DEI DATI
#=========================================================
#Candydata
print(df_cleaned_CandyData.head())#stampera la prime    5 righe
print(df_cleaned_CandyData.tail()) #stampera la ultime    5 righe
print(df_cleaned_CandyData.describe()) #ci riportera dei dati numerici
print(df_cleaned_CandyData.info()) #riportera una descrizione generale di tutto il dataframe

#CandyVendite
print(df_cleaned_CandyVendite.head())
print(df_cleaned_CandyVendite.tail())
print(df_cleaned_CandyVendite.describe())
print(df_cleaned_CandyVendite.info())

#===========================================================
# 4. Analisi dei dati
#===========================================================

#Analisi dei dati delle candy
print("Valore massimo della percentuale del prezzo:")
CandyData_max_sugarpercent	=  df_cleaned_CandyData['	sugarpercent	' ].max() #modo per riprendere il valore piu alto all'interno della tabella
print(CandyData_max_sugarpercent	) 

print("Valore minimo della percentuale del prezzo:")
CandyData_min_sugarpercent	= df_cleaned_CandyData['	sugarpercent	'].min() #modo per riprendere il valore piu basso all'interno della tabella
print(CandyData_min_sugarpercent	) 

print("Valore medio della percentuale del prezzo:")
CandyData_media_sugarpercent	= df_cleaned_CandyData['	sugarpercent	'].mean() #calcolo media 
print(CandyData_media_sugarpercent	)

print("Valore mediano della percentuale del prezzo:")
CandyData_mediana_sugarpercent	= df_cleaned_CandyData['	sugarpercent	'].median()
print(CandyData_mediana_sugarpercent	)


#Analisi dei dati delle vendite delle Candy


# 1. Raggruppare Il nome dei competetor che hanno maggiore prezzo_euro,costo_unitario_euro,budget_marketing_euro
competitorname= df_cleaned_CandyVendite.groupby("competitorname")["costo_unitario_euro,budget_marketing_euro"].sum()
print(competitorname.idxmax())

# 2. Trovare la città con maggiori unita di vendite per aree di vendita 
aree_di_vendita = df_cleaned_CandyVendite.groupby("area_vendita")["unita_vendute"].sum()
print(aree_di_vendita.idxmax())


# 3. Creare un DataFrame con giacenze magazzino inferiori a 350
giacenza_magazzino = df_scv_CandyVendite[df_cleaned_CandyVendite["giacenza_magazzino"] < 350]
print(giacenza_magazzino)


# 4. Raggruppa per area di vendita e calcola la media della valutazione clienti
media_valutazioni = df_cleaned_CandyVendite.groupby('area_vendita')['valutazione_clienti'].mean().reset_index() #df.groupby('area_vendita'): Divide il dataset in gruppi separati in base a ciascuna area geografica presente nella colonna (es. Nord, Sud, Centro, Isole).

                                                                                                                #['valutazione_clienti']: Seleziona esclusivamente la colonna su cui vuoi effettuare il calcolo.

                                                                                                                #.mean(): Calcola la media aritmetica delle valutazioni per ogni singolo gruppo.

                                                                                                                #.reset_index(): Trasforma nuovamente il risultato in un formato tabulare pulito (DataFrame) facile da leggere o stampare.


print(media_valutazioni)# stampa risultato