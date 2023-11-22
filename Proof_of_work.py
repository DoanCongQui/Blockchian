import hashlib
from datetime import datetime, timedelta

class Block:
    def __init__(self, data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""
        self.nonce = 0
        self.total_time = ""
        

def hash(block):
    data = block.data + block.prev_hash + str(block.nonce)
    data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

        block = Block("Ho_Va_Ten")
        block.hash = hash(block)
        self.chain.append(block)
    
    def add_block(self, data):
        block = Block(data)
        block.prev_hash = self.chain[-1].hash
        block.hash = hash(block)
        start = datetime.now()
        while hash(block).startswith("0000") == False:
            block.nonce = block.nonce + 1
            block.hash = hash(block)
        end = datetime.now()
        block.total_time = str(end-start)

        self.chain.append(block)

    def print(self):
        for block in self.chain :
            print("")
            print("Data:", block.data)
            print("Prev_hash:", block.prev_hash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)
            print("Total time:", block.total_time)
            print("")
    
    def is_valid(self):
        for i in range(1, len(self.chain)):
            currrent_block = self.chain[i]
            prev_block = self.chain[i-1]

            if hash(currrent_block) != currrent_block.hash:
                return False
            
            if prev_block.hash != currrent_block.prev_hash:
                return False
        return True
    
blockchain = Blockchain()
blockchain.add_block("DoanCongQui")
blockchain.add_block("NguyenVanA")
blockchain.add_block("NguyenVanB")
blockchain.add_block("NguyenVanC")

# blockchain.chain[1].data = "Qui"

print("Is valid?:", blockchain.is_valid())

blockchain.print()

