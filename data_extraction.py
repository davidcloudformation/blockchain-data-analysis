from web3 import Web3
import json

# Connect to Ethereum node via Infura
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if web3.isConnected():
    print('Connected to Ethereum network')
else:
    print('Failed to connect to Ethereum network')

# Example function to get the latest block number
def get_latest_block():
    return web3.eth.blockNumber

# Example function to get transaction details by hash
def get_transaction(tx_hash):
    return web3.eth.getTransaction(tx_hash)

# Save the latest block number to a file
latest_block = get_latest_block()
with open('latest_block.json', 'w') as f:
    json.dump({'latest_block': latest_block}, f)

print('Data extraction complete')