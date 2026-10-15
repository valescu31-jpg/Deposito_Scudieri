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
    def __init__(self,__nome_prodotto,__quantita_prodotto,__reparto):
        
        # super() richiama il costruttore della classe padre (Prodotto), riportando specificamente le variabili definendole private e non piu' protette(specifica figlio)
        super().__init__(self.__nome_prodotto, self.__quantita_prodotto)
        self.__reparto = __reparto

    def get_reparto(self):
        return self.__reparto

#aggiungeremo nelle variabile oltre a self anche reparto poiche logicamente in caso di modifiche
    def set_reparto(self, reparto):
        self.__reparto=reparto


#3) POLIMORFISMO
#Ridefiniamo lo stesso metodo del padre per farlo comportare in modo specifico
def stampa_dettagli(self):

                                #stampa la variabile del get                                                    riporta se stesso
                                 #           |                                                                          |
                                 #           |                                                                          |

        print(f"[Spl] Prodotto: {self.get_nome_prodotto()} | Quantità: {self.get_quantita_prodotto()} | Reparto: {self.__reparto}")




# MENU INTERATTIVO (programma principale)

def main(): #Punto di partenza del programma per leggere

    produzione=[] #utilizzato per aggiungere prodotti durante la giornata


    while True:
            print("\n--- GESTIONE PRODUZIONE FABBRICA ---") #\n va a capo
            print("1 - Aggiungi prodotto")
            print("2 - Visualizza produzione")
            print("3 - Cerca prodotto")
            print("4 - Modifica quantità")
            print("5 - Rimuovi prodotto")
            print("6 - Calcola totale pezzi prodotti")
            print("0 - Esci")
            
            scelta = input("Scegli un'opzione: ")
            
            if scelta == "1":
                nome_prodotto = input("Inserisci il nome del prodotto: ")
                quantita_prodotto = int(input("Inserisci la quantità prodotta: "))
                
                prodotto = Prodotto(nome_prodotto, quantita_prodotto)
                produzione.append(prodotto)                             #portera il prodotto alla fine della lista produzione
                print("Prodotto aggiunto con successo!")




                
            elif scelta == "2":
                print("\n--- LISTA PRODUZIONE CORRENTE ---")
                if not produzione:
                    print("Nessun prodotto registrato oggi.")
                else:
                    for p in produzione:        #p stara per produzione 
                        p.stampa_dettagli()      # stampa la produzione




                        
            elif scelta == "3":
                cerca_nome = input("Inserisci il nome del prodotto da cercare: ")
                trovato = False
                for p in produzione:
                    if p.get_nome_prodotto().lower() == cerca_nome.lower():
                        p.stampa_dettagli()
                        trovato = True
                if not trovato:
                    print("Prodotto non trovato nella lista.")


                    
            elif scelta == "4":
                mod_nome = input("Inserisci il nome del prodotto da modificare: ")
                modificato = False
                for p in produzione:
                    if p.get_nome_prodotto().lower() == mod_nome.lower():
                        nuova_qta = int(input("Inserisci la nuova quantità: "))
                        
                # Usiamo il setter (incapsulamento) per aggiornare il valore
                        p.set_quantita_prodotto(nuova_qta)
                        print("Quantità modificata con successo!")
                        modificato = True
                if not modificato:
                    print("Prodotto non trovato.")



                    
            elif scelta == "5":
                rem_nome = input("Inserisci il nome del prodotto da rimuovere: ")
                rimosso = False

                # Cerchiamo l'indice numerico dell'elemento nella lista
                for i in range(len(produzione)):
                    if produzione[i].get_nome_prodotto().lower() == rem_nome.lower():
                        produzione.pop(i)
                        print("Prodotto rimosso dalla lista.")
                        rimosso = True
                        break
                if not rimosso:
                    print("Prodotto non trovato.")



                    
            elif scelta == "6":
                totale = 0
                for p in produzione:

            # Usiamo il getter per prelevare la quantità senza toccare direttamente i dati privati
                    totale += p.get_quantita_prodotto()
                print(f"Totale complessivo pezzi prodotti: {totale}")
                
            elif scelta == "0":
                print("Chiusura programma in corso...")
                break
            else:
                print("Scelta non valida, riprova.")
    
if __name__ == "__main__":
    main()
    














