class Garage:


# Metodo costruttore: viene eseguito quando crei un oggetto Garage.
    # Prende in input la capienza massima e le auto già presenti.


    def __init__(self, capienza):

        self.auto_presenti= []
        self.capienza=capienza


# Metodo speciale __len__: permette di usare la funzione len() 
    # direttamente sull'oggetto Garage per sapere quanti elementi ci sono.


    def __len__(self):
        return  len(self.auto_presenti)



    def parcheggia (self, auto_presenti):

        if auto_presenti>=self.capienza:
            print ("ERRORE, parcheggio pieno")

        elif auto_presenti< self.capienza:
            self.auto_presenti+=1
            self.capienza-=1
            print("macchina parcheggiata")



    #def formato_targa_valida(self):

    
# Metodo per rimuovere un'auto dal garage

    def rimuovi(self, auto_presenti, capienza, targa):

        targa=input("inserisci targa")

        
        self.auto_presenti-=1
        self.capienza+=1

        if  targa not in self.auto_presenti:
            print ("Errore:macchina non trovata")

        else:
            self.auto_presenti.remove(targa)
            print("macchina rimossa")



    def posti_liberi(self,capienza, autopresenti):
        return self.capienza- len(self.auto_presenti)






        

        
