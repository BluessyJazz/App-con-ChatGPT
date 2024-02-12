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


elif categoria == "Longitud":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Pies a Metros",
        "Metros a Pies",
        "Pulgadas a Centímetros",
        "Centímetros a Pulgadas"
    ])
    if tipo_conversion == "Pies a Metros":
        pies = st.number_input("Ingresa la longitud en Pies:")
        metros = pies * 0.3048
        st.write(f"{pies} pies son equivalentes a {metros} metros.")
    elif tipo_conversion == "Metros a Pies":
        metros = st.number_input("Ingresa la longitud en Metros:")
        pies = metros / 0.3048
        st.write(f"{metros} metros son equivalentes a {pies} pies.")
    elif tipo_conversion == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingresa la longitud en Pulgadas:")
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas} pulgadas son equivalentes a {centimetros} centímetros.")
    elif tipo_conversion == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingresa la longitud en Centímetros:")
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros} centímetros son equivalentes a {pulgadas} pulgadas.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Peso/Masa":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Libras a Kilogramos",
        "Kilogramos a Libras",
        "Onzas a Gramos",
        "Gramos a Onzas"
    ])
    if tipo_conversion == "Libras a Kilogramos":
        libras = st.number_input("Ingresa el peso en Libras:")
        kilogramos = libras * 0.453592
        st.write(f"{libras} libras son equivalentes a {kilogramos} kilogramos.")
    elif tipo_conversion == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingresa el peso en Kilogramos:")
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos} kilogramos son equivalentes a {libras} libras.")
    elif tipo_conversion == "Onzas a Gramos":
        onzas = st.number_input("Ingresa el peso en Onzas:")
        gramos = onzas * 28.3495
        st.write(f"{onzas} onzas son equivalentes a {gramos} gramos.")
    elif tipo_conversion == "Gramos a Onzas":
        gramos = st.number_input("Ingresa el peso en Gramos:")
        onzas = gramos / 28.3495
        st.write(f"{gramos} gramos son equivalentes a {onzas} onzas.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Volumen":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Galones a Litros",
        "Litros a Galones",
        "Pulgadas cúbicas a Centímetros cúbicos",
        "Centímetros cúbicos a Pulgadas cúbicas"
    ])
    if tipo_conversion == "Galones a Litros":
        galones = st.number_input("Ingresa el volumen en Galones:")
        litros = galones * 3.78541
        st.write(f"{galones} galones son equivalentes a {litros} litros.")
    elif tipo_conversion == "Litros a Galones":
        litros = st.number_input("Ingresa el volumen en Litros:")
        galones = litros / 3.78541
        st.write(f"{litros} litros son equivalentes a {galones} galones.")
    elif tipo_conversion == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingresa el volumen en Pulgadas cúbicas:")
        centimetros_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas} pulgadas cúbicas son equivalentes a {centimetros_cubicos} centímetros cúbicos.")
    elif tipo_conversion == "Centímetros cúbicos a Pulgadas cúbicas":
        centimetros_cubicos = st.number_input("Ingresa el volumen en Centímetros cúbicos:")
        pulgadas_cubicas = centimetros_cubicos / 16.3871
        st.write(f"{centimetros_cubicos} centímetros cúbicos son equivalentes a {pulgadas_cubicas} pulgadas cúbicas.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Tiempo":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Horas a Minutos",
        "Minutos a Segundos",
        "Días a Horas",
        "Semanas a Días"
    ])
    if tipo_conversion == "Horas a Minutos":
        horas = st.number_input("Ingresa la cantidad de horas:")
        minutos = horas * 60
        st.write(f"{horas} horas son equivalentes a {minutos} minutos.")
    elif tipo_conversion == "Minutos a Segundos":
        minutos = st.number_input("Ingresa la cantidad de minutos:")
        segundos = minutos * 60
        st.write(f"{minutos} minutos son equivalentes a {segundos} segundos.")
    elif tipo_conversion == "Días a Horas":
        dias = st.number_input("Ingresa la cantidad de días:")
        horas = dias * 24
        st.write(f"{dias} días son equivalentes a {horas} horas.")
    elif tipo_conversion == "Semanas a Días":
        semanas = st.number_input("Ingresa la cantidad de semanas:")
        dias = semanas * 7
        st.write(f"{semanas} semanas son equivalentes a {dias} días.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Velocidad":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Millas por hora a Kilómetros por hora",
        "Kilómetros por hora a Metros por segundo",
        "Nudos a Millas por hora",
        "Metros por segundo a Pies por segundo"
    ])
    if tipo_conversion == "Millas por hora a Kilómetros por hora":
        mph = st.number_input("Ingresa la velocidad en Millas por hora:")
        kph = mph * 1.60934
        st.write(f"{mph} millas por hora son equivalentes a {kph} kilómetros por hora.")
    elif tipo_conversion == "Kilómetros por hora a Metros por segundo":
        kph = st.number_input("Ingresa la velocidad en Kilómetros por hora:")
        mps = kph / 3.6
        st.write(f"{kph} kilómetros por hora son equivalentes a {mps} metros por segundo.")
    elif tipo_conversion == "Nudos a Millas por hora":
        nudos = st.number_input("Ingresa la velocidad en Nudos:")
        mph = nudos * 1.15078
        st.write(f"{nudos} nudos son equivalentes a {mph} millas por hora.")
    elif tipo_conversion == "Metros por segundo a Pies por segundo":
        mps = st.number_input("Ingresa la velocidad en Metros por segundo:")
        fps = mps * 3.28084
        st.write(f"{mps} metros por segundo son equivalentes a {fps} pies por segundo.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Área":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Metros cuadrados a Pies cuadrados",
        "Pies cuadrados a Metros cuadrados",
        "Kilómetros cuadrados a Millas cuadradas",
        "Millas cuadradas a Kilómetros cuadrados"
    ])
    if tipo_conversion == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingresa el área en Metros cuadrados:")
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f"{metros_cuadrados} metros cuadrados son equivalentes a {pies_cuadrados} pies cuadrados.")
    elif tipo_conversion == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingresa el área en Pies cuadrados:")
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f"{pies_cuadrados} pies cuadrados son equivalentes a {metros_cuadrados} metros cuadrados.")
    elif tipo_conversion == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingresa el área en Kilómetros cuadrados:")
        millas_cuadradas = km_cuadrados * 0.386102
        st.write(f"{km_cuadrados} kilómetros cuadrados son equivalentes a {millas_cuadradas} millas cuadradas.")
    elif tipo_conversion == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingresa el área en Millas cuadradas:")
        km_cuadrados = millas_cuadradas / 0.386102
        st.write(f"{millas_cuadradas} millas cuadradas son equivalentes a {km_cuadrados} kilómetros cuadrados.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Energía":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Julios a Calorías",
        "Calorías a Kilojulios",
        "Kilovatios-hora a Megajulios",
        "Megajulios a Kilovatios-hora"
    ])
    if tipo_conversion == "Julios a Calorías":
        julios = st.number_input("Ingresa la energía en Julios:")
        calorias = julios * 0.239006
        st.write(f"{julios} julios son equivalentes a {calorias} calorías.")
    elif tipo_conversion == "Calorías a Kilojulios":
        calorias = st.number_input("Ingresa la energía en Calorías:")
        kilojulios = calorias / 0.239006
        st.write(f"{calorias} calorías son equivalentes a {kilojulios} kilojulios.")
    elif tipo_conversion == "Kilovatios-hora a Megajulios":
        kilovatios_hora = st.number_input("Ingresa la energía en Kilovatios-hora:")
        megajulios = kilovatios_hora * 3.6
        st.write(f"{kilovatios_hora} kilovatios-hora son equivalentes a {megajulios} megajulios.")
    elif tipo_conversion == "Megajulios a Kilovatios-hora":
        megajulios = st.number_input("Ingresa la energía en Megajulios:")
        kilovatios_hora = megajulios / 3.6
        st.write(f"{megajulios} megajulios son equivalentes a {kilovatios_hora} kilovatios-hora.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Presión":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Pascales a Atmósferas",
        "Atmósferas a Pascales",
        "Barras a Libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a Bares"
    ])
    if tipo_conversion == "Pascales a Atmósferas":
        pascales = st.number_input("Ingresa la presión en Pascales:")
        atmosferas = pascales * 0.00000986923
        st.write(f"{pascales} pascales son equivalentes a {atmosferas} atmósferas.")
    elif tipo_conversion == "Atmósferas a Pascales":
        atmosferas = st.number_input("Ingresa la presión en Atmósferas:")
        pascales = atmosferas / 0.00000986923
        st.write(f"{atmosferas} atmósferas son equivalentes a {pascales} pascales.")
    elif tipo_conversion == "Barras a Libras por pulgada cuadrada":
        barras = st.number_input("Ingresa la presión en Barras:")
        psi = barras * 14.5038
        st.write(f"{barras} barras son equivalentes a {psi} libras por pulgada cuadrada.")
    elif tipo_conversion == "Libras por pulgada cuadrada a Bares":
        psi = st.number_input("Ingresa la presión en Libras por pulgada cuadrada:")
        barras = psi / 14.5038
        st.write(f"{psi} libras por pulgada cuadrada son equivalentes a {barras} barras.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión

elif categoria == "Tamaño de Datos":
    tipo_conversion = st.selectbox("Selecciona el tipo de conversión:", [
        "Megabytes a Gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a Megabytes",
        "Terabytes a Petabytes"
    ])
    if tipo_conversion == "Megabytes a Gigabytes":
        megabytes = st.number_input("Ingresa la cantidad en Megabytes:")
        gigabytes = megabytes / 1024
        st.write(f"{megabytes} Megabytes son equivalentes a {gigabytes} Gigabytes.")
    elif tipo_conversion == "Gigabytes a Terabytes":
        gigabytes = st.number_input("Ingresa la cantidad en Gigabytes:")
        terabytes = gigabytes / 1024
        st.write(f"{gigabytes} Gigabytes son equivalentes a {terabytes} Terabytes.")
    elif tipo_conversion == "Kilobytes a Megabytes":
        kilobytes = st.number_input("Ingresa la cantidad en Kilobytes:")
        megabytes = kilobytes / 1024
        st.write(f"{kilobytes} Kilobytes son equivalentes a {megabytes} Megabytes.")
    elif tipo_conversion == "Terabytes a Petabytes":
        terabytes = st.number_input("Ingresa la cantidad en Terabytes:")
        petabytes = terabytes / 1024
        st.write(f"{terabytes} Terabytes son equivalentes a {petabytes} Petabytes.")

# Repetir este bloque de código para cada categoría y tipo de conversión

# Repetir para las otras categorías de conversión


