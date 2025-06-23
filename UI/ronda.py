from UI.logica import convertirArriesgo
from utils import cambiar_color
from UI.alertas import recuadro

def ronda(palabra_adivinar: str, dificultad: int, jugador: dict, letras_adivinadas: list, arriesgos: list, shows: list) -> str:
    if len(arriesgos) != 0:
        arriesgo = arriesgos[-1]
        for i in range(len(arriesgo)):
            if arriesgo[i] == palabra_adivinar[i]:
                letras_adivinadas[i] = cambiar_color(palabra_adivinar[i].upper(), "Verde")
        show = convertirArriesgo(palabra_adivinar, arriesgo, letras_adivinadas)
        shows.append(show)
    
    nombre_usuario = jugador.get("usuario", "JUGADOR").upper()
    palabra_mostrar = ' '.join(letras_adivinadas)
    arriesgos_restantes = 5 - len(arriesgos)
    
    # Crear lista de arriesgos para mostrar
    arriesgos_display = []
    for i in range(5):
        if i < len(shows):
            arriesgos_display.append(shows[i])
        else:
            arriesgos_display.append("_ " * dificultad)
    recuadro(
        f"ES EL TURNO DE {nombre_usuario}",
        "<linea>",  # Separador visual
        "PALABRA A ADIVINAR:",
        palabra_mostrar,
        "<linea>",  # Separador visual
        "ARRIESGOS:",
        *arriesgos_display,  # Desempaquetar la lista
        f"QUEDAN {arriesgos_restantes} RESTANTES",
        ancho=32,
        alinear="centro"
    )
    arri = input("ARRIESGO: ")
    while len(arri) != dificultad:
        arri = input(f"EL ARRIESGO DEBE TENER {dificultad} CARACTERES: ")

    return (arri.upper(), letras_adivinadas)