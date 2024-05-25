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