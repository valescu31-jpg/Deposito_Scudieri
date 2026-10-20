import numpy as np

arr= np.array([])  #creazione array

arr = np.arange(49) #lunghezza array

#arr_r = np.random.randint(49, 101)
#arr_t= np.concatenate((arr,arr_r))

print (arr) #stampa array

print(arr.dtype)  #stampa il tipo (es int)


print(arr.shape) #righe ed elementi conteggia

arr = arr.astype('float64') #modifica il tipo di numeri che si trovano all'interno dell'array
print(arr.dtype)


print("========================================================================================")


#SLICING

print("primi 10 numeri dell'array")
print(arr[:10])

print("Ultimi 7 numeri dell'array ")
print(arr[-7:])

print("Estrazione elementi")
print(arr[5:20])

print("alternanza di 4")
array_a_salti= arr[::4]
print (array_a_salti)

print("trasformazione valori")
arr[10:15]= [999]
print (arr)

print("========================================================================================")

#fancy indexing
print("Elementi selezionati in posizione scelta")
print(arr[[0, 3, 7, 12, 25, 33, 48]]) #modo per stampare le posizioni e si sfruttano le doppie quadre

print("elementi pari all'interno dell'array")
print(arr[arr % 2==0])  #stampa tutti i numeri pari attraverso maschera booleana

print ("media")
media=np.mean(arr)  #calcoli la media con funzione mean
print (media)
maggiori_della_media= arr[arr>media] #prende valori all'interno dell'array e se sono maggiori della media li stampa
print ("elementi maggiori della media")
print(maggiori_della_media)






