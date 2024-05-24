import streamlit as st
from controllers.autenticacion import *

st.set_page_config(
    page_title="Autenticación",
    page_icon="👤",
)

# Título de la página
st.title("👤 Autenticación")

# Seleccionar entre Iniciar Sesión y Registrarse
option = st.selectbox(
    "¿Qué te gustaría hacer?",
    ("Iniciar Sesión", "Registrarse")
)

# Mostrar el formulario correspondiente basado en la selección
if option == "Iniciar Sesión":
    st.subheader("Iniciar Sesión")
    # Aquí añadiremos el formulario de inicio de sesión después

elif option == "Registrarse":
    st.subheader("Registrarse")

    # Crear el formulario de registro
    name = st.text_input("Nombre")
    email = st.text_input("Email")
    password = st.text_input("Contraseña", type="password")

    # Checkbox para mostrar campos opcionales
    show_birth_date = st.checkbox("Agregar fecha de nacimiento (opcional)")
    show_phone_number = st.checkbox("Agregar número de teléfono (opcional)")

    birth_date = None
    phone_number = ""

    if show_birth_date:
        birth_date = st.date_input("Fecha de Nacimiento (YYYY-MM-DD)")

    if show_phone_number:
        phone_number = st.text_input("Número de Teléfono")

    # Botón de registro
    if st.button("Registrarse"):
        if not name or not email or not password:
            st.error("Por favor, completa los campos obligatorios: Nombre, Email y Contraseña.")
        elif not is_valid_email(email):
            st.error("Por favor, introduce un email válido.")
        elif not is_valid_password(password):
            st.error("La contraseña debe tener mínimo 8 caracteres, incluyendo letras y al menos un número.")
        else:
            with st.spinner('Registrando...'):
                response = register_user(name, birth_date, email, phone_number, password)
                if response.status_code == 201:
                    st.success("¡Registro exitoso! Ya puedes iniciar sesión.")
                elif response.status_code == 409:
                    st.error("El usuario ya existe.")
                else:
                    st.error(f"Error en el registro: {response.status_code} - {response.text} - inténtalo de nuevo más tarde.")
