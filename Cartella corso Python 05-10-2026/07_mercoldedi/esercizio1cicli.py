
# mentre il controllore e' vero il ciclo si ripete
controllore= True
while controllore:

#insereisco numero
    numero= int(input("inserisci un numero"))

#numero inserito e sara lo start poi si stoppera a -1 e scalera di numero di -1
    for x in range (numero, -1, -1):
        print(x)

    #se l'utente rispondesse no finisce il ciclo  
    richiesta = input("vuoi ripetere")
    if richiesta == "no":
        controllore= False


#es2




      

    



