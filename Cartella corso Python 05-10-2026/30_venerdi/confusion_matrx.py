
#Cosa mostra: matrice di confusione e metriche calcolate a mano e con scikit-learn su un piccolo esempio.


from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

# 1. Definizione dei dati: etichette reali (y_vero) e previsioni del modello (y_previsto)
y_vero     = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1]   # 1 = frode, 0 = transazione legittima
y_previsto = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0]

# 2. Generazione della matrice di confusione e scompattamento nei suoi 4 elementi chiave
tn, fp, fn, tp = confusion_matrix(y_vero, y_previsto).ravel()   # .ravel() appiattisce l'array nell'ordine: TN, FP, FN, TP

# 3. Visualizzazione tabulare della matrice di confusione (Le righe rappresentano il valore reale, le colonne il previsto)
print(confusion_matrix(y_vero, y_previsto))    

# 4. Stampa dei singoli valori numerici per una verifica immediata
print(f"TP={tp} TN={tn} FP={fp} FN={fn}")

# 5. Calcolo della Precisione: 
# Logica: "Su tutte le transazioni che il modello ha etichettato come frodi, quante erano davvero frodi?" 
# Formula manuale: TP / (TP + FP) vs funzione nativa di scikit-learn
print("Precision manuale:", tp / (tp + fp), "| sklearn:", precision_score(y_vero, y_previsto))

# 6. Calcolo del Recall (Sensibilità): 
# Logica: "Su tutte le frodi realmente esistenti nel dataset, quante il modello è riuscito a scoprire?"
# Formula manuale: TP / (TP + FN) vs funzione nativa di scikit-learn
print("Recall manuale:   ", tp / (tp + fn), "| sklearn:", recall_score(y_vero, y_previsto))

# 7. Calcolo dell'F1-Score e dell'Accuratezza globale:
# - F1-score: Media armonica tra Precision e Recall (utile per bilanciare i due aspetti).
# - Accuratezza: Percentuale complessiva di predizioni corrette (sia 0 che 1) sul totale.
print("F1:", round(f1_score(y_vero, y_previsto), 3), "| Accuratezza:", accuracy_score(y_vero, y_previsto))




print("==========================================================================================")


#Cosa mostra: il report completo su un dataset reale e l'importanza di scegliere la classe positiva giusta.

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, recall_score

# 1. Caricamento del dataset integrato in scikit-learn (Tumore al seno)
data = load_breast_cancer()
print(data.target_names)          # Stampa le etichette testuali: ['malignant' 'benign'] (0 = maligno, 1 = benigno)

# 2. Divisione dei dati in set di addestramento (75%) e test (25%)
# 'stratify=data.target' è fondamentale per mantenere la stessa percentuale di tumori maligni/benigni sia nel train che nel test
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
)   

# 3. Standardizzazione delle feature (importante per il KNN che si basa sulle distanze geometriche)
# Calcoliamo media e deviazione standard SOLO sul training set (.fit) per evitare "data leakage" (perdita di informazioni dal test set)
scaler = StandardScaler().fit(X_train)

# 4. Addestramento del modello K-Nearest Neighbors (KNN)
# I dati di training vengono trasformati (scalati) prima di essere usati dall'algoritmo con k=5 vicini
knn = KNeighborsClassifier(n_neighbors=5).fit(scaler.transform(X_train), y_train)

# 5. Generazione delle previsioni sul test set
# Scaliamo anche il test set utilizzando esattamente gli stessi parametri calcolati sul training set
y_pred = knn.predict(scaler.transform(X_test))

# 6. Valutazione completa delle performance del modello
# Genera un report tabulare con Precision, Recall, F1-Score e Support per ciascuna delle due classi
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 7. Calcolo mirato del Recall limitato alla classe di maggiore interesse clinico: i MALIGNI (pos_label=0)
# In campo medico il Recall è cruciale: misura la capacità di individuare tutti i veri malati, riducendo al minimo i falsi negativi.
print("Recall sui MALIGNI:", round(recall_score(y_test, y_pred, pos_label=0), 3))



print("==========================================================================================")

#Cosa mostra: perché l'accuratezza inganna con classi sbilanciate, e come disegnare la matrice di confusione.


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix

# 1. Creazione di un dataset sintetico fortemente sbilanciato
# Simula uno scenario reale tipico (es. rilevamento frodi o malattie rare): 
# Il 95% dei dati appartiene alla classe negativa (0) e solo il 5% alla classe positiva (1).
X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=42)   

# 2. Divisione in set di addestramento (train) e test
# 'stratify=y' è cruciale qui: assicura che la percentuale del 5% di positivi rimanga identica sia nel train che nel test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3. Creazione di un modello di base ("Dummy" o "pigro")
# Strategia "most_frequent": prevede SEMPRE la classe 0 (la maggioritaria). 
# Serve come termine di paragone (baseline): un vero modello deve fare molto meglio di questo.
pigro = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)   

# 4. Addestramento di un modello di Machine Learning reale: l'Albero di Decisione
albero = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)

# 5. Valutazione e confronto comparativo tra i due modelli
# Nota logica importante: vedrai che il modello "pigro" avrà un'accuratezza altissima (~95%), 
# ma un Recall e un F1-Score pari a 0, dimostrando che l'accuratezza da sola inganna sui dati sbilanciati!
for nome, m in [("Dummy", pigro), ("Albero", albero)]:
    y_pred = m.predict(X_test)
    print(f"{nome:7s} accuracy={accuracy_score(y_test, y_pred):.3f} "
          f"recall={recall_score(y_test, y_pred, zero_division=0):.3f} "
          f"f1={f1_score(y_test, y_pred, zero_division=0):.3f}")

# 6. Calcolo della matrice di confusione specifica per l'Albero di Decisione
cm = confusion_matrix(y_test, albero.predict(X_test))

# 7. Rappresentazione grafica tramite Heatmap (mappa di calore) con Seaborn
sns.heatmap(
    cm, 
    annot=True,          # annot=True scrive i numeri esatti dentro le celle della griglia
    fmt="d",             # Formato dei numeri come interi (decimali)
    cmap="Blues",        # Scala di colori basata sulle sfumature di blu
    xticklabels=["neg", "pos"], 
    yticklabels=["neg", "pos"]
)

# 8. Personalizzazione delle etichette e visualizzazione del grafico
plt.xlabel("Previsto") 
plt.ylabel("Reale") 
plt.title("Matrice di confusione - albero")
plt.show()