"""
Funciones relacionadas con la interaccion del usuario
"""
from UI.login import menu_login
from UI.ranking import ranking
from UI.alertas import recuadro
from UI.dificultad import seleccionar_dificultad

def opciones_menu(usuarios:list[dict], dificultad:int) -> dict:
    usuarios = [u["usuario"] for u in usuarios]
    usuarios = " y ".join(usuarios)

    if len(usuarios) != 0:
        recuadro(
        "MENÚ PRINCIPAL",
        "<linea>",
        "USUARIOS LOGUEADOS:",
        usuarios,
        "<linea>",
        "1. Loguearse",
        "2. Jugar", 
        f"3. Dificultad: {dificultad} letras",
        "4. Estadisticas",
        "5. Cerrar sesión",
        "6. Salir",
        ancho=32,
        alinear="izquierda",
        margen=1
    )
    else:
        recuadro(
        "MENÚ PRINCIPAL",
        "<linea>",
        "NO HAY USUARIOS LOGUEADOS",
        "<linea>",
        "1. Loguearse",
        "2. Jugar", 
        f"3. Dificultad: {dificultad} letras",
        "4. Estadisticas",
        "5. Cerrar sesión",
        "6. Salir",
        ancho=32,
        alinear="izquierda",
        margen=1
    )




def menu(config:dict = { } ) -> dict:
    """
        Funcion de UI que integra las secciones
        - Estadisticas
        - Jugadores (loguear jugadores)
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
    salir = False
    dif = config.get("dificultad", 5)
    usuarios = config.get("jugadores", [])
    while True:
        opciones_menu(usuarios, dif)
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            if len(usuarios) > 0:
                usuarios = []
                recuadro("CERRANDO SESION DE USUARIO(S) Y VOLVIENDO A LOGUEAR", ancho=60)
            usuarios = menu_login()
        elif opcion == "2":
            # SI FALTAN USUARIOS NO ARRANCA LA PARTIDA
            if len(usuarios) == 0:
                recuadro("Error: no hay usuarios para jugar, por favor loguearse", ancho=60)
                continue
            else:
                break
        elif opcion == "3":
            dif = seleccionar_dificultad()
        elif opcion == "4":
            ranking()
        elif opcion == "5":
            usuarios = []
            recuadro("CERRANDO SESION DE USUARIOS", ancho=60)
            
        elif opcion == "6":
            salir = True
            recuadro("CERRANDO PROGRAMA", "GRACIAS POR JUGAR", ancho=60)
            
            break
        else:
            print("\nOpción inválida.")

    datos = {
        "jugadores": usuarios,
        "dificultad": dif,
        "salir": salir
    }
    return datos

    ''' ASI TIENE QUE SALIR
    jugadores = gestion_datos.obtener_usuarios()[:1]
    return {
        "salir": False,
        "dificultad":5,
        "jugadores": jugadores,
    }
    '''