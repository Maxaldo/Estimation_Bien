# 🏠 ImmoEstim — Estimation de biens immobiliers par Machine Learning

Application web d'estimation du prix de biens immobiliers à Paris, construite avec **scikit-learn** pour la modélisation et **Streamlit** pour l'interface. Le projet couvre l'ensemble de la chaîne : des données brutes à une application web interactive avec cartographie.

---

## 📋 Sommaire

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Stack technique](#-stack-technique)
- [Architecture du projet](#-architecture-du-projet)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Fonctionnement du modèle](#-fonctionnement-du-modèle)
- [Structure des pages](#-structure-des-pages)
- [Améliorations possibles](#-améliorations-possibles)
- [Auteur](#-auteur)

---

## 🎯 Aperçu

ImmoEstim estime le prix d'un bien immobilier parisien à partir de ses caractéristiques (surface, nombre de pièces, étage, DPE, code postal…). Le modèle est entraîné sur un jeu de données d'annonces réelles, puis exposé via une interface web multi-pages proposant :

- un **formulaire d'estimation** qui renvoie un prix prédit,
- une **carte interactive** des biens du jeu de données,
- une **page d'accueil** présentant le projet.

---

## ✨ Fonctionnalités

- **Estimation instantanée** du prix d'un bien à partir de ses caractéristiques.
- **Prix au m²** calculé automatiquement.
- **Cartographie interactive** des biens (Folium / `st.map`).
- **Interface multi-pages** avec barre de navigation latérale.
- **Séparation claire** entre entraînement (`train.py`) et prédiction (`pred.py`).
- **Encodeurs persistés** pour garantir un encodage identique à l'entraînement et à la prédiction.

---

## 🛠 Stack technique

| Domaine | Technologies |
|---|---|
| Langage | Python 3 |
| Machine Learning | scikit-learn (`GradientBoostingRegressor`, `LabelEncoder`) |
| Manipulation de données | pandas |
| Interface web | Streamlit |
| Cartographie | Folium, streamlit-folium |
| Géocodage | API Adresse (api-adresse.data.gouv.fr) |
| Persistance | joblib |

---

## 📁 Architecture du projet

```
ESTIMATION_BIEN/
├── app.py                  # Point d'entrée : navigation multi-pages
├── train.py                # Entraînement du modèle + sauvegarde
├── pred.py                 # Chargement du modèle + fonction de prédiction
├── data.csv                # Jeu de données (annonces immobilières)
├── requirements.txt        # Dépendances Python
├── utils/                  # Modèle et encodeurs sauvegardés (généré par train.py)
│   ├── model.joblib
│   ├── le_etage.joblib
│   └── le_type_bien.joblib
└── pages/                  # Pages de l'application
    ├── accueil.py          # Page d'accueil (présentation)
    ├── estimation.py       # Formulaire d'estimation
    └── carte.py            # Carte interactive des biens
```

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Maxaldo/Estimation_Bien.git
cd Estimation_Bien
```

### 2. (Recommandé) Créer un environnement virtuel

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🚀 Utilisation

### Étape 1 — Entraîner le modèle

Cette commande lit `data.csv`, entraîne le modèle et sauvegarde le modèle ainsi que les encodeurs dans le dossier `utils/` :

```bash
python train.py
```

> À lancer une seule fois, ou à chaque fois que les données changent.

### Étape 2 — Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvre automatiquement dans le navigateur (par défaut `http://localhost:8501`).

### (Optionnel) Tester la prédiction en ligne de commande

```bash
python pred.py
```

---

## 🧠 Fonctionnement du modèle

### Préparation des données

- Suppression des colonnes non pertinentes (`url`, `prix_m2`, coordonnées, etc.).
- Filtrage des valeurs aberrantes (prix supérieurs à 5 000 000 €).
- Encodage des variables catégorielles :
  - **DPE** → encodage ordinal manuel (`A`=1, `B`=2, … `G`=7),
  - **type de bien** et **étage** → `LabelEncoder`.
- Remplacement des valeurs manquantes.

### Modèle

Le modèle utilisé est un **Gradient Boosting Regressor** :

```python
GradientBoostingRegressor(
    n_estimators=300,
    learning_rate=0.01,
    max_depth=5,
    random_state=42
)
```

### Persistance

Le modèle **et** les encodeurs sont sauvegardés avec `joblib`. C'est essentiel : au moment de la prédiction, on réutilise exactement les mêmes encodeurs qu'à l'entraînement (`transform`, et non `fit_transform`), pour garantir la cohérence de l'encodage.

---

## 🗂 Structure des pages

| Page | Rôle |
|---|---|
| **Accueil** | Présentation du projet et de ses fonctionnalités. |
| **Estimation** | Formulaire de saisie des caractéristiques et affichage du prix estimé. Les listes déroulantes sont alimentées par les classes des encodeurs, ce qui évite les valeurs inconnues du modèle. |
| **Carte** | Visualisation géographique des biens du jeu de données sur une carte de Paris. |

---

## 🔮 Améliorations possibles

- Enrichir la carte avec des **popups de prix** et une coloration par gamme de prix.
- Ajouter une **estimation de l'intervalle de confiance** autour du prix prédit.
- Comparer plusieurs modèles (Random Forest, XGBoost, LightGBM) et sélectionner le meilleur.
- Gérer proprement les **valeurs inconnues** lors de la prédiction (adresse ou étage absent du jeu d'entraînement).
- Déployer l'application (Streamlit Community Cloud, Docker…).
- Ajouter des **métriques d'évaluation** (MAE, RMSE, R²) affichées dans l'application.

---

## 👤 Auteur

**Max Sogbossi**
Développeur Full Stack & Data / ML — Mastère Expert en Informatique et Systèmes d'Information (ITIC Paris)

- GitHub : [github.com/Maxaldo](https://github.com/Maxaldo)
- Portfolio : [maxaldo.github.io/portfolio](https://maxaldo.github.io/portfolio)

---

*Projet réalisé dans le cadre du Mastère Expert en Informatique et Systèmes d'Information — ITIC Paris.*
