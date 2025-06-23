name="julio"
age = 10

print(f"Name: {"joo":<10} | Age: {age} |")
print(f"Name: {" ":^10} | Age: {age} |")

def validar_arriesgo(arriesgo):
    valido = False
    len_correcto = True
    LEN_CORRECTO = 5

    if len(arriesgo) != LEN_CORRECTO:
        print("El arriesgo debe tener 5 caracteres")
        len_correcto = False

    # Verifica que sean solo letras
    if len_correcto:
        if arriesgo.isalpha():
            valido = True
        else:
            print("El arriesgo debe contener solo letras")

    return valido


def procesar_arriesgo(palabra, arriesgo, adivinado):
    """procesa el arriesgo y lo clasifica por color"""
    resultado = procesar_intento(palabra, arriesgo)
    mostrar = ""

    for i in range(len(arriesgo)):
        letra = arriesgo[i]

        if (i in resultado["Verde"]):
            mostrar += cambiar_color(letra, "Verde")
            if not i in adivinado:
                adivinado.append(i)
        elif (letra in resultado["Amarillo"]):
            resultado["Amarillo"].remove(letra)

            mostrar += cambiar_color(letra, "Amarillo")
        elif (letra in resultado["GrisOscuro"]):
            resultado["GrisOscuro"].remove(letra)

            mostrar += cambiar_color(letra, "GrisOscuro")

    return mostrar


def mostrar_letras_adivinadas(palabra, adivinado):
    LARGO_PALABRA = 5
    print("PALABRA A ADIVINAR: ", end="")
    for i in range(LARGO_PALABRA):
        if i in adivinado:
            print(cambiar_color(palabra[i], "Verde"), end="")
        else:
            print("?", end="")

    print(" ")

def cambiar_color(texto, color):
    return (utils.obtener_color(color) + texto + utils.obtener_color("Defecto")) if texto != "" else ""


def obtener_color(color):
    colores = {
        "Verde": "\x1b[32m",
        "Amarillo": "\x1b[33m",
        "GrisOscuro": "\x1b[90m",
        "Defecto": "\x1b[39m",
        "Rojo": "\033[91m",
        "Azul": "\33[34m"
    }
    return colores[color]