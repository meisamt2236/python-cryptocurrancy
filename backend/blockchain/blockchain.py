from backend.blockchain.block import Block

class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        if len(chain) <= len(self.chain):
            raise Exception('Can not replace due to the shorter chain than local.')
        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Can not replace due to invalid chain: {e}')
        self.chain = chain

    def to_json(self):
        # serialize the blockchain into a list of blocks
        serialized_chain = []
        for block in self.chain:
            serialized_chain.append(block.to_json())
        return serialized_chain
    
    def from_json(chain_json):
        # deserialize a list of serialized blocks into a blockchain instance
        blockchain = Blockchain()
        blockchain.chain = list(map(lambda block_json: Block.from_json(block_json), chain_json))
        return blockchain

    @staticmethod
    def is_valid_chain(chain):
        if chain[0] != Block.genesis():
            raise Exception('The genesis block is not valid!')
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()