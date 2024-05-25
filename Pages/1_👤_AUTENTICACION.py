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
    st.subheader("Iniciar Sesión")
    
    # Crear el formulario de inicio de sesión
    email = st.text_input("Email")
    password = st.text_input("Contraseña", type="password")
    
    # Botón de inicio de sesión
    if st.button("Iniciar Sesión"):
        if not email or not password:
            st.error("Por favor, completa los campos obligatorios: Email y Contraseña.")
        elif not is_valid_email(email):
            st.error("Por favor, introduce un email válido.")
        else:
            with st.spinner('Iniciando sesión...'):
                response = login_user(email, password)
                if response.status_code == 200:
                    token_response = response.json()
                    access_token = token_response.get("access_token")
                    token_type = token_response.get("token_type")
                    if access_token and token_type:
                        st.success("¡Inicio de sesión exitoso!")
                        # Almacenar el token en la sesión de Streamlit
                        st.session_state["access_token"] = access_token
                        st.session_state["token_type"] = token_type
                elif response.status_code == 404:
                    st.error("El usuario no existe.")
                elif response.status_code == 401:
                    st.error("Contraseña incorrecta.")
                elif response.status_code == 500:
                    st.error("Estamos teniendo problemas, inténtalo de nuevo.")
                else:
                    st.error("Error al iniciar sesión. Por favor, verifica tus credenciales.")

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
            st.error(
                "Por favor, completa los campos obligatorios: Nombre, Email y Contraseña."
            )
        elif not is_valid_email(email):
            st.error("Por favor, introduce un email válido.")
        elif not is_valid_password(password):
            st.error(
                "La contraseña debe tener mínimo 8 caracteres, incluyendo letras y al menos un número."
            )
        else:
            with st.spinner("Registrando..."):
                response = register_user(
                    name, birth_date, email, phone_number, password
                )
                if response.status_code == 201:
                    st.success("¡Registro exitoso! Ya puedes iniciar sesión.")
                elif response.status_code == 409:
                    st.error("El usuario ya existe.")
                else:
                    st.error(
                        f"Error en el registro: {response.status_code} - {response.text} - inténtalo de nuevo más tarde."
                    )
