import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain =[]
        self.current_transaction = []
        self.new_block(proof = 100, previous_block =1 )
    def new_transaction(self,sender,recipient,ammount):
        self.current_transaction.append({
            'sender':sender,
            'recipient' : recipient,
            'ammount' : recipient,
           })

        return self.last_block['index'] + 1

    def new_block(self , proof , previous_block = None):
        block = {
            'index': len(self.chain) + 1,
            'timesptamp' : time(),
            'transaction' : self.current_transaction,
            'proof' : proof,
            'previous_block' : previous_block or self.hash(self.last_block),
        }
        self.chain.append(block)
        self.current_transaction = []
      
        return block
    @property
    def last_block(self):
        return self.chain[-1]
    @staticmethod
    def hash(block):
        block_string = json.dumps(block).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @staticmethod
    def verify_block(block):
        pass
    


    
    def proof_of_work(self,last_proof):
        proof = 0
        while self.valid_proof(last_proof,proof) is False :
           proof +=1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = '{}{}'.format(last_proof,proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:5] == "00000" 