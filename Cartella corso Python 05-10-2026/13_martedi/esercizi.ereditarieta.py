class Animale:
    def __init__(self,nome, eta):

        self.nome=nome
        self.eta=eta

    def fai_suono(self):
        print(f"{self.nome} fa suono generico")





class Leone(Animale):
    def __init__(self,nome, eta, verso):
        Animale._init__(self,nome, eta, verso)
        self.verso= verso

    def caccia(self):
        print("Il leone sta cacciando ")

        







class Giraffa(Animale):
    def __init__(self,nome, eta, verso):
        self.verso= verso

    def mangiare(self):
        print ("La giraffa sta mangiando")



class Pinguino(Animale):
    def __init__(self,nome, eta,verso):
        self.verso= verso

    def volare(self):
        print ("il pinguino sta volando")









#===========================================================#



class Prodotto:



    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome=nome
        self.costo_produzione= costo_produzione
        self.prezzo_vendita=prezzo_vendita


    def calcolare_profitto(self):
        self.calcolare_profitto= self.prezzo_vendita-self.costo_produzione




class Elettronica(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, modello):
        Prodotto.__init__(self, nome,costo_produzione, prezzo_vendita, modello)
        self.modello=modello



class Abbigliamento(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, modello, materiale):
        Prodotto.__init__(self, nome,costo_produzione, prezzo_vendita, modello, materiale)
        self.materiale=modello



class Fabbrica():



    def __init__(self,):
        self.inventario={}


    
        


    def aggiungi_prodotto(self,nome, c):
        



        
    def vendi_prodotto(self,inventario):



        
    def resi_prodotto(self,invenatario):


        





   

        

        



























































