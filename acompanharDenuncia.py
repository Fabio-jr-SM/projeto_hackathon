import streamlit as st


def acompanhar_denuncia():

    st.write("Digite seu Telefone para fazer LOGIN")
    tefone = st.text_input('Telefone: ')
    st.button("Login")
