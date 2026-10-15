def main():
    produzione = []
    
    while True:
        print("\n--- GESTIONE PRODUZIONE FABBRICA ---")
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
            produzione.append(prodotto)
            print("Prodotto aggiunto con successo!")
            
        elif scelta == "2":
            print("\n--- LISTA PRODUZIONE CORRENTE ---")
            if not produzione:
                print("Nessun prodotto registrato oggi.")
            else:
                for p in produzione:
                    p.stampa_dettagli()
                    
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
                    p.set_quantita_prodotto(nuova_qta)
                    print("Quantità modificata con successo!")
                    modificato = True
            if not modificato:
                print("Prodotto non trovato.")
                
        elif scelta == "5":
            rem_nome = input("Inserisci il nome del prodotto da rimuovere: ")
            rimosso = False
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
                totale += p.get_quantita_prodotto()
            print(f"Totale complessivo pezzi prodotti: {totale}")
            
        elif scelta == "0":
            print("Chiusura programma in corso...")
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()