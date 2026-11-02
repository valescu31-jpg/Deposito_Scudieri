import pandas as pd
from sklearn.datasets import load_breast_cancer

# 1. Caricamento del dataset come DataFrame pandas
data = load_breast_cancer(as_frame=True)

# 2. Estrazione delle feature X e del target y
X = data.data
y = data.target

# Stampa forma di X e y
print(f"Forma di X (matrice delle feature): {X.shape}")
print(f"Forma di y (vettore target): {y.shape}\n")

# Stampa nomi delle feature e delle classi
print("Nomi delle Feature (30 in totale):")
print(list(X.columns))
print("\nNomi delle Classi:")
print(data.target_names)  # Index 0: 'malignant', Index 1: 'benign'

# Stampa delle prime 5 righe
print("\nPrime 5 righe delle feature X:")
print(X.head())

# Lettura del contenuto di DESCR
print("\n--- Estratto della Descrizione (DESCR) ---")
print(data.DESCR[:1200])

# 3. Controllo del bilanciamento delle classi
print("\nDistribuzione delle classi in y:")
print(y.value_counts())
print(y.value_counts(normalize=True))

# 4. Statistiche descrittive (Min e Max)
desc = X.describe()
print("\nValore minimo più basso tra tutte le feature:", desc.loc["min"].min())
print("Valore massimo più alto tra tutte le feature:", desc.loc["max"].max())
print(
    "Feature con la scala più grande (Max):",
    desc.loc["max"].idxmax(),
    f"({desc.loc['max'].max()})",
)
print(
    "Feature con la scala più piccola (Max):",
    desc.loc["max"].idxmin(),
    f"({desc.loc['max'].min()})",
)



from sklearn.model_selection import train_test_split

# Passaggio 1: Separiamo il 20% per il Test set e l'80% temporaneo (Train + Validation)
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Passaggio 2: Dall'80% temporaneo, separiamo il 20% totale originale (ovvero il 25% dell'80%) per la Validation
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp
)

# Stampa dimensioni dei dataset
print(f"Dataset di Training:   {X_train.shape[0]} campioni ({X_train.shape[0]/len(X):.0%})")
print(f"Dataset di Validation: {X_val.shape[0]} campioni ({X_val.shape[0]/len(X):.0%})")
print(f"Dataset di Test:       {X_test.shape[0]} campioni ({X_test.shape[0]/len(X):.0%})\n")

# Percentuale di Tumori Maligni (label = 0) nei tre insiemi
print(f"Percentuale Maligni in Train:      {(y_train == 0).mean():.2%}")
print(f"Percentuale Maligni in Validation: {(y_val == 0).mean():.2%}")
print(f"Percentuale Maligni in Test:       {(y_test == 0).mean():.2%}")


import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# ==========================================
# 1. APPLICAZIONE DELLO StandardScaler (REGOLA D'ORO)
# ==========================================

# Inizializziamo lo StandardScaler (centra i dati a media 0 e deviazione standard 1)
scaler_std = StandardScaler()

# REGOLA D'ORO: Eseguiamo il fit ESCLUSIVAMENTE sul training set per calcolare
# la media (mu) e la deviazione standard (sigma) di ogni singola feature.
scaler_std.fit(X_train)

# Trasformiamo (standardizziamo) il training set usando i parametri appena calcolati
X_train_std = scaler_std.transform(X_train)

# Trasformiamo il validation set usando SEMPRE i parametri del training
# (questo evita il "data leakage" o fuga di informazioni dal validation)
X_val_std = scaler_std.transform(X_val)

# Trasformiamo il test set usando SEMPRE i parametri del training
# (il test viene scalato ora per coerenza, ma non verrà usato in questa fase)
X_test_std = scaler_std.transform(X_test)


# ==========================================
# 2. VERIFICA STATISTICA DI MEDIA E DEVIAZIONE STANDARD
# ==========================================

# Calcoliamo la media lungo le colonne (asse 0) del training scalato
train_mean_check = np.mean(X_train_std, axis=0)
# Calcoliamo la deviazione standard lungo le colonne del training scalato
train_std_check = np.std(X_train_std, axis=0)

# Calcoliamo la media lungo le colonne del validation scalato
val_mean_check = np.mean(X_val_std, axis=0)

print("--- VERIFICA STATISTICA ---")
print(
    f"Media media delle feature nel Training: {train_mean_check.mean():.6f} (≈ 0)"
)
print(
    f"Dev. Std. media delle feature nel Training: {train_std_check.mean():.6f} (≈ 1)"
)
print(
    f"Media media delle feature nel Validation: {val_mean_check.mean():.6f} (NON esattamente 0)"
)


# ==========================================
# 3. RIADDESTRAMENTO KNN (k=5) SU DATI SCALATI
# ==========================================

# Creiamo una nuova istanza di KNeighborsClassifier con k=5
knn_std = KNeighborsClassifier(n_neighbors=5)

# Addestriamo il modello utilizzando i dati di training standardizzati
knn_std.fit(X_train_std, y_train)

# Calcoliamo l'accuratezza sul training set scalato
train_acc_std = knn_std.score(X_train_std, y_train)

# Calcoliamo l'accuratezza sul validation set scalato
val_acc_std = knn_std.score(X_val_std, y_val)

print("\n--- RISULTATI KNN CON StandardScaler ---")
print(f"Training Accuracy (Standardizzato):   {train_acc_std:.4f}")
print(f"Validation Accuracy (Standardizzato): {val_acc_std:.4f}")


# ==========================================
# 4. PROVA CON MinMaxScaler
# ==========================================

# Inizializziamo il MinMaxScaler (riscala i valori nell'intervallo [0, 1])
scaler_minmax = MinMaxScaler()

# Anche qui applichiamo la regola d'oro: fit ESCLUSIVAMENTE sul training set
scaler_minmax.fit(X_train)

# Trasformiamo training, validation e test nell'intervallo [0, 1]
X_train_minmax = scaler_minmax.transform(X_train)
X_val_minmax = scaler_minmax.transform(X_val)
X_test_minmax = scaler_minmax.transform(X_test)

# Riaddestriamo il KNN (k=5) sui dati riscalati con MinMaxScaler
knn_minmax = KNeighborsClassifier(n_neighbors=5)
knn_minmax.fit(X_train_minmax, y_train)

# Valutiamo l'accuratezza di validation con MinMaxScaler
val_acc_minmax = knn_minmax.score(X_val_minmax, y_val)

print(f"Validation Accuracy con MinMaxScaler: {val_acc_minmax:.4f}")


import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# ==========================================
# 7.1 CALCOLO DELLE ACCURATEZZE PER k DISPARI DA 1 A 41
# ==========================================

# Creiamo una lista di valori di k dispari da 1 a 41 (usiamo numeri dispari
# per evitare parità nei voti della classificazione binaria)
k_values = list(range(1, 42, 2))

# Liste vuote per memorizzare le accuratezze su training e validation per ogni k
train_accuracies = []
val_accuracies = []

# Ciclo for per testare ciascun valore di k
for k in k_values:
  # Inizializziamo il KNN con il valore corrente di k
  knn_model = KNeighborsClassifier(n_neighbors=k)

  # Addestriamo il modello utilizzando i dati di training standardizzati
  knn_model.fit(X_train_std, y_train)

  # Calcoliamo l'accuratezza sul training set e la aggiungiamo alla lista
  train_acc = knn_model.score(X_train_std, y_train)
  train_accuracies.append(train_acc)

  # Calcoliamo l'accuratezza sul validation set e la aggiungiamo alla lista
  val_acc = knn_model.score(X_val_std, y_val)
  val_accuracies.append(val_acc)


# ==========================================
# 7.2 DISEGNO DELLA CURVA DI COMPLESSITÀ
# ==========================================

# Impostiamo le dimensioni del grafico
plt.figure(figsize=(10, 6))

# Tracciamo la linea dell'accuratezza sul training set (colore blu)
plt.plot(
    k_values,
    train_accuracies,
    marker="o",
    color="blue",
    linewidth=2,
    label="Training Accuracy",
)

# Tracciamo la linea dell'accuratezza sul validation set (colore arancione/rosso)
plt.plot(
    k_values,
    val_accuracies,
    marker="s",
    color="darkorange",
    linewidth=2,
    label="Validation Accuracy",
)

# Aggiungiamo titolo, etichette agli assi e griglia per facilitare la lettura
plt.title(
    "Curva di Complessità del KNN al variare di k",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Valore di k (Numero di vicini)", fontsize=12)
plt.ylabel("Accuratezza", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)
plt.xticks(k_values)

# Mostriamo il grafico a schermo
plt.show()


# ==========================================
# 7.4 SCELTA DEL MIGLIOR k BASATA ESCLUSIVAMENTE SUL VALIDATION SET
# ==========================================

# Troviamo l'indice (la posizione) che ha l'accuratezza di validation massima
best_idx = np.argmax(val_accuracies)

# Ricaviamo il valore di k corrispondente a quell'indice
best_k = k_values[best_idx]
best_val_accuracy = val_accuracies[best_idx]

print(f"--- RISULTATO OTTIMIZZAZIONE ---")
print(f"Miglior valore di k trovato: {best_k}")
print(f"Accuratezza corrispondente sul Validation Set: {best_val_accuracy:.4f}")




from sklearn.tree import DecisionTreeClassifier, export_text

# ==========================================
# 8.1 & 8.2 ADDESTRAMENTO E CONFRONTO PER DIVERSE PROFONDITÀ (DATI NON SCALATI)
# ==========================================

# Lista dei valori di max_depth da testare (inclusa None per profondità illimitata)
depths = [1, 2, 3, 5, 8, None]
results = []

# Ciclo per addestrare un albero per ciascuna profondità
for depth in depths:
  # Inizializziamo il DecisionTreeClassifier sui dati NON scalati (X_train, y_train)
  dt = DecisionTreeClassifier(max_depth=depth, random_state=42)

  # Addestriamo l'albero di decisione
  dt.fit(X_train, y_train)

  # Raccogliamo le metriche richieste
  n_leaves = dt.get_n_leaves()  # Numero di nodi foglia dell'albero
  train_acc = dt.score(X_train, y_train)  # Accuratezza sul training set
  val_acc = dt.score(X_val, y_val)  # Accuratezza sul validation set

  # Salviamo i risultati in un dizionario
  results.append({
      "max_depth": str(depth),
      "n_leaves": n_leaves,
      "train_acc": train_acc,
      "val_acc": val_acc,
  })

# Convertiamo la lista di risultati in un DataFrame pandas per una visualizzazione pulita
df_results = pd.DataFrame(results)
print("--- Tabella Riassuntiva delle Performance al variare di max_depth ---")
print(df_results)


# ==========================================
# 8.3 SCELTA DELLA PROFONDITÀ MIGLIORE SUL VALIDATION
# ==========================================

# Troviamo la riga con l'accuratezza di validation massima
best_row = df_results.loc[df_results["val_acc"].idxmax()]
print(f"\nMiglior max_depth scelto sul Validation: {best_row['max_depth']}")
print(f"Accuratezza di Validation corrispondente: {best_row['val_acc']:.4f}")

# Estraiamo il valore numerico (o None) per addestrare l'albero ottimale
best_depth = (
    int(best_row["max_depth"]) if best_row["max_depth"] != "None" else None
)
best_dt = DecisionTreeClassifier(max_depth=best_depth, random_state=42)
best_dt.fit(X_train, y_train)


# ==========================================
# 8.4 ESPORTAZIONE DELL'ALBERO IN TESTO
# ==========================================

# Stampiamo le regole decisionali testuali generate dall'albero ottimale
tree_rules = export_text(best_dt, feature_names=list(X.columns))
print("\n--- Regole Decisionali dell'Albero (Estratto) ---")
print(tree_rules[:1200])


# ==========================================
# 8.5 CALCOLO DELL'INDICE DI GINI (RADICE)
# ==========================================

# Calcoliamo il numero totale di campioni nel training set
n_tot = len(y_train)
# Calcoliamo la frazione di campioni maligni (classe 0) e benigni (classe 1)
p_mal = (y_train == 0).sum() / n_tot
p_ben = (y_train == 1).sum() / n_tot

# Calcolo manuale dell'indice di Gini: 1 - (p_mal^2 + p_ben^2)
gini_manual = 1.0 - (p_mal**2 + p_ben**2)

# Estraiamo l'indice di Gini calcolato nativamente dall'albero sul nodo radice (indice 0)
gini_code = best_dt.tree_.impurity[0]

print(f"\nIndice di Gini calcolato a mano: {gini_manual:.4f}")
print(f"Indice di Gini estratto dall'albero: {gini_code:.4f}")


# ==========================================
# 8.6 VERIFICA DELL'EFFETTO DELLO SCALING SUL DECISION TREE
# ==========================================

# Addestriamo lo stesso albero utilizzando i dati di training standardizzati (X_train_std)
dt_scaled = DecisionTreeClassifier(max_depth=best_depth, random_state=42)
dt_scaled.fit(X_train_std, y_train)

# Calcoliamo l'accuratezza sul validation set standardizzato
val_acc_scaled = dt_scaled.score(X_val_std, y_val)
print(f"Val Accuracy con dati scalati: {val_acc_scaled:.4f}")
print(
    f"Val Accuracy con dati non scalati: {best_row['val_acc']} (Identica!)"
)