
"""
Desde esta sección se maneja todas las funciones relacionadas con el registro de usuarios.
"""

import re
from datos import obtener_usuarios as cargar_usuarios
from datos import guardar_usuarios
from UI.alertas import recuadro

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario['usuario'] == nombre:
            return usuario
    return None

def validar_contrasena(contrasena):
    # Longitud entre 8 y 16
    if not re.fullmatch(r'.{8,16}$', contrasena):
        recuadro("La contraseña debe tener entre 8 y 16 caracteres.", ancho=60)
        
        return False

    # Al menos una mayúscula
    if not re.search(r'[A-Z]+', contrasena):
        recuadro("Debe contener al menos una letra mayúscula.", ancho=60)
        
        return False

    # Al menos una minúscula
    if not re.search(r'[a-z]+', contrasena):
        recuadro("Debe contener al menos una letra minúscula.", ancho=60)
        return False

    # Al menos un número
    if not re.search(r'[0-9]+', contrasena):
        recuadro("Debe contener al menos un número.", ancho=60)
        return False
    print("✅Contraseña Valida✅")
    return True

def validar_usuario(nombre_usuario):
    patron = r'^[a-z]{4,20}$'
    if re.fullmatch(patron, nombre_usuario):
        print("✅Usuario Valido✅")
        return True
    else:
        recuadro("El usuario debe tener solo letras minúsculas y entre 4 y 20 caracteres.", ancho=60)
        return False

# Lógica de login
def login():
    usuarios = cargar_usuarios()

    nombre = input("Nombre de usuario: ")
    while not validar_usuario(nombre):
        nombre = input("Nombre de usuario: ")
    usuario = buscar_usuario(usuarios, nombre)

    if usuario:
        contrasena = input("Usuario encontrado, ingrese contraseña: ")
        it = 3
        while usuario['contrasena'] != contrasena:
            it -= 1
            recuadro(f"Contraseña incorrecta. Quedan {it} intentos", ancho=60)
            
            if it == 0:
                recuadro("Demasiados intentos. El usuario se ha desconectado.", ancho=60)
                
                return None
            contrasena = input("Ingrese Contraseña: ")
        print(f"✅ Bienvenido de nuevo, {nombre}. Puntaje actual: {usuario['puntaje']}✅")
    else:
        #ACA APLICAREMOS RECURSIVIDAD DE PREGUNTAR SI QUEREMOS REGISTRARNOS O INICIAR SESION CON OTRO USUARIO LLAMANDO DE NUEVO A LOGIN
        recuadro(f"Usuario no encontrado. Creando nuevo usuario {nombre}", ancho=60)
        recuadro("Ahora debe ingresar su contraseña", ancho=60)
        recuadro("La contraseña deberá tener un minimo de 8 caracteres, al menos una mayúscula, una minúscula y un número", ancho=60)
        

        contrasena = input("Ingrese contraseña: ")
        while not validar_contrasena(contrasena):
            recuadro("La contraseña deberá tener un minimo de 8 caracteres, al menos una mayúscula, una minúscula y un número", ancho=60)
            
            contrasena = input("Ingrese contraseña: ")
        nuevo_usuario = {
            "id" : len(usuarios)+1,
            "usuario": nombre,
            "contrasena": contrasena,
            "puntaje": 0,
            "total_partidas": 0,
            "total_primeros_turnos": 0,
            "palabras_usadas": []
        }
        usuarios.append(nuevo_usuario)
        guardar_usuarios(usuarios)
        recuadro(f"El usuario {nombre} con contraseña {contrasena} fue creado exitosamente.")
        
        usuario = nuevo_usuario

    return usuario  # Retornar el diccionario del usuario logueado