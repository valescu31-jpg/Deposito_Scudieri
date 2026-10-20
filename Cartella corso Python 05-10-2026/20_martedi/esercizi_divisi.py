#rendelo ripetibile e salvare i dati all'interno di un .txt

import numpy as np

#1 somma media degli elementi

arr1= np.random.randint(1,101, size=15) #creazione array di 15 elemnti(size) con num casuali da 1 a 100
print(arr1)

print("SOMMA")
somma_elementi= np.sum(arr1)
print(somma_elementi)

print("MEDIA")
media_elementi= np.mean(arr1)
print(f"Media di tutti gli elementi: {media_elementi}")


#2 Manipolazione di Array Multidimensionali

print("Creazaione matrice")
matrice= np.arange(1,26).reshape(5,5) #np.arange(1, 26): Genera una sequenza di numeri interi da 1 a 25 (il valore finale 26 è escluso).
                                       #.reshape(5, 5): Riorganizza i 25 elementi lineari in una struttura a griglia bidimensionale di 5 righe e 5 colonne.

print("Matrice 5x5 creata") 
print(matrice) 

print("Estrazione seconda colonna matrice, terza riga e media")

seconda_colonna= matrice[:, 1] # Il simbolo ':' seleziona tutte le righe, mentre '1' seleziona la seconda colonna
print ("seconda colonna:")
print(seconda_colonna)

terza_riga= matrice[2, :] # Il numero '2' seleziona la terza riga, mentre ':' seleziona tutte le colonne
print ("terza_riga:")
print(terza_riga)


print("somma diagonale")
s_diagonale= np.diag(matrice) #tramite np.diag, estraggo la diagonale
print (s_diagonale)            #la stampo altrimenti non uscira nel terminale
s_diagonale=np.sum(s_diagonale) #faccio l somma dei numneri estratti nella diagonale 
print(s_diagonale) #stampo


#3 Operazione con fancy indexing
print("creazione matrice 4x4")
matrice_2= np.random.randint(10,50, size=(4,4))
print(matrice_2)

print("Utilizzo fancy indexing")

righe= np.array ([0, 1, 2, 3])  #Utilizzare il fancy indexing per selezionare elementi specifici: (0, 1), (1, 3), (2, 2), (3, 0)
                                 #dividendo il tutto in righe e colonne
colonne=np.array ([1, 3, 2, 0])


elementi_sel= matrice_2[righe, colonne]  #elementi selezionti dal testo
print("Cordinate selezionate")
print(elementi_sel)


#righe dispari mancanti



matrice_2[righe,colonne]+=10
print("Array modificato(aggiunendo 10 alle cordinate nel fancy indexing)")
print(matrice_2)








