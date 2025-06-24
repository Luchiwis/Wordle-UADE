from UI.alertas import recuadro
from UI.decorador_procedimientos import procedimiento

@procedimiento
def partida_finalizada(datos_partida: dict) -> None:
    """
    Es una funcion de UI que informa al usuario que la partida ha sido finalizada y muestra los datos de la misma
    """
    
    tiempo_min, tiempo_seg = datos_partida['tiempo_total']
    ganador = datos_partida['ganador']
    
    # Tarjeta 1: Encabezado
    recuadro("PARTIDA FINALIZADA", ancho=60)
    
    # Tarjeta 2: Información básica
    recuadro(
        "INFORMACIÓN GENERAL",
        f"tiempo:{tiempo_min}min {tiempo_seg}seg",
        f"palabra: {datos_partida['palabra']}",
        ancho=60
    )
    
    # Tarjeta 3: Ganador
    if ganador:
        recuadro(
            " GANADOR",
            f" {ganador['usuario'].upper()}",
            f" {ganador['intentos']} intentos",
            ancho=60
        )
        
        # Tarjeta 4: Todos los jugadores
        jugadores_lineas = [f" JUGADORES ({len(datos_partida['jugadores'])})"]
        for i, jugador in enumerate(datos_partida['jugadores'], 1):
            jugadores_lineas.append(f"{i}. {jugador['usuario']} ({jugador['intentos']} intentos)")
        
        recuadro(*jugadores_lineas, ancho=60, alinear="izquierda", margen=1)
    else:
        recuadro("SIN GANADOR", ancho=60)
    
    # Tarjeta 5: Intentos (si existen)
    if datos_partida['arriesgos']:
        intentos_lineas = [f"INTENTOS ({len(datos_partida['arriesgos'])})"]
        for i, intento in enumerate(datos_partida['arriesgos'], 1):
            intentos_lineas.append(f"{i}. {intento}")
        
        recuadro(*intentos_lineas, ancho=60, alinear="izquierda", margen=1)