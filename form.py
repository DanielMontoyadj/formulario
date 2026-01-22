import streamlit as st

st.title("Formulario de Regristro Estudiantil IP-2026")

nombre = st.text_input("Nombre Completo")
edad = st.number_input("Edad", min_value=0, max_value=80)
carrera = st.selectbox("Carrera", ["Ingenieria en Computación", "Diseño web", "Tecnico en Informatica"])
comentarios = st.text_area("Comentario adicional (opcional)")

if st.button("Enviar"):
    st.write("###Datos Registrados:")
    st.write(f"**Nombre Completo**: {nombre}")
    st.write(f"**Edad** : {edad}")
    st.write(f"**Carrera** : {carrera}")
    st.write(f"**Comentario** : {comentarios}")
    st.success("Formulario enviado con exito")