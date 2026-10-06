#condizione con if
num = 60
if num > 0:
    print("il numero e' magg di 0")


#if- else
num = 60
if num < 0:
    print("il numero e' magg di 0")
else: 
    print("il numero e' minore di 0")


    #elif

    x=20
if x>0:
    print("il numero e' positivo")

elif x<0:
    print ("il numero e  negativo")

else:
    print ("il numero e zero")






#doppio if
x=35
if x>0 :
    print ("il numero e positivo")

if x== 200:
    print ("incredibile")

else:
    print ("Il numero e 0")    




    #match

comando= input ("inserisci un comando:  ")

match comando:       #valuta e controlla ai case 

    case "start":    
        print ("avvio del programma.")

    case "stop":
        print ("chiusura del programma.")

    case "pausa":
        print ("programma in pausa.")

    case _:          #default
       print ("comando non riconosciuto")