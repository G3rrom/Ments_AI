import streamlit as st
from groq import Groq

#Inicia el usuario de Groq
def user_groq():
    clave_secreta = st.secrets["API_KEY"]
    return Groq(api_key=clave_secreta)

#retorna la respuesta del modelo AI
def config_model(cliente, modelo, msj):
    return cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": msj}],
        stream=True
    )

#Inicializa el estado de la sesión para almacenar mensajes
def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
