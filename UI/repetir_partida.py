from UI.alertas import recuadro

def repetir_partida() -> bool:
    recuadro("PARTIDA FINALIZADA","DESEA VOLVER A JUGAR?", ancho=60)

    decision = input("SI (S) o NO (N):")
    while decision not in ["S", "s", "N", "n"]:
        decision = input("SI (S) o NO (N):")
    decision = decision.upper()
    if decision == "S":
        return True
    else:
        return False