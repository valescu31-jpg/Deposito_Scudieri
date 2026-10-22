import matplotlib.pyplot as plt
import pandas as pd

f_scv_temperatura= pd.read_csv("Cartella corso Python 05-10-2026/22_giovedi/dataset_temperatura.csv")

print("Temperatura massima:")

temperatura_massima=  f_scv_temperatura['Temperatura_C'].max() #modo per riprendere il valore piu alto all'interno della tabella

print(temperatura_massima) 

print("Temperatura minima:")
temperatura_minima= f_scv_temperatura['Temperatura_C'].min() #modo per riprendere il valore piu basso all'interno della tabella

print(temperatura_minima) 

print("Temperatura media:")
temperatura_media= f_scv_temperatura['Temperatura_C'].mean() #calcolo media temperatura

print(temperatura_media)

print("Temperatura mediana:")
temperatura_mediana= f_scv_temperatura['Temperatura_C'].median()
print(temperatura_mediana)

print("===================RAPPRESENTAZIONE GRAFICA=======================")


gradi = ['15_c','16_c','17_c','18_c','19_c','20_c','20_c']

giorni = ['Lunedi','Martedi','Mercoledi','Giovedi','Venerdi','Sabato','Domenica']


plt.figure()

plt.bar(gradi, giorni) #indica le barre

plt.title('Clima di Roma questo mese')

plt.xlabel('giorni') #l'asse x avra scritto Categorie

plt.ylabel('gradi') #l'asse y avra scritto Valori


plt.show()
