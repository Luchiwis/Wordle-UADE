import utils
import solitario
import multijugador
import login

def main():
    # preguntar cantidad de jugadores
    
    # autenticar usuario
    

    while cantidad_jugadores.isalpha() or not int(cantidad_jugadores) in (1, 2):
        print("Opción no valida")
        cantidad_jugadores = pedir_cantidad_jugadores()

    veces_jugadas = 0

 
    #Lo que necesitamos hacer es que se modifiquen los puntos

    jugador_1 = {
            "color": "Azul",
            "nombre": "",
            "gano": False,
            "puntos": 0,
            "empezo_ultima_partida": False
        }

    if int(cantidad_jugadores) == 2:
        jugador_2 = {
            "color": "Rojo",
            "nombre": "",
            "gano": False,
            "puntos": 0,
            "empezo_ultima_partida": False
        }

        jugador_1["nombre"] = input("Ingrese el nombre del jugador 1: ")
        jugador_2["nombre"] = input("Ingrese el nombre del jugador 2: ")

        jugadores = (jugador_1, jugador_2)

        multijugador.comenzar_juego(jugadores, veces_jugadas)
    else:
        solitario.comenzar_juego(jugador_1, veces_jugadas)

def pedir_cantidad_jugadores():
    print("Seleccione la cantidad de jugadores")
    print("Presiona 1 para jugar solo")
    print("Persiona 2 para jugar con un amigo")
    return input()
def menu_principal():
    while True:
        print("\n════════════════ MENÚ PRINCIPAL ════════════════ ")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        opcion = input("Selecciona una opción (1 o 2): ")
        if opcion == "1":

            #Ingresa pass y verifica
            #Si los 2 estan bien


            login.registrar_usuario()
            break
        elif opcion == "2":
            login.login()
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")


main()