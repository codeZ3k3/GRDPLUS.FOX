from typing import List, Tuple
from  Web3 import Web3

# Set the provider for the Web3 instance
w3 = Web3 (Web3.HTTPProvider("https://mainnet.infura.io/v3/7cc8664020424148902c9e4e9384599f"))

# Contract ABI (generated using the Solidity compiler)
idea_market_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor",
	},
	{
		"anonymous": False,
		"inputs": [
			{"indexed": False, "name": "id", "type": "uint256"},
			{"indexed": False, "name": "name", "type": "string"},
			{"indexed": False, "name": "description", "type": "string"},
			{"indexed": False, "name": "price", "type": "uint256"},
			{"indexed": False, "name": "owner", "type": "address"},
		],
		"name": "IdeaAdded",
		"type": "event",
	},
	{
		"anonymous": False,
		"inputs": [
			{"indexed": False, "name": "id", "type": "uint256"},
			{"indexed": False, "name": "buyer", "type": "address"},
		],
		"name": "IdeaPurchased",
		"type": "event",
	},
	{
		"inputs": [
			{"name": "name", "type": "string"},
			{"name": "description", "type": "string"},
			{"name": "price", "type": "uint256"},
		],
		"name": "addIdea",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function",
	},
	{
		"inputs": [{"name": "id", "type": "uint256"}],
		"name": "purchaseIdea",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function",
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [{"name": "", "type": "address"}],
		"stateMutability": "view",
		"type": "function",
	},
	{
		"inputs": [{"name": "", "type": "uint256"}],
		"name": "ideas",
		"outputs": [
			{"name": "name", "type": "string"},
			{"name": "description", "type": "string"},
			{"name": "price", "type": "uint256"},
			{"name": "owner", "type": "address"},
			{"name": "timestamp", "type": "uint256"},
		],
		"stateMutability": "view",
		"type": "function",
	},
]

# Contract address
idea_market_address = "0x1234567890abcdef"

# Contract instance
idea_market = w3.eth.contract(
	address=idea_market_address, abi=idea_market_abi

)