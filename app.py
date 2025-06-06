import streamlit as st
from groq import Groq
from functions import configPage as cp, configAI as ca, ments as h

def main():
    cp.config_pestaña()
    clienteUS = ca.user_groq()
    ca.init_state()
    mdl = cp.config_pagina()
    cp.config_button()
    msg = cp.config_chat()
    h.area_chat()

    if msg:
        h.actualizar_historial("user", msg, "🐶")
        chatCompleto= ca.config_model(clienteUS, mdl, msg)
        if chatCompleto:
            with st.chat_message("assistant"):
                respuestaC= st.write_stream(h.gen_respuesta(chatCompleto))
                h.actualizar_historial("assistant", respuestaC, "😸")
                st.rerun()

if __name__ == "__main__":
    main()