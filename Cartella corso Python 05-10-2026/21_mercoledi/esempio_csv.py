import pandas as pd

df_scv= pd.read_csv("Cartella corso Python 05-10-2026/21_mercoledi/studenti.csv")

print(df_scv)



#Aggiunta di una colonna 
df_scv["Sesso"]= ["F", "M", "F", "F", "M", "F","F", "M", "F", "M"]
print(df_scv)
print("")


#creare colonna promosso e vado a riempirla i n base al voto se e' >=6
df_scv["promosso"]= df_scv["voto"] >=6
print(df_scv)
print("")


print("stampa media:")

print(df_scv["voto"].mean)  #stampa media
print("")

print("stampa il valore massimo:")
print(df_scv["voto"].max) #stampa valore massimo
print("")


print("stampa voti maggiori di 7, richiamando il dataframe ")
print([df_scv["voto"]] > 7)
print("") #spazio tra un print e l'altro

#Salvare il Dataframe in un nuvo CSV
df_scv.to_cs("Cartella corso Python 05-10-2026/21_mercoledi/studenti_aggiornato.csv", index= False) #index falsw non salva l'indice 

