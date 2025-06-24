def calcular_puntos_ganados(arriesgos: int, dificultad:int) -> int:
    puntos = [50, 40, 30, 20, 10]

    return puntos[arriesgos] * (dificultad-4)