import numpy as np

#while
 #   pass

# Chiediamo all'utente quante righe e colonne vuole e trasformiamo il testo in numeri interi (int)
righe = int(input("Inserisci il numero di righe: "))
colonne = int(input("Inserisci il numero di colonne: "))
            
 # Qui usiamo NumPy: np.random.randint genera numeri interi casuali (da 1 a 99) 
 # riempiendo una griglia della dimensione esatta che l'utente ha scelto (size=(righe, colonne)).
matrice = np.random.randint(1, 100, size=(righe, colonne))
print("\nMatrice Creata:")
print(matrice) # Stampiamo la matrice a schermo

if matrice is None:
    print("ERRORE: Devi prima creare una matrice")
    #continue # Riporta l'utente all'inizio del menu

# .shape ci dice la struttura della matrice (quante righe 'r' e colonne 'c' possiede)
r, c = matrice.shape
            
 # Se la matrice è troppo piccola, non ha senso tagliare il centro
if r < 3 or c < 3:
    print("La matrice è troppo piccola per estrarre un centro significativo.")
    
    # SLICING PULITO: [1:-1, 1:-1] taglia via la prima e l'ultima linea su entrambi i lati
    sotto_matrice = matrice[1:-1, 1:-1]

    print("matrice centrale:")
    print(sotto_matrice)

   
    if matrice is None:
        print("ERRORE: Devi prima creare una matrice")
        #continue
            
    matrice_trasposta = matrice.T
    print(matrice_trasposta)

    if matrice is None:
        print("ERRORE: Devi prima creare una matrice ")
        #continue
            
            # np.sum somma automaticamente tutti i numeri contenuti dentro la matrice, di qualsiasi dimensione essa sia.
    somma = np.sum(matrice)
            
    print(f"\nSomma di tutti gli elementi: {somma}")




    #difficolta nell'implementare all'interno del while tutte le casisitche, in alcune cose mi ho cecato tramite prompt all'ai degli aiuti, ancora devo toccare la seconda perte quindi non so bene ancora in cosa avrei potuto trovare difficolta




