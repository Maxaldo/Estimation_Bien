import streamlit as st
import joblib
from pred import ft_pred

st.title(" Estimer le prix d'un bien")

le_type_bien = joblib.load("utils/le_type_bien.joblib")
type_bien = st.selectbox("Type de bien", le_type_bien.classes_)

surface_m2 = st.number_input("Surface (m²)", 10.0, 500.0, 50.0)
nb_pieces = st.number_input("Nombre de pièces", 1, 15, 2)
nb_chambres = st.number_input("Nombre de chambres", 0, 10, 1)
dpe = st.selectbox("DPE", ["A", "B", "C", "D", "E", "F", "G"])

le_etage = joblib.load("utils/le_etage.joblib")
etage = st.selectbox("Étage", le_etage.classes_)

code_postal = st.number_input("Code postal", 75001, 75020)

if st.button("Estimer le prix"):
    estimation = ft_pred(type_bien, surface_m2, nb_pieces, nb_chambres, etage, dpe, code_postal)
    st.success(f"Prix estimé : {estimation:,.0f} €")