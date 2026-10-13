class Veicolo:  #primo padre piu' importante



    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")



class DotazioniSpeciali:  #secondo padre



    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}") #join unisce i de messaggi



#figli

class AutomobileSportiva (Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli): #ordine preciso dei padri l'ultimo e quello del figlio
        Veicolo.__init__(self,marca, modello) #chiama il padre con poi l'informazioni
        #alternativa a super per l'ereditarieta multipla
        DotazioniSpeciali.__init__(self,dotazioni) #chiama secondo padre
        self.cavalli= cavalli #parametro dentro al costruttore unico dentro all'init

    def mostra_informazioni(self): #funzione sovrascritta dal padre
        super().mostra_informazioni() #prende dal padre 

        #chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        DotazioniSpeciali.mostra_dotazione() #prende dal padre ma meno utilizzato(self)

        #possiamo chiamare metodi di etnrambe le superclassi


auto_sportiva= AutomobileSportiva("Ferrari", "F8", ["ABS","Controllo", "trazione", "Airbag laterali"], 720)

auto_sportiva.mostra_informazioni()
        
    