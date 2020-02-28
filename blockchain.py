class blockchain:
    def __init__(self):
        self.chain =[]
        self.current_transaction = []
    def new_transaction(self,sender,recipient,ammount):
        pass
    def new_block(self , proof , previous_block = None):
        pass
    @property
    def last_block(self):
        return self.chain[-1]
    @staticmethod
    def hash(block):
        pass
    @staticmethod
    def verify_block(block):
        pass
    
