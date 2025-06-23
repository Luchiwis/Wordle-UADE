from UI.alertas import recuadro
def seleccionar_dificultad() -> int:
    recuadro("seleccionar dificultad",
             "<linea>",
             "1. Facil (5 letras)",
             "2. Normal (6 letras)",
             "3. Dificil (7 letras)"
             , ancho=32, alinear="centro")
    selec = input("Seleccione una dificultad (1-3):")
    while selec not in ["1", "2", "3"]:
        selec = input("Seleccione una dificultad (1-3):")

    return int(selec)+4