class Studente:
    def __init__(self, nome, eta):
        self.nome=nome
        self.eta=eta

    def __str__(self):
        return "Shrek: " + self.nome + ", pipino: " + str(self.eta) #crea un vero e proprio dialogo

studente1=Studente("Luca", 20)

print(studente1)



#=====================================================#


class Squadra:

    def __init__(self, nome, giocatori):
        self.nome= nome
        self.giocatori= giocatori


    def __len__(self):

        
        return len(self.giocatori)


squadra1= Squadra("Eufrate",["Luca","Marco", "Anna","Agela"]) # ci riconsegnail numero di persone della lista non il nome

print (len(squadra1))


#=============================================#

class Moltiplicatore:
    
    
    def __init__(self, numero):
        self.numero=numero

    def __call__(self, valore):
        return valore* self.numero

doppio= Moltiplicatore(3)

print(doppio(10)) 

    




