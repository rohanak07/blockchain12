
from blockchain import Blockchain
netcoin = Blockchain()
print(netcoin.chain)
netcoin.new_transaction('rohan','ash',12.5)
print(netcoin.current_transaction)
print(netcoin.proof_of_work(7555))
