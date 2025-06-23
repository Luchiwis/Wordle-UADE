import datos
from UI.alertas import recuadro
from UI.decorador_procedimientos import procedimiento

@procedimiento
def ranking():
    try:
        usuarios = datos.obtener_usuarios()

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