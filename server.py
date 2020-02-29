from blockchain import Blockchain
from flask import Flask, jsonify,request
from uuid import uuid4
import requests

app = Flask(__name__)
netcoin = Blockchain()

node_identifier = str(uuid4()).replace('-','')

@app.route('/chain', methods = ['GET',])
def full_chain():
    response = {
        'chain': netcoin.chain,
        'length': len(netcoin.chain),

    }

    return jsonify(response)

@app.route('/mine',methods=['get'])
def mine():
   last_block = netcoin.last_block
   last_proof = last_block['proof']
   proof = netcoin.proof_of_work(last_proof)

   netcoin.new_transaction(sender ='0', recipient = node_identifier, ammount=12.5)
   previous_hash = netcoin.hash(last_block)
   block = netcoin.new_block(proof, previous_hash)
   response ={
       'message' : 'new bolck added',
       'index'  : block['index'],
       'transaction' : block['transaction'],
       'proof' :block['proof'],
       'previous_hash' : block['previous_block']
     }
   return jsonify(response)

@app.route('/transaction/new', methods =['POST',])
def new_transaction():
    values = request.get_json()

    index =netcoin.new_transaction(values['sender'], values['recipient'], values['ammount'])
    response ={
        'message' : f'transaction will be added to block{index}'
    } 
    return jsonify(response)

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=8000)
