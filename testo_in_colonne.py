# CODICE PER DIVIDERE UNA STRINGA IN CAMPI SEPARATI IN BASE A UN DELIMITATORE (REPLICA LA FUNZIONE DATI TESTO IN COLONNE DI EXCEL)

import pandas as pd

# Crea una lista di liste separando gli elementi della colonna desiderata (String, in questo caso) in base a un delimitatore
delim = "_"
liste = data.String.str.split(delim)

# Individua la lista con il maggior numero di stringhe
lunghezza_max = max([len(lista) for lista in liste])

# Crea le colonne necessarie ad accogliere tutti gli elementi della stringa che si vuole separare
colonne = []
for i in range(1, lunghezza_max + 1):
    colonne.append("colonna" + str(i))
 
# Aggiunge le colonne al dataframe e divide la stringa inserendo ogni elemento in una colonna separata
data[colonne] = data.String.str.split(delim, expand=True)

# Elimina la colonna di partenza
data.drop("String", inplace=True)
