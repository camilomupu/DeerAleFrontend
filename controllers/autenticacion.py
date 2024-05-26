import re
import requests
import streamlit as st

API_URL = "https://deeralebackend.azurewebsites.net"
REGISTER_ENDPOINT = "/user/register/"
LOGIN_ENDPOINT = "/user/login"


# Función para validar el formato del correo electrónico
def is_valid_email(email):
    regex = r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.match(regex, email) is not None


# Función para validar la contraseña
def is_valid_password(password):
    # Ejemplo: al menos 8 caracteres, con letras y números
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


# Función para registrar un nuevo usuario
def register_user(name, birth_date, email, phone_number, password):
    user_data = {
        "name": name,
        "email": email,
        "password": password,
    }

    # Solo agregar birth_date y phone_number si están proporcionados
    if birth_date:
        user_data["birth_date"] = birth_date.isoformat()  # Convertir a string ISO
    if phone_number:
        user_data["phone_number"] = phone_number

    response = requests.post(API_URL + REGISTER_ENDPOINT, json=user_data)
    return response


# Función para iniciar sesión
def login_user(email, password):
    login_data = {
        "username": email,
        "password": password,
    }
    response = requests.post(API_URL + LOGIN_ENDPOINT, data=login_data)
    return response


def handle_login_response(response):
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


def show_login_form():
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
            with st.spinner("Iniciando sesión..."):
                response = login_user(email, password)
                handle_login_response(response)


def handle_registration_response(response):
    if response.status_code == 201:
        st.success("¡Registro exitoso! Ya puedes iniciar sesión.")
    elif response.status_code == 409:
        st.error("El usuario ya existe.")
    else:
        st.error(
            f"Error en el registro: {response.status_code} - {response.text} - inténtalo de nuevo más tarde."
        )


def show_registration_form():
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
                handle_registration_response(response)