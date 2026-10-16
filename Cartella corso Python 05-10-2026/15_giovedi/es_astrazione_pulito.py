from abc import ABC, abstractmethod  # Importa le classi per gestire le classi astratte (ABC)

class VeicoloTrasporto(ABC):  # Definizione della classe astratta base per i veicoli
    def __init__(self, _targa, _peso_massimo: int):  # Costruttore della classe base
        self._targa = targa  # Assegna il valore della targa all'attributo protetto
        self._peso_massimo = peso_massimo  # Assegna il peso massimo consentito
        self._carico_attuale = 0  # Inizializza il carico corrente del veicolo a zero

    def carico(self, peso):  # Metodo per gestire l'aggiunta di un carico
        self.peso = peso  # Salva il peso passato come attributo dell'istanza

        if self._carico_attuale + peso <= self._peso_massimo:  # Controlla se il nuovo carico rientra nel limite massimo
            print("carico effettuato")  # Messaggio di successo (aggiunto 'print()' che mancava originariamente)
            self._carico_attuale += peso  # Incrementa il carico attuale con il nuovo peso
            return True  # Ritorna True se l'operazione è andata a buon fine
        else:
            print("superata capacita massima")  # Messaggio di errore se si supera la capacità
            return False  # Ritorna False correggendo il 'false' minuscolo errato

    def scarica(self):  # Metodo per svuotare il veicolo
        self._carico_attuale = 0  # Riporta il carico attuale a zero
        print("veicolo scaricato")  # Messaggio di avvenuto scarico (aggiunto 'self' nei parametri)

    @abstractmethod  # Decoratore che rende questo metodo astratto
    def costo_manutenzione(self):  # Metodo astratto che obbliga le sottoclassi a implementarlo (aggiunto 'self')
        pass  # Nessun corpo nella classe base


class Camion(VeicoloTrasporto):  # Sottoclasse Camion che eredita da VeicoloTrasporto
    def __init__(self, __targa, __peso_massimo, numero_assi):  # Costruttore del Camion
        self.numero_assi = numero_assi  # Assegna il numero di assi
        super().__init__(targa, peso_massimo)  # Chiama il costruttore della classe padre
    
    def get_numero_assi(self):  # Getter per il numero di assi
        return self._numero_assi  # Ritorna il numero di assi (rimosso il refuso "_nome_prodotto")
    
    def set_numero_assi(self, numero_assi):  # Setter per il numero di assi
        self._numero_assi = numero_assi  # Aggiorna il numero di assi

    def costo_manutenzione(self):  # Implementazione del costo di manutenzione per il camion
        self.costo_manutenzione_val = self._numero_assi * 100 + 1 * self._peso_massimo  # Calcola il costo
        return self.costo_manutenzione_val  # Ritorna il valore calcolato


class Furgone(VeicoloTrasporto):  # Sottoclasse Furgone che eredita da VeicoloTrasporto
    def __init__(self, __targa, __peso_massimo, alimentazione):  # Costruttore del Furgone
        self.alimentazione = alimentazione  # Assegna il tipo di alimentazione
        super().__init__(targa, peso_massimo)  # Chiama il costruttore del padre

    def get_alimentazione(self):  # Getter per l'alimentazione
        return self.alimentazione  # Ritorna l'alimentazione

    def set_alimentazione(self, alimentazione):  # Setter per l'alimentazione
        self.alimentazione = alimentazione  # Aggiorna l'alimentazione

    def costo_manutenzione(self):  # Implementazione del costo di manutenzione per il furgone
        if self.alimentazione == "diesel":  # Controlla se l'alimentazione è benzina
            return 200  # Ritorna 200 se a benzina
        else:
            return 150  # Ritorna 150 per gli altri casi


class Motocarro(VeicoloTrasporto):  # Sottoclasse Motocarro che eredita da VeicoloTrasporto
    def __init__(self, __targa, __peso_massimo, anni_servizio):  # Costruttore del Motocarro
        self.anni_servizio = anni_servizio  # Assegna gli anni di servizio
        super().__init__(targa, peso_massimo)  # Chiama il costruttore del padre

    def get_anni_servizio(self):  # Getter per gli anni di servizio
        return self.anni_servizio  # Ritorna gli anni di servizio
            
    def set_anni_servizio(self, anni_servizio):  # Setter per gli anni di servizio
        self.anni_servizio = anni_servizio  # Aggiorna gli anni di servizio

    def costo_manutenzione(self):  # Implementazione del costo di manutenzione (aggiunto 'self')
        return self.anni_servizio * 50  # Calcola il costo moltiplicando gli anni per 50


class GestoreFlotta:  # Classe per la gestione della flotta (spostata fuori da Motocarro per correggere l'indentazione)
    def __init__(self, nome_flotta):  # Costruttore del gestore
        self.nome_flotta = nome_flotta  # Assegna il nome della flotta
        self.listaVeicoli = []  # Inizializza la lista vuota dei veicoli

    def aggiungi_veicoli(self, veicolo):  # Metodo per aggiungere un veicolo alla lista
        self.listaVeicoli.append(veicolo)  # Aggiunge il veicolo alla lista
        print(veicolo._targa, "aggiunto")  # Stampa un messaggio usando la targa corretta del veicolo

    def rimuovi_veicolo(self, targa):  # Metodo corretto per rimuovere un veicolo in base alla targa
        for veicolo in self.listaVeicoli:  # Cicla attraverso la lista dei veicoli
            if veicolo._targa == targa:  # Controlla se la targa corrisponde
                self.listaVeicoli.remove(veicolo)  # Rimuove l'oggetto dalla lista
                print("veicolo rimosso")  # Messaggio di conferma rimozione
                return True  # Ritorna True se trovato e rimosso
        return False  # Ritorna False se la targa non viene trovata


    def costo_totale(self):  # Metodo per calcolare il costo complessivo di manutenzione della flotta
        totale = 0  # Inizializza il totale a zero
        for v in self.listaVeicoli:  # Scorre ogni veicolo presente nella lista della flotta
            totale = totale + v.costo_manutenzione()  # Somma il costo di manutenzione del singolo veicolo richiamando il metodo con le parentesi
        return totale  # Ritorna il costo totale accumulato (messo fuori dal ciclo)def costo_totale():
        totale=0

    def stampa_veicoli(self):
        print ("\n ELENCO VEICOLI FLOTTA")
        if len(self.listaVeicoli)==0:
            print("Nessun veicolo presente nella flotta.")

    
            

                




    

    