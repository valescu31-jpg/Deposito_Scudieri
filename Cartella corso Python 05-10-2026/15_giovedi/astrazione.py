from abc import ABC, abstractmethod
class Pippo_Astratto(ABC): #classe astratta utilizzata

    
    x = 10
    
    def ciao(self):
        print("ciao")
        
    @abstractmethod #lascia metodi vuoti vostringendo i figli a nsovrascroverli

    def Metodo_obbligatorio(self): #questo metodo e' astratto
        pass
    
    @abstractmethod
    def Metodo_obbligatorio2(self):
        pass
    
    
    
class Pippo_reale(Pippo_Astratto):
    
    def Metodo_obbligatorio(self):
        print("sono reale")
        
    def Metodo_obbligatorio2(self):
        print("sono reale 2")

        
        
P_r = Pippo_reale()  # dai figli si

# P_a = Pippo_Astratto()  Non si può creare un oggeto tramite una classe astratt
                


#===============================================================================#


#Es 1 Astrazione

from abc import ABC, abstractmethod

class Impiegato:
     def __init__(self, nome, cognome, stipendio_base):
         self.nome=nome
         self.cognome=cognome
         self.stipendio_base=stipendio_base

abstractmethod
def calcola_stipendio():

    pass


class ImpiegatoFisso(Impiegato):
    def calcola_stipendio():

        print(f"Lo stipendio sara base")
        pass



class ImpiegatoApprovigione():
    def calcola_stipendio():
        bonus=int(input("inserisci un bonus in €"))
        print(f"Lo stipendio e' maggiore attraverso bonus")

        prova1=
        prova2=

        pass

    
    
    
        




