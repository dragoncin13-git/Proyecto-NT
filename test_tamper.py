from blockchain import Blockchain

def probar_manipulacion():
    print("==================================================")
    print("     PRUEBA DE MANIPULACIÓN Y DETECCIÓN DE FRAUDE  ")
    print("==================================================\n")

    # 1. Crear cadena con 5 bloques
    mi_cadena = Blockchain()
    mi_cadena.add_block(["Alicia envía 50 USD a Carlos"])
    mi_cadena.add_block(["Carlos envía 20 USD a Beatriz"])
    mi_cadena.add_block(["Beatriz envía 10 USD a Daniel"])
    mi_cadena.add_block(["Daniel envía 5 USD a Esteban"])

    # 2. Verificar estado inicial
    estado_inicial = mi_cadena.is_chain_valid()
    print(f"[ESTADO INICIAL] ¿Cadena íntegra y válida?: {estado_inicial}")

    # 3. Alterar intencionalmente un bloque intermedio (Bloque #2)
    print("\n>>> ATANQUE: Modificando la transacción del Bloque #2 de '20 USD' a '2000 USD'...\n")
    mi_cadena.chain[2].transactions = ["Carlos envía 2000 USD a Beatriz"]

    # 4. Verificar estado posterior al ataque
    estado_posterior = mi_cadena.is_chain_valid()
    print(f"[ESTADO TRAS ALTERACIÓN] ¿Cadena íntegra y válida?: {estado_posterior}")

if __name__ == "__main__":
    probar_manipulacion()