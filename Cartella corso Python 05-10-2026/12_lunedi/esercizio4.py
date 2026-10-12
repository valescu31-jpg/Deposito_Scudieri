class Garage:



    def __init__(self, capienza, auto_presenti):

        self.auto_presenti= auto_presenti
        self.capienza=capienza



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

    targa=input("inserisci targa")


    def rimuovi(self, auto_presenti, capienza, targa):
        self.auto_presenti-=1
        self.capienza+=1

        if  targa not in self.auto_presenti:
            print ("Errore:macchina non trovata")

        else:
            self.auto_presenti.remove(targa)
            print("macchina rimossa")



    def posti_liberi(self,capienza, autopresenti):
        return self.capienza- len(self.auto_presenti)

    

        print (len(auto_presenti))


        

        
