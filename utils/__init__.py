def obtener_color(color) -> str:
    """
    devuelve el codigo del color indicado
    """
    colores = {
        "verde": "\x1b[32m",
        "amarillo": "\x1b[33m",
        "grisOscuro": "\x1b[90m",
        "defecto": "\x1b[39m",
        "rojo": "\033[91m",
        "azul": "\33[34m"
    }
    return colores.get(color.lower(), "\x1b[39m") #si no encuentra el color devuelve "\x1b[39m" para evitar errores

def cambiar_color(texto, color):
    return (obtener_color(color) + texto + obtener_color("Defecto")) if texto != "" else ""