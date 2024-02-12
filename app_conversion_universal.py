import streamlit as st


# Configuración de la página para centrar la interfaz
st.set_page_config(layout="centered")


def conversiones_temperatura(valor, tipo_conversion):
    if tipo_conversion == "Celsius a Fahrenheit":
        return valor * 9/5 + 32
    elif tipo_conversion == "Fahrenheit a Celsius":
        return (valor - 32) * 5/9
    elif tipo_conversion == "Celsius a Kelvin":
        return valor + 273.15
    elif tipo_conversion == "Kelvin a Celsius":
        return valor - 273.15

def conversiones_longitud(valor, tipo_conversion):
    if tipo_conversion == "Pies a metros":
        return valor * 0.3048
    elif tipo_conversion == "Metros a pies":
        return valor / 0.3048
    elif tipo_conversion == "Pulgadas a centímetros":
        return valor * 2.54
    elif tipo_conversion == "Centímetros a pulgadas":
        return valor / 2.54

def conversiones_peso(valor, tipo_conversion):
    if tipo_conversion == "Libras a kilogramos":
        return valor * 0.453592
    elif tipo_conversion == "Kilogramos a libras":
        return valor / 0.453592
    elif tipo_conversion == "Onzas a gramos":
        return valor * 28.3495
    elif tipo_conversion == "Gramos a onzas":
        return valor / 28.3495

def conversiones_volumen(valor, tipo_conversion):
    if tipo_conversion == "Galones a litros":
        return valor * 3.78541
    elif tipo_conversion == "Litros a galones":
        return valor / 3.78541
    elif tipo_conversion == "Pulgadas cúbicas a centímetros cúbicos":
        return valor * 16.3871
    elif tipo_conversion == "Centímetros cúbicos a pulgadas cúbicas":
        return valor / 16.3871

def conversiones_tiempo(valor, tipo_conversion):
    if tipo_conversion == "Horas a minutos":
        return valor * 60
    elif tipo_conversion == "Minutos a segundos":
        return valor * 60
    elif tipo_conversion == "Días a horas":
        return valor * 24
    elif tipo_conversion == "Semanas a días":
        return valor * 7

def conversiones_velocidad(valor, tipo_conversion):
    if tipo_conversion == "Millas por hora a kilómetros por hora":
        return valor * 1.60934
    elif tipo_conversion == "Kilómetros por hora a metros por segundo":
        return valor * 0.277778
    elif tipo_conversion == "Nudos a millas por hora":
        return valor * 1.15078
    elif tipo_conversion == "Metros por segundo a pies por segundo":
        return valor * 3.28084

def conversiones_area(valor, tipo_conversion):
    if tipo_conversion == "Metros cuadrados a pies cuadrados":
        return valor * 10.7639
    elif tipo_conversion == "Pies cuadrados a metros cuadrados":
        return valor / 10.7639
    elif tipo_conversion == "Kilómetros cuadrados a millas cuadradas":
        return valor * 0.386102
    elif tipo_conversion == "Millas cuadradas a kilómetros cuadrados":
        return valor / 0.386102

def conversiones_energia(valor, tipo_conversion):
    if tipo_conversion == "Julios a calorías":
        return valor * 0.000239006
    elif tipo_conversion == "Calorías a kilojulios":
        return valor * 0.004184
    elif tipo_conversion == "Kilovatios-hora a megajulios":
        return valor * 3.6
    elif tipo_conversion == "Megajulios a kilovatios-hora":
        return valor / 3.6

def conversiones_presion(valor, tipo_conversion):
    if tipo_conversion == "Pascales a atmósferas":
        return valor * 0.00000986923
    elif tipo_conversion == "Atmósferas a pascales":
        return valor * 101325
    elif tipo_conversion == "Barras a libras por pulgada cuadrada":
        return valor * 14.5038
    elif tipo_conversion == "Libras por pulgada cuadrada a bares":
        return valor * 0.0689476

def conversiones_tamaño_datos(valor, tipo_conversion):
    if tipo_conversion == "Megabytes a gigabytes":
        return valor * 0.001
    elif tipo_conversion == "Gigabytes a terabytes":
        return valor * 0.001
    elif tipo_conversion == "Kilobytes a megabytes":
        return valor * 0.001
    elif tipo_conversion == "Terabytes a petabytes":
        return valor * 0.001

categorias = [
    "Temperatura",
    "Longitud",
    "Peso/Masa",
    "Volumen",
    "Tiempo",
    "Velocidad",
    "Área",
    "Energía",
    "Presión",
    "Tamaño de datos"
]

tipo_conversion_temperatura = [
    "Celsius a Fahrenheit",
    "Fahrenheit a Celsius",
    "Celsius a Kelvin",
    "Kelvin a Celsius"
]

tipo_conversion_longitud = [
    "Pies a metros",
    "Metros a pies",
    "Pulgadas a centímetros",
    "Centímetros a pulgadas"
]

tipo_conversion_peso = [
    "Libras a kilogramos",
    "Kilogramos a libras",
    "Onzas a gramos",
    "Gramos a onzas"
]

tipo_conversion_volumen = [
    "Galones a litros",
    "Litros a galones",
    "Pulgadas cúbicas a centímetros cúbicos",
    "Centímetros cúbicos a pulgadas cúbicas"
]

tipo_conversion_tiempo = [
    "Horas a minutos",
    "Minutos a segundos",
    "Días a horas",
    "Semanas a días"
]

tipo_conversion_velocidad = [
    "Millas por hora a kilómetros por hora",
    "Kilómetros por hora a metros por segundo",
    "Nudos a millas por hora",
    "Metros por segundo a pies por segundo"
]

tipo_conversion_area = [
    "Metros cuadrados a pies cuadrados",
    "Pies cuadrados a metros cuadrados",
    "Kilómetros cuadrados a millas cuadradas",
    "Millas cuadradas a kilómetros cuadrados"
]

tipo_conversion_energia = [
    "Julios a calorías",
    "Calorías a kilojulios",
    "Kilovatios-hora a megajulios",
    "Megajulios a kilovatios-hora"
]

tipo_conversion_presion = [
    "Pascales a atmósferas",
    "Atmósferas a pascales",
    "Barras a libras por pulgada cuadrada",
    "Libras por pulgada cuadrada a bares"
]

tipo_conversion_tamaño_datos = [
    "Megabytes a gigabytes",
    "Gigabytes a terabytes",
    "Kilobytes a megabytes",
    "Terabytes a petabytes"
]

categoria_seleccionada = st.sidebar.selectbox("Selecciona una categoría", categorias)

if categoria_seleccionada == "Temperatura":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_temperatura)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_temperatura(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Longitud":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_longitud)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_longitud(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Peso/Masa":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_peso)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_peso(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Volumen":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_volumen)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_volumen(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Tiempo":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_tiempo)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_tiempo(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Velocidad":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_velocidad)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_velocidad(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Área":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_area)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_area(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Energía":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_energia)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_energia(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Presión":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_presion)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_presion(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")

elif categoria_seleccionada == "Tamaño de datos":
    tipo_conversion = st.sidebar.selectbox("Selecciona un tipo de conversión", tipo_conversion_tamaño_datos)
    valor = st.sidebar.number_input("Ingresa el valor a convertir")
    resultado = conversiones_tamaño_datos(valor, tipo_conversion)
    st.sidebar.write(f"El resultado es: {resultado}")
