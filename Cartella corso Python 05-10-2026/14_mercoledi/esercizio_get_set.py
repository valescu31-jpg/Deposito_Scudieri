class ContoCorrente:


    __intestatario= ""

    __saldo= ""

    def __init__(self, intestatario, saldo=0.0):
        self.__intestatario = __intestatario
        self.__saldo = __saldo

    def get_intestatario(self):
        pass
    def get_saldo(self):
        pass
    def set_intestatario(self):

        self.intestatario = nuovo_intestatario
        print(f"Intestatario aggiornato a: {self.intestatario}")

        
    def set_saldo(self):

        if nuovo_saldo < 0:
            print("ERRORE: Impossibile impostare un saldo negativo.")
        else:
            self.saldo = nuovo_saldo
            print(f"Saldo impostato a: {self.saldo} euro")
        
        





    def deposita(self, importo):
        if importo < 0:
            print("ERRORE: Impossibile depositare un importo negativo. Saldo non modificato.")
        else:
            self.saldo += importo
            print(f"Deposito riuscito. Nuovo saldo: {self.saldo}")

    def preleva(self, importo):
        if importo < 0 or importo > self.saldo:
            print("ERRORE: Importo non valido o fondi insufficienti. Saldo non modificato.")
        else:
            self.saldo -= importo
            print("Il tuo saldo è stato aggiornato.")

    def stampa_saldo(self):
        return f"Intestatario: {self.intestatario} - Saldo attuale: {self.saldo} euro"