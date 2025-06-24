# 🧠 UADLE

Este proyecto es un **juego de adivinanza de palabras** tipo Wordle desarrollado en Python. Permite iniciar sesión, jugar rondas con palabras de distintas dificultades, registrar partidas, mostrar rankings, estadisticas y testear funciones del sistema.

---

## 👥 Integrantes
- Lucio Petrucci
- Octavio Poggi
- Matias Marrassini
- Juan Cruz Bogarín

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
╔══════════════════════════════════════════════════════════╗
║ MENÚ PRINCIPAL                                           ║
╠══════════════════════════════════════════════════════════╣
║ USUARIOS LOGUEADOS:                                      ║
║ mati y toti                                              ║
╠══════════════════════════════════════════════════════════╣
║ 1. Loguearse                                             ║
║ 2. Jugar                                                 ║
║ 3. Dificultad: 5 letras                                  ║
║ 4. Estadisticas                                          ║
║ 5. Cerrar sesión                                         ║
║ 6. Salir                                                 ║
╚══════════════════════════════════════════════════════════╝
```

### Partida en Curso

```
╔══════════════════════════════════════════════════════════╗
║                   ES EL TURNO DE TOTI                    ║
╠══════════════════════════════════════════════════════════╣
║                   PALABRA A ADIVINAR:                    ║
║                        _ _ _ _ _                         ║
╠══════════════════════════════════════════════════════════╣
║                        ARRIESGOS:                        ║
║                        _ _ _ _ _                         ║
║                        _ _ _ _ _                         ║
║                        _ _ _ _ _                         ║
║                        _ _ _ _ _                         ║
║                        _ _ _ _ _                         ║
║                    QUEDAN 5 RESTANTES                    ║
╚══════════════════════════════════════════════════════════╝
```

### Ranking

```
╔══════════════════════════════════════════════════════════╗
║ RANKING DE JUGADORES                                     ║
╠══════════════════════════════════════════════════════════╣
║ Pos  Usuario         Puntaje    Partidas   1° Turnos     ║
╠══════════════════════════════════════════════════════════╣
║ 1°   matias          580        18         1             ║
║ 2°   mati            200        6          3             ║
║ 3°   lucho           160        9          4             ║
║ 4°   juan            120        0          0             ║
║ 5°   toti            120        6          3             ║
║ 6°   juanc           30         4          1             ║
║ 7°   juancho         0          0          0             ║
║ 8°   jorge           0          0          0             ║
╠══════════════════════════════════════════════════════════╣
║ Total de jugadores: 8                                    ║
╚══════════════════════════════════════════════════════════╝
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

---

## ⚙️ Requisitos solicitados por el docente
- [x]  Expresiones regulares
- [x]  Funcion map
- [x]  Funcion reduce del modulo functools
- [ ]  Funcion filter
- [x]  Manejo de errores 
- [x]  Testing
- [x]  "Rebanadas" (cortes de lista)
- [x]  Listas por comprensión
- [x]  Manejo de archivos

---

## 📂 Estructura del Proyecto

```
├── main.py                 # Archivo principal para iniciar el juego
├── datos/                  # Configuración, usuarios y diccionarios de palabras
├── juego/                  # Lógica principal del juego
├── UI/                     # Módulos relacionados con la interfaz por consola
├── utils/                  # Funciones utilitarias generales
└── testing/                # Tests automatizados
```
