# CODICE PER MEMORIZZARE E RECUPERARE CREDENZIALI DI DIVERSE PIATTAFORME

# Creare un dizionario di dizionari
diz = {
    "piattaforma1": {"Utente" : "utente1", "Password" : "password1"},
    "piattaforma2": {"Utente" : "utente2", "Password" : "password2"},
    "piattaforma3": {"Utente" : "utente2", "Password" : "password3"},
    "piattaforma4": {"Utente" : "utente2", "Password" : "password4"}
    }

# Mostrare tutte le piattaforme disponibili
print("\nPIATTAFORME DISPONIBILI")
for x in diz.keys():
    print("-", x)

# Input per la piattaforma desiderata
risp = input("\nPer quale piattaforma hai bisogno dei dati di login? Se vuoi uscire, scrivi q e premi INVIO. ")

# Ciclo while 
while risp != "q" and risp != "Q":
    
    
    try:
        print("\n")
        # Estrazione delle credenziali
        for x,y in diz[risp].items():
            print(x + ":",y)
        # Ripetere input per la piattaforma desiderata
        risp = input("\nPer quale piattaforma hai bisogno dei dati di login? Se vuoi uscire, scrivi q e premi INVIO. ")
    
    # Gestione dell'errore
    except:
        # Messaggio di errore
        print("Nessun dato trovato! Assicurati di aver scritto il nome della piattaforma correttamente.")
        # Ripetere input per la piattaforma desiderata
        risp = input("\nPer quale piattaforma hai bisogno dei dati di login? Se vuoi uscire, scrivi q e premi INVIO. ")

# Messaggio di chiusura
print("\nA presto!")
