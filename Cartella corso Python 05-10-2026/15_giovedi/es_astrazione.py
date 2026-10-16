from abc import ABC, abstractmethod

class VeicoloTrasporto(ABC):
    def __init__(self,_targa, _peso_massimo:int):
        self._targa=targa
        self._peso_massimo=peso_massimo
        self._carico_attuale=0
        

    def carico(self,peso):
        self.peso=peso

        if self._carico_attuale+peso <= self._peso_massimo:
            ("carico effettuato")
            self._carico_attuale+= peso
        
            return True
        else:
            print("superata capacita massima")
            return false

        

    def scarica():

        self._carico_attuale=0
        print("veicolo scaricato")

    @abstractmethod
    def costo_manutenzione():
    
    pass


class Camion(VeicoloTrasporto):

    def __init__(self, targa, peso_massimo, numero_assi):
        self.__numero_assi=numero_assi
        super().__init__(targa,_peso_massimo)
    
    def get_numero_assi(self):
                return self._nome_prodotto
    
    def set_numero_assi(self, nome_prodotto):
            self._nome_prodotto = nome_prodotto


    def costo_manutenzione(self):
        self.costo_manutenzione=self.numero_assi* 100+1* self._peso_massimo
        return self.costo_manutenzione


class Furgone(VeicoloTrasporto)

    def __init__(self, targa, peso_massimo,alimentazione):
        self.alimentazione=alimentazione
        super().__init__(_targa, _peso_massimo)

    def get_alimentazione(self):
            return self._nome_prodotto

    def costo_manutenzione(self):
        if self.alimentazione== "elettrico":
             return 200
        else:
            return 150

class Motocarro(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,anni_servizio):
        self.anni_servizio=anni_servizio
        super().__init__(_targa, _peso_massimo)

    def get_anni_servizio(self):
        return self.anni_servizio
            
    def set_anni_servizio(self, nome_prodotto):
        self.anni_servizio = anni_servizio

    def costo_manutenzione():
         return self.anni_servizio*50

    class GestoreFlotta:

         def __init__(self, nome_flotta):
              self.nome_flotta=nome_flotta
              self.listaVeicoli= []



        def aggiungi_veicoli(self, veicolo):

              self.listaVeicoli.append(veicolo)
              print(veicolo.nome, "aggiunto")


        def aggiungi_veicoli(self, targa):

            for veicolo in self.listaVeicoli
                if veicolo.targa== targa:


                self.listaVeicoli.pop(veicolo)
            pass



        


        
        