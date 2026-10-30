#Obiettivo: addestra un DecisionTreeClassifier(max_depth=2) su load_wine() e stampa le regole con export_text. Scrivi in italiano,
#  in due righe, le regole che portano alla classe 0.


from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text


wine = load_wine()
albero= DecisionTreeClassifier(max_depth=2).fit(wine.data, wine.target)


# Stampa le regole testuali
regole = export_text(albero, feature_names=list(wine.feature_names))
print(regole)



print("===============================================================")

print("MEDIO:")


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#Obiettivo: su load_wine() confronta criterion="gini" e criterion="entropy" con max_depth da 1 a 6 (split 75/25, random_state=0).
#  Stampa una tabella con accuratezza di training e di test e indica la combinazione migliore.

wine2 = load_wine()
X = wine.data
y = wine.target

# 2. Dividiamo i dati: 75% training, 25% test (con random_state=0 per avere risultati fissi)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0

)

# Definiamo i criteri e le profondità da testare come richiesto
criteri = ["gini", "entropy"]
profondita = range(1, 7)  # Da 1 a 6

# Prepariamo le variabili per memorizzare la combinazione migliore
miglior_accuratezza_test = 0
miglior_configurazione = None


# Stampa l'intestazione della tabella; i simboli '<10' e '<15' servono a lasciare dello spazio vuoto e allineare le parole a sinistra per rendere la tabella ordinata
print(f"{'Criterio':<10} | {'Max Depth':<10} | {'Acc. Training':<15} | {'Acc. Test':<15}")


# 3. Ciclo per provare tutte le combinazioni
for criterio in criteri: # Primo ciclo: ripete le istruzioni prima usando "gini" e poi "entropy"
  
  for depth in profondita: # Secondo ciclo (annidato): per ogni criterio, prova tutte le profondità da 1 a 6
    
    #  Creiamo e alleniamo l'albero decisionale
    modello = DecisionTreeClassifier(
        criterion=criterio, max_depth=depth, random_state=0 # Crea l'albero decisionale con il criterio e la profondità del giro attuale
    )
    modello.fit(X_train, y_train) # "Allena" l'albero sfruttando i dati di addestramento (il 75% del dataset)

    #  Calcoliamo le predizioni e l'accuratezza
    pred_train = modello.predict(X_train) # Chiede all'albero di indovinare le classi usando i dati di training
    pred_test = modello.predict(X_test) # Chiede all'albero di indovinare le classi usando i dati di test (quelli nuovi)

    acc_train = accuracy_score(y_train, pred_train) # Calcola la percentuale di risposte esatte sul training (da 0 a 1)
    acc_test = accuracy_score(y_test, pred_test) # Calcola la percentuale di risposte esatte sul test (da 0 a 1)


    print(
        f"{criterio:<10} | {depth:<10} | {acc_train:<15.4f} | {acc_test:<15.4f}"
    )  # Stampa a schermo la riga della tabella con i risultati di questo specifico giro


    #  Salviamo la migliore combinazione basandoci sull'accuratezza di test

    if acc_test > miglior_accuratezza_test:  # Controlla se l'accuratezza sul test di questo giro è superiore alla migliore trovata finora
      miglior_accuratezza_test = acc_test # Se è più alta, aggiorna il record del test migliore
      miglior_configurazione = (criterio, depth, acc_train, acc_test) # Salva i dati di questa combinazione vincente

      # Stampiamo il risultato migliore trovato
print(
    f"\nLa combinazione migliore è con Criterio: '{miglior_configurazione[0]}'"
    f" e Max Depth: {miglior_configurazione[1]}"
)
print(
    f"Accuratezza sul Test: {miglior_configurazione[3]:.4f} (Training:"
    f" {miglior_configurazione[2]:.4f})"
)