# FUNZIONE PER CONFRONTARE LA DISTRIBUZIONE DI UNA VARIABILE CON UNA NORMALE STANDARDIZZATA

# Moduli
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, zscore

# Funzione
def plot_kde_over_norm(data):
    
    # Crea la curva normale standardizzata
    x = np.linspace(-3,3)
    y = norm(0,1).pdf(x)
    
    # Plotta la normale standardizzata
    plt.plot(x,y, linestyle="--")
    
    # Standardizza i dati forniti e li plotta sopra la normale
    sns.kdeplot(zscore(data), color="red")
    
    # Aggiunge una legenda
    plt.legend(["Normal", "Your data"])
    
    # Mostra il grafico
    plt.show()
