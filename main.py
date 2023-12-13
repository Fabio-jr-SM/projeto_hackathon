# main.py
import streamlit as st
from streamlit_option_menu import option_menu
from formularios import *
from mapa import *

st.title("Seja Bem-vindo(a)")
st.write("Disk Denúncia Aqui você pode...")

# horizontal menu
selected2 = option_menu(None, ["Mapa de Reclamações", "Formulario de denuncia", "Acompanhar Denuncia"],
                        icons=['map', 'a', "list-task"],
                        menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Mapa de Reclamações":
    exibir_mapa_reclamacoes()

if selected2 == "Formulario de denuncia":
    criar_formulario_denuncia()

if selected2 == "Acompanhar Denuncia":
    st.header("Acompanhar Reclamações")
