import streamlit as st 

#Configuro la pestaña de aplicacion
def config_pestaña():
    st.set_page_config(page_title="AI Ments",
                       page_icon="AI",
                       layout="centered",
                       initial_sidebar_state="collapsed")

#Configuro la barra lateral
def config_pagina():
    modelos = ["llama3-8b-8192", "llama3-70b-8192"]
    st.sidebar.title("Configuración")
    st.sidebar.text("Elige tu modelo de IA")
    elegirModelo = st.sidebar.selectbox('Seleccione un modelo', 
                                        options=modelos, 
                                        index= 0)
    return elegirModelo

#Configuramos el boton de bienvenida
def config_button():
    st.title("MENTs")
    nom = st.text_input("Escribe tu nombre: ")
    if st.button("Enviar"):
        st.write(f"Hola, {nom}! Bienvenido a MENTs.")
    else:
        st.write("Por favor, escribe tu nombre y presiona el botón para enviar.")

#Configuramos el chat
def config_chat():
    st.title("MENTs chat.")
    mensaje = st.chat_input("Escribe tu mensaje aquí:")
    return mensaje

