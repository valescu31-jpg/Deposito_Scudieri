#Obiettivo: su load_wine() applica StandardScaler e PCA(n_components=2), 
# stampa la varianza spiegata dalle due componenti e disegna lo scatter colorato per classe. 
# Ripeti senza scaling e confronta i due grafici: quale feature domina la PCA non scalata e perché?

import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

"""""
wine = load_wine()
X_scaled = StandardScaler().fit_transform(wine.data)    # prima lo scaling (qui nessun test set: solo esplorazione)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)                     # da (150, 4) a (150, 2)

print("Varianza spiegata:", pca.explained_variance_ratio_.round(3))          # [0.73 0.229]
print("Totale conservato:", pca.explained_variance_ratio_.sum().round(3))
print("PC1 =", {f: round(float(c), 2) for f, c in zip(wine.feature_names, pca.components_[0])})   # ricetta della PC1

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=wine.target, cmap="viridis", edgecolor="k")
plt.xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
plt.title("wine dopo la PCA"); plt.show()
"""


wine = load_wine()
X_scaled = StandardScaler().fit_transform(wine.data)   # prima lo scaling (qui nessun test set: solo esplorazione)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled) 

print("Varianza spiegata:", pca.explained_variance_ratio_.round(3))          
print("Totale conservato:", pca.explained_variance_ratio_.sum().round(3))
print("PC1 =", {f: round(float(c), 2) for f, c in zip(wine.feature_names, pca.components_[0])}) 


# 5. Prepariamo il primo grafico (a sinistra) con i dati scalati e colorati per classe
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=wine.target, cmap="viridis", edgecolor="k")
plt.xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
plt.title("wine dopo la PCA"); plt.show()



# ==========================================
# PARTE 2: SENZA SCALING
# ==========================================

# 6. Ripetiamo la PCA ma saltando lo StandardScaler (usiamo X grezzo)
pca_unscaled = PCA(n_components=2)
X_pca = pca_unscaled.fit_transform(X_pca)

# 7. Stampiamo la varianza spiegata senza scaling
print("\n--- RISULTATI SENZA SCALING ---")
print("Varianza spiegata dalle 2 componenti (non scalate):", pca_unscaled.explained_variance_ratio_)




# 8. Prepariamo il secondo grafico (a destra) senza scaling
plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=wine.target, cmap='viridis', edgecolor='k')
plt.title("PCA SENZA Scaling (Dominata dalla Proline)")
plt.xlabel("Prima Componente (Dominante)")
plt.ylabel("Seconda Componente")

# Mostriamo a schermo il confronto visivo tra i due grafici
plt.tight_layout()
plt.show()

# DOMANDA: Quale feature domina la PCA non scalata e perché?
# RISPOSTA: Senza scaling, la prima componente spiega quasi il 100% della varianza (circa 0.99 o 99%).
# Perchè succede? Nel dataset wine ci sono feature con scale enormi (come la 'proline', che va da centinaia a 
# oltre mille) e feature con scale piccolissime (es. da 0 a 2). La PCA misura la "varianza" come grandezza numerica pura: 
# un numero che va da 0 a 1000 ha una varianza matematica molto più alta di uno che va da 0 a 1, quindi la PCA 
# pensa erroneamente che quella sia l'unica informazione importante, ignorando le altre.









print("Medio")
#Obiettivo: su load_breast_cancer() (30 feature, standardizzate) disegna lo scree plot e la curva della varianza cumulata.
#  Quante componenti servono per il 90% e per il 99%? 
# Stampa le 3 feature con il peso (in valore assoluto) maggiore nella prima componente.


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA


""""
digits = load_digits()
X = digits.data                                       # 64 pixel con valori da 0 a 16 (stessa scala)

pca_tutte = PCA().fit(X)
cumulata = np.cumsum(pca_tutte.explained_variance_ratio_)
print("Componenti per il 95% della varianza:", np.argmax(cumulata >= 0.95) + 1)

pca95 = PCA(n_components=0.95).fit(X)                 # decimale = frazione di varianza da conservare
print("Con n_components=0.95:", pca95.n_components_, "componenti")

fig, axes = plt.subplots(1, 4, figsize=(12, 3))
axes[0].plot(range(1, 65), cumulata); axes[0].set_title("Varianza cumulata")
axes[0].set_xlabel("n. componenti")
for ax, k in zip(axes[1:], [5, 15, 40]):
    pca_k = PCA(n_components=k).fit(X)
    ricostruita = pca_k.inverse_transform(pca_k.transform(X[:1]))   # comprimi e decomprimi
    ax.imshow(ricostruita.reshape(8, 8), cmap="gray"); ax.set_title(f"{k} componenti")
plt.show()
"""