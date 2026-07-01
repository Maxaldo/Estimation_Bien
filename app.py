import streamlit as st

# Déclaration des pages
Accueil = st.Page(
    "pages/accueil.py",
    title="Accueil",
    icon="🏠",
    default=True
)
Estimation = st.Page(
    "pages/estimation.py",
    title="Estimation",
    icon="📊"
)
Carte = st.Page(
    "pages/carte.py",
    title="Carte",
    icon="🗺️"
)

# Barre de navigation
pg = st.navigation(
    [Accueil, Estimation, Carte],
    position="sidebar"
)

# Lance la page sélectionnée
pg.run()