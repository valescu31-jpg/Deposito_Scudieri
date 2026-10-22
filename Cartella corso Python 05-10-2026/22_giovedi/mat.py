import matplotlib.pyplot as plt
import numpy as np

print("=========================GRAFICO LINEARE================================")

x = [1, 2, 3, 4, 5]             #liste di dati che servono per il grafico
y = [2, 3, 5, 7, 11]

plt.figure() #creazione della figura
plt.plot(x, y) #imporrtazione delle variabili all'interno del grafico

# extra
plt.title('Grafico a Linee') #da un titolo
plt.xlabel('X Axis') #assegna all'asse x la varibile X
plt.ylabel('Y Axis')  #assegna all'asse y la varibile y

plt.show() #mostra il grafico


print("==================GRAFICO A BARRE========================")

categories = ['A', 'B', 'C', 'D', 'E']

values = [3, 7, 2, 5, 8]


plt.figure()

plt.bar(categories, values) #indica le barre

plt.title('Grafico a Barre')

plt.xlabel('Categorie') #l'asse x avra scritto Categorie

plt.ylabel('Valori') #l'asse y avra scritto Valori


plt.show()



print("================ISTOGRAMMA=========================")




data = np.random.randn(100) #serve per i dati visualizzati sull'asse x e quello y


plt.figure()

plt.hist(data, bins=10) #comando per importare istogramma, bins valori (linee) itogramma

plt.title('Istogramma')

plt.xlabel('Valori')

plt.ylabel('Frequenza')

plt.show()



print("========================SCATTER PLOT======================================")


x = np.random.rand(50) #puntini sull'asse x

y = np.random.rand(50)  #puntini sull'asse y


plt.figure()

plt.scatter(x, y) #richiamo variabili

plt.title('Scatter Plot')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.show()