class Elettrodomestico:

    def __init__(self,__marca, __modello, __anno_acquisto, __guasto):
        self.__marca=marca
        self.__modello=modello
        self.__anno_acquisto=anno_acquisto
        self.__guasto=guasto

    
    
    
    def descrizione(self,__marca, __modello, __anno_acquisto, __guasto):
            print(f"L'elettrodomestico casa {__marca} di modello{__modello}, e' stato acquistato nell'annp{__anno_acquisto} e possiede {__guasto}")
        
        
        
        
