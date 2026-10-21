# Importa la libreria Pandas e la chiama "pd" per comodità
import pandas as pd

# Crea un dizionario con i dati grezzi organizzati per colonne
data_multi = {
    'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
    'Anno': [2023, 2024, 2023, 2024],
    'Vendite': [120, 135, 110, 118]
}

# Converte il dizionario in un DataFrame di Pandas (una tabella di dati)
df_multi = pd.DataFrame(data_multi)

# Trasforma le colonne "Paese" e "Anno" in un indice gerarchico (MultiIndex)
df_multi = df_multi.set_index(['Paese', 'Anno'])

# Stampa un'intestazione testuale per separare l'output
print("\nDataFrame con MultiIndex:")

# Stampa a schermo il DataFrame finale con il nuovo indice a più livelli
print(df_multi)