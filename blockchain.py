import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Es crucial ordenar las llaves para garantizar el mismo hash en cada llamada
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_content).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # El primer bloque no tiene previous_hash real, se usa '0' por convención
        genesis_block = Block(index=0, transactions="Bloque Genesis", previous_hash="0")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            transactions=transactions,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # 1. Verificar si el contenido del bloque fue alterado
            if current_block.hash != current_block.calculate_hash():
                print(f"Error: El hash del bloque {current_block.index} ha sido alterado.")
                return False

            # 2. Verificar si la referencia al bloque anterior es válida
            if current_block.previous_hash != previous_block.hash:
                print(f"Error: El previous_hash del bloque {current_block.index} no coincide con el hash del bloque {previous_block.index}.")
                return False

        return True