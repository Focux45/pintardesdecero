import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Pintando con estilo', layout='wide')
st.title('Vamos a dibujar algo pro')
st.subheader("Dibuja en el panel")

# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 10)
#stroke_color = '#00000' # Set background color to white
bg_color = '#ffffff'
stroke_color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", stroke_color)
with st.sidebar:
    st.subheader([stroke_width])

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=400,
    width=400,
    key="canvas",
)
