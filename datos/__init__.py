import json
import os
from datos.decorador_archivos import apertura
from juego.calculo_puntos import calcular_puntos_ganados

PATH_USUARIOS = os.path.join(os.path.dirname(__file__), "Usuarios.json")
PATH_PALABRAS = os.path.join(os.path.dirname(__file__), "palabras")
PATH_CONFIGURACION = os.path.join(os.path.dirname(__file__), "config.json")

@apertura
def registrar_datos_partida(datos_partida: dict) -> None:
    """
    Registra los datos de una partida en el archivo de usarios.json
   """
    usuarios = obtener_usuarios()  # usuarios del json

    for jugador in datos_partida["jugadores"]:  # se repite maximo 2 veces
        if  datos_partida["ganador"] != None and jugador["id"] == datos_partida["ganador"]["id"]:
            jugador["puntaje"] += calcular_puntos_ganados(jugador["intentos"], datos_partida["dificultad"])
        else:
            jugador["puntaje"] -= 0

        for usuario in usuarios:
            if usuario["id"] == jugador["id"]:
                usuario["total_partidas"] = jugador["total_partidas"]
                usuario["puntaje"] = jugador["puntaje"]
                usuario["total_primeros_turnos"] = jugador["total_primeros_turnos"]
                usuario["palabras_usadas"].append(datos_partida["palabra"])
                # palabras usadas es una lista
                # palabra es un str

        with open(PATH_USUARIOS, "w") as f:
            json.dump(usuarios, f, indent=2)

@apertura
def guardar_nuevo_usuario(datos_usuario: dict) -> None:
    with open(PATH_USUARIOS, "r") as f:
        usuarios = json.load(f)

    usuarios.append(datos_usuario)
    with open(PATH_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=2)

@apertura
def obtener_usuarios():
    with open(PATH_USUARIOS, "r") as f:
        usuarios = json.load(f)

    return usuarios

@apertura
def guardar_usuarios(usuarios):
    with open(PATH_USUARIOS, 'w') as archivo:
        json.dump(usuarios, archivo, indent=2)

@apertura
def obtener_palabras(longitud: int) -> list[str]:
    assert longitud in range(5, 8)
    with open(os.path.join(PATH_PALABRAS, f"{longitud}.txt")) as f:
        palabras = f.readlines()

    palabras = list(map(lambda x: x.replace("\n", ""), palabras))

    return palabras

@apertura
def guardar_configuracion(config: dict) -> None:
    with open(PATH_CONFIGURACION, "w") as f:
        json.dump(config, f, indent=2)

@apertura
def cargar_configuracion() -> dict:
    with open(PATH_CONFIGURACION, "r") as f:
        config = json.load(f)

    return config

# TESTEO
if __name__ == "__main__":
    print(cargar_configuracion())
