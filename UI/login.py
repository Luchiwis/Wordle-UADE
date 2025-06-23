import autenticacion
from UI.alertas import recuadro

def menu_login():
    usuario = autenticacion.login()
    if usuario == None:
        recuadro("ERROR AL LOGUEAR AL USUARIO, VOLVIENDO AL MENU PRINCIPAL", ancho=50)
        return []
    print ("Usuario 1 logueado con exito")
    opcion = input("Desea loguear un segundo usuario (S/N):")
    opcion = opcion.upper()
    while opcion != "N" and opcion != "S":
        opcion = input("Desea loguear un segundo usuario (S/N):")
        opcion = opcion.upper()
    if opcion == "S":
        usuario2 = autenticacion.login()
        if usuario2 == None:
            recuadro("ERROR AL LOGUEAR AL SEGUNDO USUARIO, VOLVIENDO AL MENU PRINCIPAL", ancho=50)
            
            return []
        return [usuario, usuario2]
    return [usuario]