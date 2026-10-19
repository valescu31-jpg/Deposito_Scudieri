class Elettrodomestico:

    def __init__(self,_marca, _modello, _anno_acquisto, _guasto):
        self._marca=marca
        self._modello=modello
        self._anno_acquisto=anno_acquisto
        self._guasto=guasto

    
    
    
    def descrizione(self,_marca, _modello, _anno_acquisto, _guasto):
            print(f"L'elettrodomestico casa {_marca} di modello{_modello}, e' stato acquistato nell'annp{_anno_acquisto} e possiede {_guasto}")
            pass


    def stima_costo_base(self):
         pass


class Lavatrice(Elettrodomestico):
     def __init__(self, __marca, __modello, __anno_acquisto, __guasto, __capacita_kg: int, __giri_centrifuga: int):
        super().__init__(__marca, __modello, __anno_acquisto, __guasto)

        #self.__capacita_kg=capacita_kg
        #self.__giri_centrifuga=giri_centrifuga

    def stima_costo_base(self):
        if  capacita_kg == giri_centrifuga:
             print("La lavatrice e' prestante")

        elif capacita_kg < giri_centrifuga:
             print("Lavatrice poco prestante")


     
    
        


class Frigorifero(Elettrodomestico):
    def __init__(self, __marca, __modello, __anno_acquisto, __guasto, __litri:int, ha_freezeer: bool):
        super().__init__(__marca, __modello, __anno_acquisto, __guasto)
        
        #self.__litri=litri
        self.__ha_freezeer=ha_freezeer

    def stima_costo_base(self):
         pass



class Forno(Elettrodomestico):

     def __init__(self, __marca, __modello, __anno_acquisto, __guasto, __tipo_alimentazione, __ha_ventilato:bool):
          super().__init__(__marca, __modello, __anno_acquisto, __guasto)

        #self.__tipo_alimentazione=tipo_alimentazione
          #self.__ha_ventilato=ha_ventilato

    def stima_costo_base(self):
     pass










class TicketRiparazione(Officina):






class Officina:
     


    
    
        
        
        
        
