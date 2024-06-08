import api.smartcontract.helper.Connection as con
from decimal import Decimal


# Function to get balance for an address
def get_balance(address):
    balance_wei = con.w3.eth.get_balance(address)
    balance_eth = con.w3.from_wei(balance_wei, 'ether')
    return Decimal(balance_eth)

def get_threshold_ether():
    threshold_ether = Decimal('2e-15')
    return threshold_ether
