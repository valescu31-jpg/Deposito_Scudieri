import pandas as pd



# ==========================================
# 1. CREAZIONE DEL DATAFRAME DI PARTENZA
# ==========================================



data = {
    'Nome': ['Marco De Luca', 'Alessandro Costa', 'Davide Gallo', 'Giulia Rossi', 'Luca Bianchi', 'Sofia Romano', 'Matteo Ferrari', 'Francesca Esposito'],
    'Età': [50, 59, 57, 34, 42, 28, 45, 38],
    'Città': ['Firenze', 'Verona', 'Verona', 'Milano', 'Roma', 'Napoli', 'Torino', 'Bologna'],
    'Salario (€)': [55400, 60100, 59800, 35000, 42000, 28500, 48000, 39000]
}

# Convertiamo il dizionario in un oggetto DataFrame di Pandas
df = pd.DataFrame(data)

#viasualizazzione righe

print("visualizazzione prime 5 righe")

print(df.head()) #mod per visualizzare le prime 5 righe sfruttandolo metodo head 


print("visualizazzione ultime 5 righe") 

print(df.tail()) #mod per visualizzare le ultime 5 righe sfruttandolo metodo tail 


#visualizazzione del tipo di dato di ciascuna colonna
print("Visualizazzione dei tipi di dati di ciascuna colonna")
print(df.info()) #visualizazzione dei Tipi di dati 


print("calcolo statistiche descrittive : media, mediana e deviazione")
# Calcoliamo la media e la deviazionr della colonna 'Età' (Pandas ignora automaticamente i valori NaN nel calcolo)
print("MEDIA, DEVIAZIONE DI ETA")
media_eta = df['Età'].mean() #modo similare all'sql per la media al livello strutturale, richiamando il nome della tabella con metodo
print(f"-> Info: La media calcolata dell'Età è {media_eta:.2f}\n") #modo per stampare 
deviazione_eta = df['Età'].std()
print(f"-> Info: La deviazione calcolata dell'Età è {deviazione_eta:.2f}\n")

print("MEDIA, DEVIAZIONE DI SALARIO")
media_salario = df['Salario (€)'].mean()
print(f"-> Info: La media calcolata dell'Età è {media_salario:.2f}\n")
deviazione_salario = df['Salario (€)'].std()
print(f"-> Info: La deviazione calcolata del Salario è {deviazione_salario:.2f}\n")


print("MEDIANA")

mediana_eta= df['Età'].median()
print(f"-> Info: Il valore mediano calcolata dell'Età è {mediana_eta:.2f}\n")

mediana_salario= df['Salario (€)'].median()
print(f"-> Info: Il valore mediano  dell'Salario è {mediana_salario:.2f}\n")


print("MEDIA TOTALE") #La mediana, guardando solo la posizione centrale, non si fa influenzare dai valori estremi o sproporzionati, risultando spesso un indicatore molto più affidabile per descrivere la "realtà tipica" di un gruppo (come nel caso dei salari o dei prezzi delle case).

media_totale= df.mean(numeric_only= True) #struttura preimpostata di python per poter far la media totale delle informazioni (escludendo Citta e Nome)
print(media_totale)