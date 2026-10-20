import numpy as np

arrlin = np.linspace(0, 1, 12)  #creera' valori equidistanti tra loro permeteendo la creazione di dati artificiali

print(arrlin)

print("Cambio forma in matrice 3x4")
matrice_arrlin = arrlin.reshape((3, 4)) #lo converto in matrice attraverso reshape con poi il numero di righe (3) e colonne(4) 
print(matrice_arrlin)


print("genenerazione matrice 3x4")
random_matrice = np.random.rand(3, 4) #crea una matrice random di 3 righe e 4 colonne 
print(random_matrice)


print("Somma due matrici")

somma_matrice1 = np.sum(arrlin)
somma_matrice2 = np.sum(matrice_arrlin)

print(somma_matrice1)
print(somma_matrice2)







print("Cambio tipo matrice")

matrice_arrlin= (matrice_arrlin*10).astype(int) #metodo per rendere una matrice di numeri con la virgola in intero 
                                                #attraverso moltiplicazioni per 10 per preservare il decimale
print(matrice_arrlin)



