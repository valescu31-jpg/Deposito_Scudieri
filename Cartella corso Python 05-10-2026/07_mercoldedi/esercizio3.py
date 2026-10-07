#ciclo while

continuare= True

while continuare:
     

    scelta1=int(input("inserisci un numero"))
    

    scelta2=int(input("inserisci un numero"))
    
    scelta3=int(input("inserisci un numero"))
    

    scelta4=int(input("inserisci un numero"))
   
    somma_totale= scelta1+scelta2+scelta3+scelta4
    print("la somma totale e':", somma_totale)

    scelta=int(input("press 0 for exit, press 1 for continue"))

if scelta==0:
    continuare== False
    print("end.")


#ciclo for

parola= input("inserisci una parola")

for lettera in parola:
    print(lettera)


#ciclo range

massimo= int(input("Inserisci il numero massimo: "))
step = int(input("Inserisci lo step: "))
start= int(input("Inserisci lo start: "))

for numero in range (start, massimo+1, step): #massimo+1 serve per aver il risultato esatto che vogliamo
        print(numero)