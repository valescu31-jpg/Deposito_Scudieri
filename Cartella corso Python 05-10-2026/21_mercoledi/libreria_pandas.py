import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]

df = pd.DataFrame(data)