import streamlit as st

# Título y autor
st.title("Conversor Universal")
st.write("Esta app fue elaborada por Anderson Bedoya")

# Categorías de conversión
categoria = st.selectbox("Selecciona una categoría:", [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de Datos"
])

# Funciones de conversión
if categoria == "Temperatura":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ])
    if tipo_conversion == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius:")
        fahrenheit = celsius * 9/5 + 32
        st.write(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
    elif tipo_conversion == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit:")
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")
    elif tipo_conversion == "Celsius a Kelvin":
        celsius = st.number_input("Ingresa la temperatura en Celsius:")
        kelvin = celsius + 273.15
        st.write(f"{celsius} grados Celsius son equivalentes a {kelvin} Kelvin.")
    elif tipo_conversion == "Kelvin a Celsius":
        kelvin = st.number_input("Ingresa la temperatura en Kelvin:")
        celsius = kelvin - 273.15
        st.write(f"{kelvin} Kelvin son equivalentes a {celsius} grados Celsius.")

# Repetir este bloque de código para cada categoría y tipo de conversión

