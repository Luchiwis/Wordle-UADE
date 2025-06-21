import utils
from juego import partida
import UI
import gestion_datos

def main():
    salir = False
    
    while not salir:
        
        configuracion = UI.menu()
        
        jugadores = configuracion.get("jugadores")
        dificultad = configuracion.get("dificultad")
        salir = configuracion.get("salir")
    
        # jugar partida
        continuar_partida = True
        while continuar_partida:
            datos_partida = partida(jugadores, dificultad)
            
            UI.partida_finalizada(datos_partida)
            gestion_datos.registrar_datos_partida(datos_partida)
            
            continuar_partida = UI.repetir_partida()
            jugadores = datos_partida["jugadores"]      #para que se apliquen palabras_usadas y total_primeros_turnos, indispensables


if __name__ == "__main__":
    main()