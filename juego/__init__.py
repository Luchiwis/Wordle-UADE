import time
import juego.logica as logica
import UI


def partida(jugadores: list[dict], dificultad: int) -> dict:
    """
    Esta funcion se encarga de efectuar una partida, cuando la misma finaliza devuelve los datos de los resultados
    """

    # Variables de la partida
    jugadores = logica.acomodar_jugadores(jugadores)
    palabras_usadas = [palabra_usada for j in jugadores for palabra_usada in j["palabras_usadas"]]
    palabra_adivinar = logica.conseguir_palabra(dificultad, palabras_usadas)
    arriesgos = []  # palabras arriesgadas
    adivinado = []  # letras adivinadas
    tiempo_inicial = time.time()
    partida_terminada = False
    arriesgo = ""
    turno = 0
    ganador = None
    
    # crear key intentos:0 para contabilizar individualmente los arriesgos de cada jugador
    for jugador in jugadores:
        jugador["intentos"] = 0


    # ejecución de la partida
    while not partida_terminada:
        jugador = jugadores[turno]
        arriesgo = UI.ronda(palabra_adivinar, dificultad, jugador, adivinado, arriesgos)
        arriesgos.append(arriesgo)

        # chequear si alguien ganó
        if arriesgo == palabra_adivinar:
            partida_terminada = True
            ganador = jugador
        # chequear si se acabaron los intentos
        elif len(arriesgos) >= 5:
            partida_terminada = True
        else:
            # la partida continua
            jugador["intentos"] += 1
            turno = (turno + 1) % len(jugadores)

    datos_partida = {
        "tiempo_total": logica.calcular_tiempo_total(tiempo_inicial),
        "ganador": ganador,
        "jugadores": jugadores,
        "arriesgos": arriesgos,
        "adivinado": adivinado
    }

    return datos_partida
