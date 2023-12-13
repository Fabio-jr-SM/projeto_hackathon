# formularios.py
import streamlit as st
from geopy.geocoders import Nominatim


def obter_coordenadas(endereco):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(endereco)

    if location:
        return location.latitude, location.longitude
    else:
        return None


def criar_formulario_denuncia():
    coordenadas = None

    st.header("Formulário de reclamações")
    d = {}

    d['logradouro'] = st.text_input('logradouro:')
    d['Municipio'] = st.text_input('Municipio:')

    endereco = f"{d['logradouro']} {d['Municipio']}"

    print(endereco)

    if st.button("encontrar Endereço") and endereco:
        coordenadas = obter_coordenadas(endereco)

        if coordenadas:
            st.success(f"Endereço encontrado")
        else:
            st.warning("Não foi possível encontrar o endereço fornecido.")

    if coordenadas:
        with st.expander("Formulário"):
            with st.form("Formulário de reclamação:"):
                d['nome'] = st.text_input('Nome Completo:')
                d['telefone'] = st.text_input('Telefone: ')

                option = st.selectbox(
                    'Selecione o problema',
                    ('Vazamentos', 'Esgotos a céu aberto', 'Buracos nas vias', 'Fiação elétrica',
                     'Lixo acumulado', 'Falta de internet', 'Poda de árvores', 'Outros'),
                    index=None,
                    placeholder="-------",
                )

                d['ponto_referencia'] = st.text_input('Ponto de referência:')
                d['comentário'] = st.text_area('Um comentário: ')

                button_pressed = st.form_submit_button('Enviar')
                if button_pressed:
                    st.write("Denúncia concluída com sucesso!\n")
