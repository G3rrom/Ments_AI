import streamlit as st
from groq import Groq

def mostrar_historial():
    for mensaje in st.session_state.messages:
        with st.chat_message(mensaje["role"], avatar=mensaje["avatar"]):
            st.markdown(mensaje["content"])

def actualizar_historial(rol, contenido, avatar):
    st.session_state.messages.append({"role": rol, "content": contenido, "avatar": avatar})

def area_chat():
    content_chat = st.container(height=400, border=True)
    with content_chat:
        mostrar_historial()

def gen_respuesta(chat_completo):
    respuestaC= ""
    for frase in chat_completo:
        if frase.choices[0].delta.content:
            respuestaC += frase.choices[0].delta.content
            yield frase.choices[0].delta.content
    return respuestaC