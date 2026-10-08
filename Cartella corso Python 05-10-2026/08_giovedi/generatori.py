#decoratore

def decoratore(funzione):
        def wrapper():
            print("prima dell' esecuzione")
            funzione()
            print("dopo esecuzione")
        return wrapper
            


@decoratore
def saluta():
        print ("Ciao!")

saluta()





#generatore
def conta_fino(numero_masimo):
       n=1

# Usa 'n' sia nella condizione che nell'incremento
       while numero<= numero_masimo:
                yield n
                n=n+1

# 1. Chiedi l'input nel programma principale (fuori dalla funzione)
#    Ora 'n' è definita nel programma principale!
                n=int(input(""))

# 2. Passa la variabile 'n' alla funzione
for valore in conta_fino(n):

        print (valore)