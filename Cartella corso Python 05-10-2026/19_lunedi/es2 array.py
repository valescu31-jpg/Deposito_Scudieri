import numpy as np


# Genera 20 numeri casuali interi da 10 a 50 (51 è escluso, quindi arriva a 50)
arr = np.random.randint(10, 51, size=20)

print(arr)
print("Tipo:", arr.dtype)

print("primi 10 numeri dell'array")
print(arr[:10])

print("Ultimi 5 numeri dell'array ")
print(arr[-5:])

print("Estrazione elementi")
print(arr[5:16])

print("alternanza di 3")
array_a_salti= arr[::3]
print (array_a_salti)

print("trasformazione valori")
arr[5:10]= [99]
print (arr)

print("================================================================")


matrice= np.random.randint (1,101, size=(6,6)) #creazione matrice 6x6

print("matrice creata")
print(matrice)


sotto_matrice= matrice [1:5, 1:5] #prendera la parte interna della matrice facendola 4x4

# 2. Estrazione della sotto-matrice centrale 4x4
# Visto che la matrice ha indici da 0 a 5, la parte centrale 4x4 
# si estende dalle righe/colonne 1 alla 4
print("sotto matrice 4x4")
print(sotto_matrice)

#1. Inversione delle righe della sotto-matrice 4x4
# [::-1, :] inverte l'ordine delle righe, mentre ':' lascia le colonne inalterate

matrice_invertita= sotto_matrice[::-1, :] #Indicando -1 come passo per le righe (::-1), 
                                          #diciamo a Python di percorrere le righe della matrice all'indietro, partendo dall'ultima fino alla prima (invertendone quindi l'ordine).

# 2. Estrazione della diagonale principale
# np.diag() estrae gli elementi sulla diagonale principale sotto forma di array 1D
diagonale_principale= np.diag(matrice_invertita)     #np.diag() è uno strumento nativo di NumPy che riceve una matrice 2D 
                                                          #e restituisce automaticamente un array 1D contenente gli elementi che si trovano sulla diagonale principale (quella che va dall'angolo in alto a sinistra a quello in basso a destra).

print("Array 1D della diagonale principale:")
print(diagonale_principale)

#Sostituzione dei multipli di 3 con -1
matrice_modificata= matrice_invertita.copy # Creiamo una copia per preservare la matrice invertita originale intatta
matrice_modificata[matrice_modificata%3==0]= -1


#STAMPA DI TUTTI GLI ELEMENTI


print("1. Matrice originale 6x6:")
print(matrice)

print("2. Sotto-matrice centrale 4x4:")
print(sotto_matrice)

print("3. Matrice invertita (righe ribaltate):")
print(matrice_invertita)

print("4. Diagonale principale (array 1D):")
print(diagonale_principale)

print("5. Matrice invertita modificata (multipli di 3 -> -1):")
print(matrice_modificata)

    



















