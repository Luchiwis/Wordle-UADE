from juego import partida
import UI
from UI.partida_finalizada import partida_finalizada
from UI.repetir_partida import repetir_partida
import datos


def main():

    configuracion = datos.cargar_configuracion()

    while True:
        configuracion = UI.menu(configuracion)

        jugadores = configuracion.get("jugadores")
        dificultad = configuracion.get("dificultad")
        salir = configuracion.get("salir")
        if salir:
            break

        # jugar partida
        continuar_partida = True
        while continuar_partida:
            datos_partida = partida(jugadores, dificultad)

            partida_finalizada(datos_partida) #funcion UI
            datos.registrar_datos_partida(datos_partida)  # funcion de mati

            continuar_partida = repetir_partida() #funcion UI
            jugadores = datos_partida["jugadores"]  # para que se apliquen palabras_usadas y total_primeros_turnos, indispensables

    datos.guardar_configuracion(configuracion)

if __name__ == "__main__":
    main()
