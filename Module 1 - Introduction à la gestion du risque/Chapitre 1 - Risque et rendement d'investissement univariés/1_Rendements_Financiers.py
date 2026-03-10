'''
1_Rendements_Financiers

Ce chapitre couvre :
    - Le chargement de données de prix via yfinance
    - Le calcul des rendements discrets et logarithmiques
    - La visualisation de la série temporelle et de la distribution

Actif utilisé: AAPL (Apple) | Période : 2015-2024
Librairies : numpy, pandas, matplotlib, yfinance
'''

# Importation des librairies nécessaires

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf




# 1. Charger les données de prix d'un actif financier depuis Yahoo Finance

'''
Description des paramètres utilisés dans yf.download :
- "AAPL" : le ticker de l'action Apple
- auto_adjust=False : conserve Close et Adj Close séparément
    => on utilise "Adj Close" manuellement pour les rendements
    => avec auto_adjust=True, "Close" serait déjà ajusté mais "Adj Close" disparaîtrait du DataFrame
- progress=False : pour éviter l'affichage de la barre de progression
- isinstance(data.columns, pd.MultiIndex) : vérifie si les colonnes sont un MultiIndex (cas où yfinance retourne des données avec plusieurs niveaux de colonnes)
- data.columns.get_level_values(0) : récupère le premier niveau des colonnes si c'est un MultiIndex
- data.sort_index() : s'assure que les données sont triées par date
- print(data.head()) : affiche les premières lignes du DataFrame pour vérifier que les données ont été chargées correctement
'''

TICKER = "AAPL"
data = yf.download(TICKER, start="2015-01-01", end="2024-12-31", auto_adjust=False, progress=False)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)
data = data.sort_index()
print(f"Données de prix chargées pour {TICKER} :")
print(data.head())

# Dans un fichier CSV, on aurait utilisé :
# StockPrices = pd.read_csv("StockData.csv", parse_dates=["Date"])
# StockPrices = StockPrices.sort_values(by="Date")
# StockPrices.set_index("Date", inplace=True) 




# 2. Calculer les rendements discrets et logarithmiques 

'''
_Rendement discret (simple return) :

    R_t2 = (P_t2 - P_t1) / P_t1

Où :
    P_t2 = prix à la période actuelle
    P_t1 = prix à la période précédente

Propriétés des rendements discrets :
- Discrete returns s'agrègent sur les ACTIFS : R_portfolio = somme(w_i * R_i)
En Python :
- data["Adj Close"].pct_change() : calcule automatiquement (P_t - P_{t-1}) / P_{t-1} pour chaque ligne


_Rendement logarithmique (log return) :

    Rl = ln(P_t2 / P_t1)

ou de façon équivalente :

    Rl = ln(P_t2) - ln(P_t1)

Propriétés des rendements logarithmiques :
- Log returns s'agrègent dans le TEMPS : r_annuel = r_j1 + r_j2 + ... + r_j252
En Python : 
- np.log(data["Adj Close"] / data["Adj Close"].shift(1))


_A savoir : 
- Les Log returns sont toujours plus petits que les discrete returns. 
- "Adj Close" est affiché en référence pour valider visuellement les calculs.
    Un dividende ou un split crée un saut artificiel dans "Close" qui fausserait
    les rendements => on travaille toujours sur "Adj Close".
'''

data["Returns"] = data["Adj Close"].pct_change()
data["LogReturns"] = np.log(data["Adj Close"] / data["Adj Close"].shift(1))
returns     = data["Returns"].dropna()
log_returns = data["LogReturns"].dropna()
print("\nRendements calculés (discrets et logarithmiques) :")
print(data[["Adj Close", "Returns", "LogReturns"]].head(8))


# 3. Visualiser les rendements et la distribution des rendements

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Graphique gauche : série temporelle des rendements
axes[0].plot(returns.index, returns, color="steelblue", linewidth=0.6)
axes[0].set_title(f"Rendements journaliers de {TICKER}")
axes[0].set_xlabel("Date")
axes[0].set_ylabel(f"Rendements")

# Graphique droite : histogramme de la distribution
axes[1].hist(returns, bins=75, color="seagreen")
axes[1].set_title(f"Distribution des rendements de {TICKER}")
axes[1].set_xlabel("Rendements")
axes[1].set_ylabel("Fréquence")

plt.tight_layout()
plt.show()
