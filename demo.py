from blockchain import Blockchain

def ejecutar_demostracion():
    print("==================================================")
    print("      INICIALIZANDO BLOCKCHAIN Y BLOQUE GÉNESIS    ")
    print("==================================================\n")
    
    mi_cadena = Blockchain()

    print("Agregando bloques a la cadena...\n")
    mi_cadena.add_block(transactions=["Transacción 1: Alice paga 10 Monedas a Bob"])
    mi_cadena.add_block(transactions=["Transacción 2: Bob paga 5 Monedas a Charlie"])
    mi_cadena.add_block(transactions=["Transacción 3: Charlie paga 2 Monedas a Dave"])
    mi_cadena.add_block(transactions=["Transacción 4: Dave paga 0.5 Monedas a Eve"])

    print("==================================================")
    print("          ESTADO ACTUAL DE LA BLOCKCHAIN          ")
    print("==================================================\n")

    for bloque in mi_cadena.chain:
        print(f"--- Bloque #{bloque.index} ---")
        print(f"Timestamp    : {bloque.timestamp}")
        print(f"Transacciones: {bloque.transactions}")
        print(f"Previous Hash: {bloque.previous_hash}")
        print(f"Hash Actual  : {bloque.hash}\n")

    print(f"¿La cadena es válida de principio a fin?: {mi_cadena.is_chain_valid()}")

if __name__ == "__main__":
    ejecutar_demostracion()