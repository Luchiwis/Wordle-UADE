from UI.alinear import *


def recuadro(*args, **kwargs) -> None:
    """
    Dibuja un recuadro decorativo con caracteres Unicode y muestra texto alineado dentro.

    Esta función toma múltiples cadenas de texto y las posiciona dentro de un cuadro
    con bordes dibujados usando caracteres box-drawing de Unicode. Permite personalizar
    el ancho, márgenes, alineación y si el recuadro debe cerrarse o continuar.

    Args:
        *args (str): Cadenas de texto que se mostrarán dentro del recuadro.
                    Cada argumento será una línea separada dentro del recuadro.
                    <linea> dibuja una linea horizontal

        **kwargs: Argumentos opcionales para personalizar el recuadro:
            ancho (int, optional): Ancho total del recuadro en caracteres.
                                 Defaults to 30.
            margen (int, optional): Espacio adicional entre el borde y el texto
                                  en ambos lados. Defaults to 0.
            alinear (str, optional): Alineación del texto dentro del recuadro.
                                   Opciones: "centro", "izquierda", "derecha".
                                   Defaults to "centro".
            continuo (bool, optional): Si es True, no dibuja la línea inferior
                                     del recuadro, permitiendo continuar el
                                     recuadro en llamadas posteriores.
                                     Defaults to False.

    Returns:
        None: Esta función solo imprime en pantalla y no retorna valores.

    Raises:
        KeyError: Si se proporciona una opción de alineación no válida.

    Examples:
        >>> recuadro("Hola mundo")
        ╔════════════════════════════╗
        ║        Hola mundo          ║
        ╚════════════════════════════╝

        >>> recuadro("Línea 1", "Línea 2", ancho=20, alinear="izquierda")
        ╔══════════════════╗
        ║Línea 1           ║
        ║Línea 2           ║
        ╚══════════════════╝

        >>> recuadro("Con margen", ancho=25, margen=2)
        ╔═══════════════════════╗
        ║  Con margen           ║
        ╚═══════════════════════╝

        >>> # Recuadro continuo (sin cerrar)
        >>> recuadro("Primera parte", continuo=True)
        ╔════════════════════════════╗
        ║      Primera parte         ║

    Note:
        - Esta función depende de las funciones auxiliares 'centrar', 'izquierda'
          y 'derecha' para la alineación del texto.
        - El ancho interno efectivo es ancho - 2 (por los bordes) - (margen * 2).
        - Si el texto es más largo que el ancho disponible, puede causar
          desbordamiento visual.
        - Los caracteres Unicode utilizados son: ╔ ╗ ╚ ╝ ║ ═
    """
    ancho = kwargs.get("ancho", 30)
    margen = kwargs.get("margen", 0)
    alinear = kwargs.get("alinear", "centro")
    continuo = kwargs.get("continuo", False)
    ancho_interno = ancho - 2

    alineados = {"centro": centrar, "izquierda": izquierda, "derecha": derecha}

    print("╔" + "═" * (ancho_interno) + "╗")
    for linea in args:
        if linea == "<linea>":
            print("╠"+ "═" * (ancho_interno) +"╣")
        else:
            
            print(
                f"║{' '*margen}{alineados.get(alinear,"centro")(linea, ancho_interno-(margen*2))}{' '*margen}║"
            )

    if continuo:
        return

    print("╚" + "═" * (ancho - 2) + "╝")


if __name__ == "__main__":
    recuadro("holis", margen=1, alinear="centro", continuo=True)
