class Persona:

#costruttore che dichiara parametri
    def __init__(self, nome, eta: int):
        self.nome=nome
        self.eta=eta


    def presentazione(self):
        print("Si chiama:",self.nome, "con eta'=:", self.eta)


class Studente(Persona):


#inizializzo la lista voti

    __voti=[10,8,4,5,2,7,9]
    

    
# costruttore e non dichiara voti, poiche voti e' stato inizializzato primo

    def __init__(self,nome,eta:int):
        self.__nome=nome
        self.__eta=eta
        


    

    

    def calcolo_media(self):

        #media voti che riprende la variabile __voti(privato), sfruttando la somma diviso la lunghezza della lista

        media_voti= sum(self.__voti)/ len(self.__voti)

        
        print (media_voti)
        


    
    
    
        





class Professore(Persona):

    

    def __init__(self,nome,eta, materia):
        self.__nome=nome
        self.__eta=eta
        self.__materia=materia

    


        



        

        
        

        


        
        

        
