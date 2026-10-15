class BasePosto:
#"""Classe base che rappresenta un posto generico all'interno della struttura."""
    def __init__(self,_numero):
        self._numero=_numero

    def prenota(self,_numero,_fila):

#"""Metodo per effettuare la prenotazione del posto."""
        

        pass

#"""Metodo per liberare un posto precedentemente occupato."""
    def libera(self,_occupato,_numero):
        

        pass

# --- Proprietà (Getter e Setter) per il numero ---
    @property
    def _numero(self):
        return self._numero
        pass


    @_numero.setter
    def set_numero(self, numero_nuovo):
       # """Imposta un nuovo numero per il posto, con un controllo di validazione."""
        pass
        if len(_numero_nuovo)<5:
                pass

# --- Proprietà per la fila
    def _fila(self):

    @_fila.setter

# --- Proprietà per lo stato di occupazione
    def _occupato(self):
    @ _occupato.setter

    pass


class PostoStandars(BasePosto):

    def __init__(self,_numero, costo):
          self.costo=costo
# Chiama il costruttore della classe padre per inizializzare il numero
          def prenota(self,_numero,_fila):
               pass



class Teatro():

#"""Classe che gestisce il teatro e l'insieme dei posti disponibili."""
    def __init__(self, _posto):
          self
          
          pass

               
               
          
     







        



        