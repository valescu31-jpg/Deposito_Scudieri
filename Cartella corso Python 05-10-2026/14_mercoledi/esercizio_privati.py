class Persona:


    def __init__(self, nome, eta: int):
        self.nome=nome
        self.eta=eta


    def presentazione(self):
        print("Si chiama:",self.nome, "con eta'=:", self.eta)


class Studente:

    voti=[10,8,4,5,2,7,9]
    

    
    

    def __init__(self,nome,eta, voti: int):
        self.__nome=nome
        self.__eta=eta
        self.__voti=voti


    

    media_voti= sum(voti)/ len(voti)

    def calcolo_media(self):

        self.calcolo_media.voti=self.media_voti
        print (self.media_voti)
        


    class Studente(Persona):
    
            def presentazione(self):
                print("Si chiama:",self.nome, "con eta'=:", self.eta, "possiede media voti:", voti)
        





class Professore:

    pass

    def __init__(self,nome,eta, materia):
        self.nome=nome
        self.eta=eta
        self.materia=materia


    class Professore(Persona):

        def presentazione(self):
            print("Si chiama:",self.nome, "con eta'=:", self.eta, "Insegna:", self.materia)


        



        

        
        

        


        
        

        
