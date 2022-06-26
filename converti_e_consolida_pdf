# CODICE PER CONVERTIRE IMMAGINI PRESENTI IN UNA SPECIFICA DIRECTORY E CONSOLIDARLE IN UN UNICO PDF

# Importare i moduli necessari
from PIL import Image
from PyPDF2 import PdfFileMerger
import os

# Specificare la directory in cui le immagini sono salvate
os.chdir("direcory")
os.getcwd()

# Convertire i file immagini in pdf
for x in os.listdir() :
    if x.endswith(".jpg") or x.endswith(".png") or x.endswith(".jpeg"):
        pdf = Image.open(x)
        pdf.save(f"{x}.pdf")

# Inizializzare l'aggregatore
merger = PdfFileMerger()

#Unire i singoli pdf
for x in os.listdir() :
    if x.endswith(".pdf"):
        merger.append(x)

# Salvare il file combinato
merger.write("Merged.pdf")
merger.close()

# Rimuovere i singoli pdf dalla directory corrente
for x in os.listdir():
    if x.endswith(".pdf") and x != "Merged.pdf":
        os.remove(x)

