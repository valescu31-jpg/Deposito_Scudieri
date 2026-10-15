class MeteodoPagamento:


    def effettua_pagamento(self,importo):
        pass
        


class CartadiCredito(MeteodoPagamento):
    def effettua_pagamento(self,importo=500):
            self.importo=importo
            if importo<=0:
                print("transazione errata, saldo CartadiCredito inseufficente")

            elif importo>0:
                print("transazione avvenuta con successo")



class Paypal(MeteodoPagamento):
     def effettua_pagamento(self,importo=500):
        self.importo=importo
        if importo<=0:
            print("transazione errata, saldo Paypal insufficente")
     
        elif importo>0:
            print("transazione avvenuta con successo")
        
                 


class GestorePagamenti(MeteodoPagamento):

    def __init__(self,metodo):
          self.metodo= metodo



    def processa(self,importo):
            self.metodo= effettua_pagamento(importo)
    
     

     
                
