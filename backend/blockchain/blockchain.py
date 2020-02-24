from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.config import MINING_REWARD_INPUT
from backend.wallet.wallet import Wallet

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
        Blockchain.is_valid_transaction_chain(chain)

    @staticmethod
    def is_valid_transaction_chain(chain):
        transaction_ids = set()
        for i in range(len(chain)):
            block = chain[i]
            has_mining_reward = False
            for transation_json in block.data:
                transaction = Transaction.from_json(transation_json)
                if transaction.id in transaction_ids:
                    raise Exception(f'Transaction {transaction.id} is not unique!')
                transaction_ids.add(transaction.id)
                if transaction.input == MINING_REWARD_INPUT:
                    if has_mining_reward:
                        raise Exception(f'There can only be one mining reward per block. Check block with this hash: {block.hash}')
                    has_mining_reward = True
                else:

                    historic_blockchain = Blockchain()
                    historic_blockchain.chain = chain[0:i]
                    historic_balance = Wallet.calculate_balance(historic_blockchain, transaction.input['address'])
                    if historic_balance != transaction.input['amount']:
                        raise Exception(f'Transaction {transaction.id} has an invalid input amount!')
                    Transaction.is_valid_transaction(transaction)

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()