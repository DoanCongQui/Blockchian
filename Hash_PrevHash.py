import hashlib

class Block:
    def __init__(self, data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""
        

def hash(block):
    data = block.data + block.prev_hash 
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

        self.chain.append(block)

    def print(self):
        for block in self.chain :
            print("")
            print("Data:", block.data)
            print("Prev_hash:", block.prev_hash)
            print("Hash:", block.hash)
            print("")
    
    def is_valid(self):
        for i in range(1, len(self.chain)):
            currrent_block = self.chain[i]
            prev_block = self.chain[i-1]

            if hash(currrent_block) != currrent_block.hash:
                return False
            
            # if prev_block.hash != currrent_block.prev_hash:
            #     return False
        return True
    
blockchain = Blockchain()
blockchain.add_block("DoanCongQui")
blockchain.add_block("NguyenVanA")
blockchain.add_block("NguyenVanB")
blockchain.add_block("NguyenVanC")

# blockchain.chain[1].data = "Qui"
# blockchain.chain[1].hash = hash(blockchain.chain[1])

print("Is valid?:", blockchain.is_valid())


blockchain.print()

