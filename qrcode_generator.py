# CODICE PER GENERARE QRCODE DA PAGINE WEB E SALVARLI IN UNA CARTELLA

# Importare i moduli necessari
import pyqrcode as qrc
import png
import os
import requests
from scrapy import Selector

# Lista di link alle pagine web
urls = ["https://www.google.com/","https://it.wikipedia.org/", "https://www.amazon.it/"]

# Lista vuota per raccogliere i titoli delle pagin web
titoli = []

# Lista vuota per raccogliere i qrcode generati

qrcodes = []

# Connettersi alle pagine web e generare il qrcode
for url in urls:

    # Estrarre il codice html
    html = requests.get(url).content

    # Estrarre il titolo della pagina web
    sel = Selector(text = html)
    titolo = sel.xpath('//title/text()').extract_first()

    # Aggiungere il titolo alla lista vuota
    titoli.append(titolo)

    # Generare il qrcode
    qrcode = qrc.create(url)

    # Aggiungere il qrcode alla lista vuota
    qrcodes.append(qrcode)
    
# Directory in cui salvare i qrcode
path = "C:\\Users\\david\\OneDrive\\Desktop\\qrcodes"

# Se la directory è già esistente
try:
    os.chdir(path)

    for i in range(len(qrcodes)):
        qrcodes[i].png(titoli[i] + ".png", scale=7)
        
# Se la directory non è esistente
except:
    os.mkdir(path)
    os.chdir(path)

    for i in range(len(qrcodes)):
        qrcodes[i].png(titoli[i] + ".png", scale=7)
