#definizione lista
nomi= ["Valerio", "Federico", "Giovanni"]
misto= [1, "due", True, 4.5]

#stampa dei nomi
print (nomi[0])

#metodi liste
numeri= [3,1,4,2,5]

#conta la lunghezza della lista
print (len(numeri))

numeri.append (4)
print (numeri)

#inserisci numeri nella lista nella posizione a tua scelta
numeri.insert (1,4)
print(numeri)


numeri.remove(3)
print (numeri)

#ordina dal piu alto al piu basso
numeri.sort()
print(numeri)