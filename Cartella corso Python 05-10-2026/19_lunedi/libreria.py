import numpy as np



# Creazione di un array

arr = np.array([1, 2, 3, 4, 5])


# Utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape)  # Output: (5,)

print("Dimensioni dell'array:", arr.ndim)  # Output: 1

print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)

print("Numero di elementi:", arr.size)  # Output: 5

print("Somma degli elementi:", arr.sum())  # Output: 15

print("Media degli elementi:", arr.mean())  # Output: 3.0

print("Valore massimo:", arr.max())  # Output: 5

print("Indice del valore massimo:", arr.argmax())  # Output: 4



print("==============================================================")

#dtype
arr = np.array([1, 2, 3], dtype='int32')

print(arr.dtype)  # Output: int32

print("==============================================================")

#shape
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # Output: (2, 3)  #due righe(le due liste) e 3 numeri all'interno


print("==============================================================")

#arange
arr = np.arange(10) #avra' sempre le start,stop e step

print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]



print("==============================================================")

#reshape
arr = np.arange(6)

reshaped_arr = arr.reshape((2, 3))

print(reshaped_arr)

# Output:  [[0 1 2] [3 4 5]] #divide il range 





print("==============================================================")




#Esempio:

arr = np.array([1, 2, 3, 4, 5])


# Indexing

print(arr[0])  # Output: 1= posizione


# Slicing prende da un punto x da uno y escluso e prende tutti i valori che rientrano in quella logica

print(arr[2:3])  # Output: [2 3]


# Boolean Indexing tutti i valori che superano questo elemento

print(arr[arr > 2])  # Output: [3 4 5]


print("==============================================================")


arr_2d = np.array([[1, 2, 3, 4],

                   [5, 6, 7, 8],

                   [9, 10, 11, 12]])

# Slicing sulle righe

print(arr_2d[1:3])  # Output: [[ 5  6  7  8]

                   #          [ 9 10 11 12]]

# Slicing sulle colonne

print(arr_2d[:, 1:3])  # Output: [[ 2  3]

                       #          [ 6  7]

                       #          [10 11]]

# Slicing misto


print(arr_2d[1:3, 1:3])  # Output: [[ 6  7]

                        #          [10 11]]





                        # Slicing di base

print(arr[2:7])  # Output: [2 3 4 5 6]


# Slicing con passo

print(arr[1:8:2])  # Output: [1 3 5 7]


# Omettere start e stop

print(arr[:5])  # Output: [0 1 2 3 4]

print(arr[5:])  # Output: [5 6 7 8 9]


# Utilizzare indici negativi

print(arr[-5:])  # Output: [5 6 7 8 9]

print(arr[:-5])  # Output: [0 1 2 3 4]



#fancy indexing

arr = np.array([10, 20, 30, 40, 50])


# Utilizzo di un array di indici

indices = np.array([1, 3])

print(arr[indices])  # Output: [20 40]


# Utilizzo di una lista di indici

indices = [0, 2, 4]

print(arr[indices])  # Output: [10 30 50]


