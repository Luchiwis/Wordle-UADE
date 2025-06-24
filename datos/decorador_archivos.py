from utils import cambiar_color


def apertura(func) -> callable:
    """
    es un decorador para manejo de errores en la apertura de archivos
    """
    
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            print(cambiar_color(f"Ocurrió un error en la lectura del archivo: \"{e.filename}\"", "rojo"))
            return None
        
        
        
    return wrapper



if __name__ == "__main__":
    @apertura
    def abrir():
        with open("jajs","r") as f:
            pass

    abrir()