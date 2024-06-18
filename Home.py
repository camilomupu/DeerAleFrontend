import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.sidebar.success("Navega por nuestro menú.")

# Título y descripción principal
st.markdown(
    "<h1 style='text-align: center;'>Bienvenidos a Deer Ale</h1>",
    unsafe_allow_html=True,
)

# Mostrar imagen
img = "http://imgfz.com/i/yvq5g0B.png"
# Centro y redimensiono la imagen usando HTML y CSS
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" width="400">
    </div>
    """,
    unsafe_allow_html=True,
)

# Descripción de la empresa
st.write(
    """
En el vasto mundo de la moda, Deer Ale se erige como un oasis para los amantes del calzado. 
Nuestra pasión por la elegancia y la comodidad se refleja en cada par de zapatos que ofrecemos. 
Desde clásicos atemporales hasta las últimas tendencias de la moda, en Deer Ale, encontrarás 
el calzado perfecto para cada ocasión.

Explora nuestra amplia colección que abarca desde zapatillas deportivas de alta tecnología 
hasta elegantes tacones para destacar en eventos especiales. Nos enorgullece ofrecer no solo 
una variedad impresionante de estilos, sino también un compromiso inquebrantable con la calidad. 
Cada par de zapatos Deer Ale está diseñado para brindar confort durante todo el día sin sacrificar el estilo.

Navegar por nuestro ecommerce es tan fácil como deslizarte en tu par favorito de zapatos. 
Con un proceso de compra intuitivo, opciones de pago seguras y envío rápido, hacemos que la 
experiencia de comprar zapatos sea tan placentera como usarlos. Además, nuestro equipo de atención 
al cliente está siempre listo para ayudarte, brindando asesoramiento experto y garantizando tu 
satisfacción en cada paso.

En Deer Ale, no solo vendemos zapatos, creamos experiencias de moda. Únete a nosotros mientras 
caminamos juntos por el mundo de la elegancia, la tendencia y el confort. Tu próximo par de zapatos 
perfectos te espera en Deer Ale, donde la moda se encuentra con la comodidad.
"""
)

# Información adicional y widgets interactivos
st.markdown("### Descubre nuestras categorías:")
st.markdown(
    """
- **Zapatillas deportivas de alta tecnología**
- **Elegantes tacones para eventos especiales**
- **Clásicos atemporales**
- **Últimas tendencias de la moda**
"""
)

# Botón de llamada a la acción
if st.button("Explorar el catálogo"):
    st.write("¡Explora nuestra colección ahora!")

# Sección de contacto
st.markdown("### ¿Tienes alguna pregunta?")
st.write(
    "Nuestro equipo de atención al cliente está siempre listo para ayudarte. [Contáctanos](mailto:deerale23@gmail.com)"
)

# Pie de página
st.markdown(
    """
---
**Deer Ale** - Elegancia y comodidad en cada paso
"""
)
