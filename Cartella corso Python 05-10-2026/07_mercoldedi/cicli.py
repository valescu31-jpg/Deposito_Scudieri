#While

c=0
while c <5:
    print (c)
    c+=1


#ciclo booleano

controllore= True

while controllore:  #andrebbe all'infinito siccome sempre vero
    print("ciao")

    scelta= input ("scrivi per uscire")
if scelta.lower() == "end":             #scrivendo end, finisce il ciclo
    controllore= False


#For

numeri = [5, 2, 3, 4, 1]
for numero in numeri:  #permette di stampare ogni elemento in maniera cronologicamente giusta  
    print (numero)


limite= 5
for numero in limite: 
    print ("numero")


    #range
    #range start stop
    #range start stop step

