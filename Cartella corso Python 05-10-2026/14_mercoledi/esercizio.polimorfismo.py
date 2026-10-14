class MeteodoPagamento:


    def effettua_pagamento(self,importo):
        self.importo=importo
        print("Stai effetuando un pagamento.")

        








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

importo=int (input("Inserisci saldo"))

     
                
