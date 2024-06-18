import json
from . import Connection as con

abi = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "data",
				"type": "string"
			}
		],
		"name": "DataStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			}
		],
		"name": "retrieveData",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_data",
				"type": "string"
			}
		],
		"name": "storeData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]


bytecode = '6080604052348015600e575f80fd5b5061078c8061001c5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c80632a77d70714610038578063fb218f5f14610068575b5f80fd5b610052600480360381019061004d9190610256565b610084565b60405161005f91906102f1565b60405180910390f35b610082600480360381019061007d919061043d565b610150565b005b60605f808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2080546100cd906104b1565b80601f01602080910402602001604051908101604052809291908181526020018280546100f9906104b1565b80156101445780601f1061011b57610100808354040283529160200191610144565b820191905f5260205f20905b81548152906001019060200180831161012757829003601f168201915b50505050509050919050565b805f803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2090816101999190610687565b503373ffffffffffffffffffffffffffffffffffffffff167f4b33dafb50dac5530c30aca4e4069fd67a18220888b874b8519558d1769d49a1826040516101e091906102f1565b60405180910390a250565b5f604051905090565b5f80fd5b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610225826101fc565b9050919050565b6102358161021b565b811461023f575f80fd5b50565b5f813590506102508161022c565b92915050565b5f6020828403121561026b5761026a6101f4565b5b5f61027884828501610242565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6102c382610281565b6102cd818561028b565b93506102dd81856020860161029b565b6102e6816102a9565b840191505092915050565b5f6020820190508181035f83015261030981846102b9565b905092915050565b5f80fd5b5f80fd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b61034f826102a9565b810181811067ffffffffffffffff8211171561036e5761036d610319565b5b80604052505050565b5f6103806101eb565b905061038c8282610346565b919050565b5f67ffffffffffffffff8211156103ab576103aa610319565b5b6103b4826102a9565b9050602081019050919050565b828183375f83830152505050565b5f6103e16103dc84610391565b610377565b9050828152602081018484840111156103fd576103fc610315565b5b6104088482856103c1565b509392505050565b5f82601f83011261042457610423610311565b5b81356104348482602086016103cf565b91505092915050565b5f60208284031215610452576104516101f4565b5b5f82013567ffffffffffffffff81111561046f5761046e6101f8565b5b61047b84828501610410565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806104c857607f821691505b6020821081036104db576104da610484565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261053d7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610502565b6105478683610502565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61058b6105866105818461055f565b610568565b61055f565b9050919050565b5f819050919050565b6105a483610571565b6105b86105b082610592565b84845461050e565b825550505050565b5f90565b6105cc6105c0565b6105d781848461059b565b505050565b5b818110156105fa576105ef5f826105c4565b6001810190506105dd565b5050565b601f82111561063f57610610816104e1565b610619846104f3565b81016020851015610628578190505b61063c610634856104f3565b8301826105dc565b50505b505050565b5f82821c905092915050565b5f61065f5f1984600802610644565b1980831691505092915050565b5f6106778383610650565b9150826002028217905092915050565b61069082610281565b67ffffffffffffffff8111156106a9576106a8610319565b5b6106b382546104b1565b6106be8282856105fe565b5f60209050601f8311600181146106ef575f84156106dd578287015190505b6106e7858261066c565b86555061074e565b601f1984166106fd866104e1565b5f5b82811015610724578489015182556001820191506020850194506020810190506106ff565b86831015610741578489015161073d601f891682610650565b8355505b6001600288020188555050505b50505050505056fea2646970667358221220d9c0cac87f2134218d478934e6fcc5b0ed967912a21e1ea8be5b613c8640110064736f6c634300081a0033'


# Deploy the contract
def deploy_contract(deployer_address,deployer_private_key):
    UserDataStorage = con.w3.eth.contract(abi=abi, bytecode=bytecode)

    # Build transaction
    construct_txn = UserDataStorage.constructor().build_transaction({
        'from': deployer_address,
        'nonce': con.w3.eth.get_transaction_count(deployer_address),
        'gas': 6721975,
        'gasPrice': con.w3.to_wei('21', 'gwei')
    })

    # Sign transaction
    signed_txn = con.w3.eth.account.sign_transaction(construct_txn, private_key=deployer_private_key)
    # Send transaction
    tx_hash = con.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for the transaction to be mined
    receipt = con.w3.eth.wait_for_transaction_receipt(tx_hash)
    # Print the deployed contract address
    contract_address = receipt.contractAddress
    return contract_address

# Store data for a user
def store_data(contract, address, private_key, data):
    if con.is_internet_available():
        contract_instance = con.w3.eth.contract(address=contract, abi=abi)
        # Build transaction
        txn_dict = contract_instance.functions.storeData(data).build_transaction({
            'from': address,
            'nonce': con.w3.eth.get_transaction_count(address),
            'gas': 2000000,
            'gasPrice': con.w3.to_wei('10', 'gwei')
        })
        # Sign transaction
        signed_txn = con.w3.eth.account.sign_transaction(txn_dict, private_key=private_key)
        # Send transaction
        tx_hash = con.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return tx_hash.hex()
    else:
        return None

# Retrieve data using event logs
def retrieve_data(contract, tx_hash):
    if con.is_internet_available():
        try:
            contract_instance = con.w3.eth.contract(address=contract, abi=abi)

            # Retrieve transaction receipt
            receipt = con.w3.eth.get_transaction_receipt(tx_hash)

            # Retrieve event logs
            logs = contract_instance.events.DataStored().process_receipt(receipt)

            # Print retrieved data
            if logs:
                user = logs[0]['args']['user']
                stored_data = logs[0]['args']['data']
                return True, user, stored_data
            else:
                return False, None, None
        except Exception as e:
            return False, None, None
    else:
        return False, None, None


### Deploy contract
##contract_address = deploy_contract("0x90d9F10E690D7b1C5Cd8eA9A7B3C5815E66931f6","2b6e820a51fdc093e7d6f00debf1a8e17e8d60b590f274bac5cfa74171aca987")
contract_address = "0xe0699ef746B5E4881FaB67e252970f8C620dfF81"

### Store data for a user
##user_address = admin1_address
##user_private_key = admin1_private_key
##data_to_store = "This is the data you want to store."
##tx_hash = store_data(contract_address, user_address, user_private_key, data_to_store)
##print(f"Data stored. Transaction Hash: {tx_hash}")

### Wait for transaction to be mined
##time.sleep(10)  # Adjust as necessary for the transaction to be mined
##
### Retrieve data using transaction hash
##flag, user, stored_data = retrieve_data(contract_address, tx_hash)
##if flag and user is not None and stored_data is not None:
##    print("Successfull", f"User :{user} and Data :{stored_data}")
##else:
##    print("Failed", f"No such transaction with hash: {tx_hash}")
