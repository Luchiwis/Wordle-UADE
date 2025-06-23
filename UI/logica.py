from utils import cambiar_color

def convertirArriesgo(palabra_adivinar, arriesgo, adivinado: list):
    # Analiza el arriesgo para devolver el color en el que va a ir cada letra
    palabra_adivinar_arr = [*palabra_adivinar]
    arriesgo_arr = [*arriesgo]
    letras_sin_adivinar = []
    letras_sin_procesar = []
    resultado = {
        "Verde": [],
        "Amarillo": [],
        "GrisOscuro": [],
    }

    for index in range(len(arriesgo_arr)):
        if palabra_adivinar_arr[index] == arriesgo_arr[index]:
            resultado["Verde"].append(index)
        else:
            letras_sin_adivinar.append(palabra_adivinar_arr[index])
            letras_sin_procesar.append(arriesgo_arr[index])

    if len(letras_sin_procesar) > 0:
        for index in range(len(letras_sin_procesar.copy())):
            if letras_sin_procesar[index] in letras_sin_adivinar:
                resultado["Amarillo"].append(letras_sin_procesar[index])
                letras_sin_adivinar.remove(letras_sin_procesar[index])
            else:
                resultado["GrisOscuro"].append(letras_sin_procesar[index])
    mostrar = ""
    for i in range(len(arriesgo)):
        letra = arriesgo[i]

        if (i in resultado["Verde"]):
            mostrar += cambiar_color(letra.upper(), "Verde")
        elif (letra in resultado["Amarillo"]):
            resultado["Amarillo"].remove(letra)

            mostrar += cambiar_color(letra.upper(), "Amarillo")
        elif (letra in resultado["GrisOscuro"]):
            resultado["GrisOscuro"].remove(letra)

            mostrar += cambiar_color(letra.upper(), "GrisOscuro")

    return mostrar
