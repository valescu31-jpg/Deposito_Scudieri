import numpy as np

arr1 = np.linspace(0, 10, 50) #array equidistante

print(arr1)

arr2= np.random.rand(0,1,50) #array random equidistante
print(arr2)


print("somma array con creazione nuovo array")

nuovo_array = []

# 2. Inizializziamo i due contatori (indici) per i due array
i = 0
j = 0

# Troviamo la lunghezza massima per decidere quanti giri deve fare il ciclo for
max_len = max(len(arr1), len(arr2))

# 3. Ciclo for basato sulla dimensione massima
for _ in range(max_len):
    
    # Se il contatore è ancora dentro i limiti dell'array, prendiamo il valore, altrimenti 0
    val1 = arr1[i] if i < len(arr1) else 0
    val2 = arr2[j] if j < len(arr2) else 0
    
    # Sommiamo i valori delle posizioni correnti
    somma = val1 + val2
    nuovo_array.append(somma)
    
    # Incrementiamo i contatori se non hanno raggiunto la fine del rispettivo array
    if i < len(arr1):
        i += 1
    if j < len(arr2):
        j += 1

# Risultato
print(f"Elementi in arr1: {len(arr1)}")
print(f"Elementi in arr2: {len(arr2)}")
print(f"Elementi nel nuovo array (somma): {len(nuovo_array)}")

