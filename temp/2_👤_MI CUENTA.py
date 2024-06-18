import streamlit as st
from controllers.cuenta import *
from datetime import datetime

st.set_page_config(page_title="Mi Cuenta", page_icon="👤")

# Título de la página
st.title("👤 Mi Cuenta")

# Verificar si el usuario ha iniciado sesión
if "access_token" not in st.session_state:
    st.warning("Por favor, inicia sesión primero.")
else:
    token = st.session_state["access_token"]

    # Crear un menú en el sidebar
    st.sidebar.title("Menú")
    menu_option = st.sidebar.selectbox(
        "Selecciona una opción", ("Actualizar mi información", "Cambiar contraseña")
    )

    # Mostrar el contenido basado en la opción seleccionada
    if menu_option == "Actualizar mi información":
        show_update_info_screen(token)
    elif menu_option == "Cambiar contraseña":
        show_change_password_screen(token)
