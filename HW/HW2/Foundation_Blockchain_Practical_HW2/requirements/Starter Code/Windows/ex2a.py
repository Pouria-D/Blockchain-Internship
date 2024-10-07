from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from ex1 import send_from_P2PKH_transaction

######################################################################
Q2a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 9610, OP_EQUALVERIFY, OP_SUB, 6484, OP_EQUAL]
######################################################################
if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.000001
    txid_to_spend = (
        '738b56d4505431e2c5b6b151dfeaf3671650bc128489c1b264dd6789c22e91c2')
    utxo_index = 3
    ######################################################################
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
