# PROGRAMMA PER ORGANIZZARE I FILE IN UNA DIRECTORY IN BASE ALLA LORO ESTENSIONE

# Moduli
import os
import shutil
from pathlib import Path
import sys

# Richiede la directory di lavoro
directory = str(input("Inserisci la directory (q per uscire): "))
x = 0

# Si sposta nella directory
while x == 0:

    # Esce dal ciclo se viene dato q come input
    if directory.lower() == "q":
        sys.exit()
    else:
        
        try:
            os.chdir(directory)
            x = 1
        except:
            print("\nDirectory non valida")
            directory = str(input("\nInserisci la directory (q per uscire): "))

# Individua le estensioni presenti nella directory
estensioni = set([Path(x).suffix for x in os.listdir()])
estensioni = [x for x in estensioni if x != ""]

# Mostra le estensioni presenti
print("Estensioni trovate:")
for x in estensioni:
    print(x)

# Crea le cartelle e sposta i file
if len(estensioni) > 0:
    for est in estensioni:
        try:
            os.mkdir(est)
            for file in os.listdir():
                if file.endswith(est):
                    shutil.move(file, est)
        except:
            for file in os.listdir():
                if file.endswith(est):
                    shutil.move(file, est)
                    
    print("\nOrganizzazione terminata!")

else:
    # Restituisce messaggio
    print("\nNessun file trovato! Trovati questi elementi:")

    # Mostra gli elementi presenti nella directory
    for file in os.listdir():
        print(file)
        
# Input finale per evitare che il prompt si chiuda automaticamente
input()
