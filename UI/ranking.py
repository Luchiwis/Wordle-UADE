from datos import obtener_usuarios
from UI.alertas import recuadro
from UI.decorador_procedimientos import procedimiento

import functools


def estadisticas():
    recuadro("Menú de estadísticas",
             "<linea>",
             "1. Ranking total de jugadores",
             "2. Promedio de puntaje global",
             "3. Volver",
             ancho=60)

    opcion = input("Seleccione una opción (1-2): ").strip()

    if opcion == "1":
        ranking()
    elif opcion == "2":
        promedio_puntaje_global()
    elif opcion == "3":
        return
    else:
        recuadro("Opción inválida. Por favor, ingrese 1, 2 o 3.", ancho=60)


@procedimiento
def ranking():
    try:
        usuarios = obtener_usuarios()

        if not usuarios:
            recuadro("No hay usuarios registrados.", ancho=60)
            return

        usuarios_ordenados = sorted(usuarios, key=lambda x: x['puntaje'], reverse=True)

        lineas = []
        lineas.append("RANKING DE JUGADORES")
        lineas.append("<linea>")
        lineas.append(f"{'Pos':<4} {'Usuario':<15} {'Puntaje':<10} {'Partidas':<10} {'1° Turnos':<10}")
        lineas.append("<linea>")

        for i, usuario in enumerate(usuarios_ordenados, 1):
            linea = f"{i}°   {usuario['usuario']:<15} {usuario['puntaje']:<10} {usuario['total_partidas']:<10} {usuario['total_primeros_turnos']:<10}"
            lineas.append(linea)

        lineas.append("<linea>")
        lineas.append(f"Total de jugadores: {len(usuarios_ordenados)}")

        recuadro(*lineas, ancho=60, margen=1, alinear="izquierda")

    except Exception as e:
        recuadro(f"Error al mostrar el ranking: {e}", ancho=60)

@procedimiento
def promedio_puntaje_global():
    try:
        usuarios = obtener_usuarios()

        if not usuarios:
            recuadro("No hay usuarios registrados.", ancho=60)
            return

        # Usamos itertools.reduce para sumar puntajes
        total_puntaje = functools.reduce(lambda acc, u: acc + u['puntaje'], usuarios, 0)
        promedio = total_puntaje / len(usuarios)

        recuadro("Promedio de puntaje global",
                 "<linea>",
                 f"Puntaje total: {total_puntaje}",
                 f"Cantidad de jugadores: {len(usuarios)}",
                 f"Promedio de puntaje: {promedio:.2f}",
                 ancho=60)

    except Exception as e:
        recuadro(f"Error al calcular promedio: {e}", ancho=60)