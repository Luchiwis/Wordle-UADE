
# 🧠 Juego de Palabras por Consola

Este proyecto es un **juego de adivinanza de palabras** tipo Wordle desarrollado en Python. Permite iniciar sesión, jugar rondas con palabras de distintas dificultades, registrar partidas, mostrar rankings y testear funciones del sistema.

---

## 📦 Estructura del Proyecto

```
.
├── main.py                  # Archivo principal para iniciar el juego
├── pruebas.py              # Script auxiliar para pruebas manuales
├── readme.md               # Este archivo
├── .gitignore              # Archivos/carpetas ignorados por git

├── autenticacion/          # Lógica de inicio de sesión y control de usuarios
│   └── __init__.py

├── datos/                  # Configuración, usuarios y diccionarios de palabras
│   ├── config.json
│   ├── Usuarios.json
│   └── palabras/
│       ├── 5.txt
│       ├── 6.txt
│       └── 7.txt

├── juego/                  # Lógica principal del juego
│   ├── logica.py
│   └── __init__.py

├── UI/                     # Módulos relacionados con la interfaz por consola
│   ├── alertas.py
│   ├── alinear.py
│   ├── decorador_procedimientos.py
│   ├── dificultad.py
│   ├── logica.py
│   ├── login.py
│   ├── partida_finalizada.py
│   ├── ranking.py
│   ├── repetir_partida.py
│   └── ronda.py

├── utils/                  # Funciones utilitarias generales
│   └── __init__.py

└── testing/                # Tests automatizados
    ├── test_alinear.py
    ├── test_logica_juego.py
    └── test_logica_ui.py
```

---

## ▶️ Cómo Ejecutar

1. Asegurate de tener **Python 3.11+** instalado.
2. Cloná el repositorio o descargá los archivos.
3. Ejecutá el juego desde `main.py`:

```bash
python main.py
```

---

## 🧰 Funcionalidades

- Inicio de sesión y gestión de usuarios
- Juego de adivinanza por rondas
- Selección de dificultad (5, 6 o 7 letras)
- Ranking de jugadores por puntaje
- Estadisticas globales
- Decoradores y helpers para mostrar información y evitar errores
- Consola enriquecida con recuadros de texto

---

## 🎮 Ejemplo Visual

### Menú Principal

```
╔══════════════════════════════╗ 
║ MENÚ PRINCIPAL               ║
╠══════════════════════════════╣
║ USUARIOS LOGUEADOS:          ║
║ lucho                        ║
╠══════════════════════════════╣
║ 1. Loguearse                 ║
║ 2. Jugar                     ║
║ 3. Dificultad: 6 letras      ║
║ 4. Estadísticas              ║
║ 5. Cerrar sesión             ║
║ 6. Salir                     ║
╚══════════════════════════════╝
```

### Partida en Curso

```
╔══════════════════════════════╗
║     ES EL TURNO DE TOTI      ║
╠══════════════════════════════╣
║     PALABRA A ADIVINAR:      ║
║          _ _ _ _ _           ║
╠══════════════════════════════╣
║          ARRIESGOS:          ║
║          _ _ _ _ _           ║
║          _ _ _ _ _           ║
║          _ _ _ _ _           ║
║          _ _ _ _ _           ║
║          _ _ _ _ _           ║
║      QUEDAN 5 RESTANTES      ║
╚══════════════════════════════╝
```

---

## ⚙️ Características

- Guarda la información de los usuarios logueados.
- Los datos de los jugadores (puntaje, partidas, etc.) persisten entre partidas.
- Al loguearse un nuevo usuario, se desloguean automáticamente los anteriores.
- Las contraseñas no están hasheadas.
- Dificultades disponibles: **5, 6 o 7 letras**.
- Estilo visual con recuadros enriquecidos en consola.
- Basado en la mecánica del juego **Wordle**.

---

## 📌 Notas

Este software fue diseñado como un proyecto educativo, por lo tanto:

- No implementa cifrado o protección de contraseñas.
- Está pensado para ejecutarse en consola.
- Es ideal para prácticas de lógica, manipulación de archivos JSON y trabajo modular en Python.
