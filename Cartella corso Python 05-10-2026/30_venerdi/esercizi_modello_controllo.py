#Obiettivo: un modello di controllo qualità ha analizzato 200 pezzi:
#  15 difettosi reali, di cui 12 individuati; inoltre ha segnalato come difettosi 6 pezzi buoni. 
# Calcola a mano TP, TN, FP, FN, accuratezza, precision, recall e F1, poi verifica i risultati con scikit-learn creando i vettori y_vero e y_previsto.

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Creiamo i vettori per i 200 pezzi:
# 1 = Difettoso, 0 = Buono
# Sappiamo che ci sono 15 difettosi reali (quindi quindici '1' in y_vero)
# e 185 buoni (185 '0' in y_vero).

y_vero = [1] * 15 + [0] * 185

# Ora costruiamo y_previsto (le decisioni del modello) rispettando i nostri numeri:
# - 12 TP: i primi 12 difettosi reali devono essere previsti come 1 (12 volte '1')
# - 3 FN: i restanti 3 difettosi reali devono essere previsti per sbaglio come buoni (3 volte '0')
# - 6 FP: i primi 6 pezzi buoni reali devono essere previsti per sbaglio come difettosi (6 volte '1')
# - 179 TN: i restanti 179 pezzi buoni reali devono essere previsti come buoni (179 volte '0')

y_previsto = [1] * 12 + [0] * 3 + [1] * 6 + [0] * 179

# Calcoliamo le metriche usando scikit-learn
accuratezza = accuracy_score(y_vero, y_previsto)
precision = precision_score(y_vero, y_previsto)
recall = recall_score(y_vero, y_previsto)
f1 = f1_score(y_vero, y_previsto)

# Stampiamo i risultati in modo pulito
print(f"Accuratezza: {accuratezza:.4f}")
print(f"Precision:   {precision:.4f}")
print(f"Recall:      {recall:.4f}")
print(f"F1-Score:    {f1:.4f}")