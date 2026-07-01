import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("🗺️ Carte des biens")

data = pd.read_csv("data_geoloc.csv")
carte_data = data[["latitude", "longitude", "prix_eur"]].dropna()

m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# On construit une liste de marqueurs
markers = []
for _, ligne in carte_data.iterrows():
    marker = folium.Marker(
        location=[ligne["latitude"], ligne["longitude"]],
        popup=f"Prix : {ligne['prix_eur']:,.0f} €",
        icon=folium.Icon(color="red", icon="home")
    )
    markers.append(marker)

# On les regroupe et on les passe a st_folium
fg = folium.FeatureGroup(name="Biens")
for marker in markers:
    fg.add_child(marker)

st_folium(m, feature_group_to_add=fg, width=700, height=500)