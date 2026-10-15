#1)INCAPSULAMENTO


class Prodotto:

    def __init__(self,_nome_prodotto,_quantita_prodotto):

#proteggiamo(essendo il padre) i valori per evitare la modifica degli stessi dati


        self._nome_prodotto=_nome_prodotto
        self._quantita_prodotto=_quantita_prodotto
        pass


#=======================================================================#
#    METODO PER LEGGERE DATI (get), METODO PER AGGIORNARE I DATI(set)

#========================================================================#


    # Getter per il nome del prodotto
    def get_nome_prodotto(self):
        return self._nome_prodotto

    # Setter per il nome del prodotto (il nome come anche la quantita non dovranno essere in generale nascosti per la stampa e la modifica degli stessi )
    def set_nome_prodotto(self, nome_prodotto):
        self._nome_prodotto = nome_prodotto

    # Getter per la quantità del prodotto
    def get_quantita_prodotto(self):
        return self._quantita_prodotto

    # Setter per la quantità del prodotto
    def set_quantita_prodotto(self, quantita_prodotto):
        self._quantita_prodotto = quantita_prodotto

    # Metodo base per la stampa
    def stampa_dettagli(self):
        print(f"Prodotto: {self._nome_prodotto} | Quantità: {self._quantita_prodotto}")



#2) EREDITARIETA'
class PrezzoSpl(Prodotto):
    def __init__(self,__nome_prodotto,__quantita_prodotto):












