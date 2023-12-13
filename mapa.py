# mapa.py
import streamlit as st
import streamlit_folium
import folium


def exibir_mapa_reclamacoes():
    st.header("Mapa de Reclamações")
    # Lógica para exibir o mapa de reclamações aqui

    # Criando um mapa Folium
    mapa = folium.Map(location=[-15.6010, -56.0974], zoom_start=12, width=900)
    # folium.Marker([0, 0], popup="endereco").add_to(mapa)
    st_folium = streamlit_folium.st_folium(mapa)
