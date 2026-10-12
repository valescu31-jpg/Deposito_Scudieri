class Persona:

    #variabile di classe
     nome=" "

     def saluta(self):
        return("Ciao sono Mirko")


    #metodo utilizzato
ogg_1= Persona()        #indettazione da controllare sempre
ogg_2= Persona()


    #inizializazzione del'oggetto tramite costruttore
ogg_1.nome="Luca"
ogg_2.nome="Martina"

print(ogg_1.nome)
print(ogg_2.nome)

    
print(ogg_1.saluta())



#metodi speciali

class Persona:

    #metodo costruttore
    def __init__(self, eta):
        self.eta= eta

    #variabile di classe
    nome=" "

    def saluta(self):
        return("Ciao sono Mirko")


    #metodo utilizzato
ogg_1= Persona(31)        #indettazione da controllare sempre
ogg_2= Persona(22)


    #inizializazzione del'oggetto tramite costruttore
ogg_1.nome="Luca"
ogg_2.nome="Martina"

print(ogg_1.nome)
print(ogg_2.nome)


#creazione di una classe

class Automobile: #dichiaro istanza
    num_ruote=4    #attributo di classe

    def __init__(self, marca, modello): #metodo costruttore

        self.modello= modello

def stampa_info(self):

    print("L'automobile e' una, self.marca, self.modello")



#creazione dell'oggetto

Auto1= Automobile("Fiat", "500")
Auto1= Automobile("BMW", "X3")

Auto1.stampa_info 

Auto2.stampa_info 



#metodo statico

class Calcolatrice:

    @staticmethod
    def somma(a, b):
        return a+b

risultato= Calcolatrice.somma(5,3)

print (risultato)