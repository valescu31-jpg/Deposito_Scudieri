#modo per avere il numero randomico
def numero_casuale():
    """Genera un numero casuale da 1 a 100"""
    import random
    return random.randint(1,100)

def controlla_tentativo (tentativo, numero_casuale):

#ciclo che rende possibile la ciclicita' del programma 

while tentativo != numero_casuale:
    tentativo = int(input("indovina il numero da 1 a 100:"))

#condizioni possibili

    if tentativo < numero_casuale:
    print ("il numero da indovinare e' piu alto")    

    elif tentativo > numero_casuale:
    print ("il numero da indovinare e' piu basso")

    else tentativo==numero_casuale:
    print ("indovinato")



#es 2