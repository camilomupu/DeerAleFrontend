import streamlit as st
from controllers.autenticacion import *

st.set_page_config(
    page_title="Autenticación",
    page_icon="👤",
)

# Título de la página
st.title("👤 Autenticación")

# Seleccionar entre Iniciar Sesión y Registrarse
option = st.selectbox("¿Qué te gustaría hacer?", ("Iniciar Sesión", "Registrarse"))

# Mostrar el formulario correspondiente basado en la selección
if option == "Iniciar Sesión":
    show_login_form()

elif option == "Registrarse":
    show_registration_form()