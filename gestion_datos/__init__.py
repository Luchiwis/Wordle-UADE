import json
PATH_DATOS = "./datos/"

def registrar_datos_partida():
    pass

def guardar_nuevo_usuario():
    pass

def obtener_usuarios():
    with open(PATH_DATOS + "usuarios.json") as f:
        usuarios = json.load(f)
    
    return usuarios

def obtener_palabras(longitud):
    assert longitud in range(5,7)
    with open(PATH_DATOS + f"palabras/{longitud}.txt") as f:
        palabras = f.readlines()
        
    return palabras


def calcular_puntos_ganados(arriesgos, gano):
    # puntos = {
    #     1: 50,
    #     2: 40,
    #     3: 30,
    #     4: 20,
    #     5: 10,
    # }
    # Esta parte del codigo fue modificada para cumplir con el requisito de implementacion de comprension luego de la primera correción
    puntos = {
        arriesgo: puntos
        for arriesgo, puntos in [[1, 50], [2, 40], [3, 30], [4, 20], [5, 10]]
    }

    return -100 if not gano else puntos[len(arriesgos)]

if __name__ == "__main__":
    print(obtener_palabras(5))
    
    