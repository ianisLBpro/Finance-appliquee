# Installation

Ce guide explique comment récupérer ce projet et configurer l'environnement Python pour exécuter les scripts.

## Prérequis

- **Python 3.10+** — [Télécharger Python](https://www.python.org/downloads/)
- **Git** — [Télécharger Git](https://git-scm.com/downloads)

> Le projet a été développé avec Python 3.14.0. Les versions 3.10 et supérieures sont compatibles.

---

## 1. Cloner le dépôt

```bash
git clone https://github.com/ianisLBpro/Gestion-de-portefeuille.git
cd Gestion-de-portefeuille
```

---

## 2. Créer un environnement virtuel

**Windows :**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux :**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 4. Exécuter un script

Depuis la racine du projet, lancez par exemple :

```bash
python "Module 1 - Introduction à la gestion du risque/Chapitre 1 - Risque et rendement d'investissement univariés/1_Rendements_Financiers.py"
```

---

## Dépendances

| Librairie | Version | Usage |
|---|---|---|
| `numpy` | 2.4.3 | Calcul numérique |
| `pandas` | 3.0.1 | Manipulation de données |
| `matplotlib` | 3.10.8 | Visualisation |
| `seaborn` | 0.13.2 | Visualisation (heatmaps, corrélations) |
| `scipy` | 1.17.1 | Optimisation, statistiques |
| `yfinance` | 1.2.0 | Téléchargement de données boursières |
| `pandas-datareader` | 0.10.0 | Accès aux données Fama-French |
| `statsmodels` | 0.14.6 | Régressions, modèles économétriques |
