# FUNZIONE CHE CONSENTE DI OTTENERE LA PANORAMICA DI UN DATAFRAME

def overview(df):

    # Prime 5 righe
    display(df.head())
    
    # Dimensione
    display(df.shape)
    
    # Presenza di duplicati
    print("Duplicati: ", df.duplicated().sum())
    
    # Presenza di valori nulli
    if df.isnull().values.any() == False:
        print("Nulli: ", df.isnull().any())
    else:
        print("\nNulli:\n\n", df.isnull().sum())
