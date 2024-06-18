import requests
import streamlit as st
from datetime import datetime

API_URL = "https://backend-deer-ale.vercel.app"


# Función para obtener la información del usuario actual
def get_user_info(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(API_URL + "/user/me/", headers=headers)
    return response.json()


# Función para actualizar la información del usuario
def update_user_info(token, user_data):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.patch(
        API_URL + "/user/update/me/", json=user_data, headers=headers
    )
    return response


# Función para cambiar la contraseña del usuario
def change_user_password(token, old_password, new_password):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "old_password": old_password,
        "new_password": new_password,
    }
    response = requests.put(
        API_URL + "/user/change/password/", json=data, headers=headers
    )
    return response


def show_update_info_screen(token):
    st.header("Actualizar mi información")

    with st.spinner("Cargando información..."):
        user_info = get_user_info(token)

    if user_info:
        with st.form("update_form"):
            name = st.text_input("Nombre", user_info.get("name", ""))
            email = st.text_input("Email", user_info.get("email", ""))

            birth_date_str = user_info.get("birth_date")
            if birth_date_str:
                birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            else:
                birth_date = None

            birth_date = st.date_input("Fecha de Nacimiento", birth_date)
            phone_number = st.text_input(
                "Número de Teléfono", user_info.get("phone_number", "")
            )

            submitted = st.form_submit_button("Actualizar")
            if submitted:
                user_data = {
                    "name": name,
                    "email": email,
                }
                if birth_date:
                    user_data["birth_date"] = birth_date.isoformat()
                if phone_number:
                    user_data["phone_number"] = phone_number

                handle_response(update_user_info(token, user_data))


def show_change_password_screen(token):
    st.header("Cambiar contraseña")

    with st.form("password_form"):
        old_password = st.text_input("Contraseña actual", type="password")
        new_password = st.text_input("Nueva contraseña", type="password")
        confirm_password = st.text_input("Confirmar nueva contraseña", type="password")

        submitted = st.form_submit_button("Cambiar Contraseña")
        if submitted:
            if new_password != confirm_password:
                st.error("Las nuevas contraseñas no coinciden.")
            else:
                handle_response(change_user_password(token, old_password, new_password))


def handle_response(response):
    if response.status_code == 200:
        st.success("¡Operación exitosa!")
    elif response.status_code == 404:
        st.error("Este usuario no existe.")
    elif response.status_code == 401:
        st.error("Contraseña incorrecta.")
    elif response.status_code == 500:
        st.error("Estamos teniendo problemas, inténtalo de nuevo.")
    else:
        st.error(
            f"Error: {response.status_code} - {response.text} - inténtalo de nuevo más tarde."
        )
