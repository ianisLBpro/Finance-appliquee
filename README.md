# Gestion de Portefeuille

Ce projet regroupe l'ensemble de mes travaux réalisés dans le cadre de l'étude de la gestion de portefeuille et de la gestion quantitative des risques appliquées à la finance de marché. Il couvre un large spectre de sujets allant de la construction et l'optimisation de portefeuille jusqu'à la modélisation du risque de crédit et les modèles GARCH, en passant par les modèles factoriels, la Value at Risk et la théorie moderne du portefeuille.

## Technologies utilisées

| Catégorie | Librairies |
|---|---|
| Calcul scientifique | `numpy`, `scipy`, `pandas` |
| Visualisation | `matplotlib`, `seaborn` |
| Finance | `yfinance`, `pandas_datareader` |
| Statistiques & économétrie | `statsmodels` |

> **Python 3.x** — Voir le fichier [INSTALLATION.md](INSTALLATION.md) pour la mise en place de l'environnement virtuel.

---

## Structure du projet

### Module 1 — Introduction à la gestion du risque

Ce module introduit les fondamentaux de la gestion du risque et du rendement d'un portefeuille financier. Il couvre la construction de portefeuille, les modèles factoriels de Fama-French, et l'estimation du risque de queue.

**Actifs utilisés** : AAPL, MSFT, AMZN, JPM, JNJ | **Période** : 2016–2026 | **Benchmark** : S&P 500

#### Chapitre 1 — Risque et rendement d'investissement univarié

| Fichier | Description |
|---|---|
| `1_Rendements_Financiers.py` | Calcul des rendements discrets et logarithmiques, rendements cumulatifs, annualisation. |
| `2_Moyenne_Variance_Distribution_normale_Skewness_Kurtosis.py` | Moments statistiques des rendements : moyenne, variance, écart-type, skewness, kurtosis. Tests de normalité et visualisation des distributions. |

#### Chapitre 2 — Investissement en portefeuille

| Fichier | Description |
|---|---|
| `1_Composition_portefeuille_Backtesting.py` | Construction d'un portefeuille pondéré, backtesting des rendements cumulatifs, comparaison au benchmark. |
| `2_Correlation_et_co-variance.py` | Matrice de corrélation et de covariance, visualisation heatmap, corrélation glissante. |
| `3_Portefeuille_de_Markowitz.py` | Optimisation de Markowitz via `scipy.optimize` : frontière efficiente, portefeuille à variance minimale, portefeuille à Sharpe maximum. |
| `3bis_Portefeuille_de_Markowitz_Scipy.py` | Variante de l'optimisation Markowitz avec implémentation alternative. |

#### Chapitre 3 — Investissement factoriel

| Fichier | Description |
|---|---|
| `1_CAPM.py` | Modèle CAPM : estimation du bêta, de l'alpha, et du R² via régression OLS. Décomposition risque systématique / idiosyncratique. |
| `2_Modeles_alpha_et_multifactoriels.py` | Modèle de Fama-French à 3 facteurs (Mkt-RF, SMB, HML) via `pandas_datareader`. Comparaison CAPM vs FF3. |
| `3_Extension_du_modele_à_3_facteurs.py` | Extension au modèle de Fama-French à 5 facteurs (+ RMW, CMA). Comparaison CAPM vs FF3 vs FF5 via R² ajusté et alpha annualisé. |

#### Chapitre 4 — Value at Risk

| Fichier | Description |
|---|---|
| `1_Estimation_du_risque_extreme.py` | Drawdown historique, VaR historique et CVaR (Expected Shortfall) aux quantiles 90/95/99. |
| `2_Extensions_de_VaR.py` | Comparaison multi-quantiles VaR/CVaR, VaR paramétrique (loi normale, `norm.ppf`), scaling temporel (règle de la racine carrée du temps). |
| `3_Random_walks.py` | Marches aléatoires, simulation Monte Carlo multi-trajectoires, VaR Monte Carlo. |
| `4_Comprendre_le_risque.py` | Dashboard récapitulatif : drawdown, VaR/CVaR/MC sur le portefeuille custom AAPL/MSFT/AMZN/JPM/JNJ. |

---

### Module 2 — Gestion quantitative des risques

Ce module approfondit la gestion quantitative des risques. Il couvre la théorie moderne du portefeuille, la gestion des risques orientée objectifs, l'identification des risques et les méthodes avancées de gestion.

**Actifs utilisés** : AAPL, MSFT, AMZN, JPM, JNJ | **Période** : 2016–2026 | **Benchmark** : S&P 500

#### Chapitre 1 — Base du risque

| Fichier | Description |
|---|---|
| `1_Quantification_du_risque.py` | Rendement du portefeuille (`.dot()`), matrice de covariance, volatilité annualisée (`w^T · Cov · w`), volatilité glissante 30 jours comparée au S&P 500. |
| `2_Facteurs_de_risque_et_crise_financiere.py` | Dispersion des rendements, décomposition risque systématique/idiosyncratique (CAPM), modèle factoriel OLS sur le VIX comme proxy du stress de marché. |
| `3_Theorie_moderne_du_portefeuille.py` | Trade-off risque/rendement, simulation Monte Carlo de 5 000 portefeuilles aléatoires, optimisation de la frontière efficiente via `scipy.optimize.minimize` (SLSQP), portefeuille à variance minimale et à Sharpe maximum. |

#### Chapitre 2 — Gestion des risques orientée objectifs

| Fichier | Description |
|---|---|
| *À venir* | — |

#### Chapitre 3 — Estimation et identification du risque

| Fichier | Description |
|---|---|
| *À venir* | — |

#### Chapitre 4 — Gestion avancée des risques

| Fichier | Description |
|---|---|
| *À venir* | — |

---

### Module 3 — Modélisation du risque de crédit

| Fichier | Description |
|---|---|
| *À venir* | — |

---

### Module 4 — Modèles GARCH

| Fichier | Description |
|---|---|
| *À venir* | — |

---

## Exécution

```bash
python ".\Module X - Nom du module\Chapitre X - Nom du chapitre\<nom_du_script>.py"
```