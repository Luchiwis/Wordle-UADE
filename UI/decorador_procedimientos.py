def procedimiento(func) -> callable:
    """
    es un decorador de funciones que impide que las funciones de UI que no piden datos al usuario desaparezcan antes de que el usuario presione enter
    """
    
    def wrapper():
        func()
        input("")
        
    return wrapper