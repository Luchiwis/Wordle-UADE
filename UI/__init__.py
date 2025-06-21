"""
Funciones relacionadas con la interaccion del usuario
"""

from UI.decorador_procedimientos import procedimiento
import utils
import gestion_datos
import logica

def menu(configuracion_previa: dict = {}) -> dict:
    """
    Funcion de UI que integra las secciones
    - Estadisticas
    - Jugadores
    - Dificultad
    - Jugar
    - Salir

    Cuando el usuario elige la opcion jugar la funcion termina de ejecutarse y devuelve un diccionario con el siguiente formato:
    {
        "salir": False,
        "dificultad":5,
        "jugadores": [{info jugador del JSON}, ...],
    }
    """
    
    #prueba para que no falle el resto del programa
    jugadores = gestion_datos.obtener_usuarios()[:1]
    return {
        "salir": False,
        "dificultad":5,
        "jugadores": jugadores,
    }


def repetir_partida() -> bool:
    """
    Funcion de UI que pregunta al usuario si desea repetir la partida con los mismos jugadores (revancha) o si desea salir para cambiar las configuraciones
    devuelve True si desea continuar, False si desea volver al menu principal
    
    TODO
    """


def ronda(palabra_adivinar:str, dificultad:int, jugador:dict, adivinado:list, arriesgos:list) -> str:
    """
    Muestra la interfaz de la ronda y devuelve el intento del usuario

    TODO: hacer que se vea mejor
    TODO: hacer las validaciones correspondientes (que la cantidad de letras sea igual a la dificultad y normalizar los caracteres con tildes)
    """
    logica.mostrar_letras_adivinadas(palabra_adivinar, adivinado)
    logica.mostrar_arriesgos(arriesgos, dificultad)
    print(f"turno de:{jugador.get("usuario")}")
    return input("")


@procedimiento
def partida_finalizada(datos_partida: dict) -> None:
    """
    Es una funcion de UI que informa al usuario que la partida ha sido finalizada y muestra los datos de la misma
    """

    print(datos_partida)
