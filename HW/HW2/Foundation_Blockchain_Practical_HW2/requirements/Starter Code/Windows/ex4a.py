
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from ex1 import send_from_P2PKH_transaction

# jUST NEED TO CHANGE SCRIPT PUBKEY ...
######################################################################

txout_scriptPubKey = [1635710,
    OP_CHECKLOCKTIMEVERIFY,
    OP_DROP,
    OP_DUP,
    OP_HASH160,
    my_address,
    OP_EQUALVERIFY,
    OP_CHECKSIG]
######################################################################
if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00002
    txid_to_spend = (
        '09679f0471013c55fd3a268a128bfb39257c8cc8635110941fe48840e9917d28')
    utxo_index = 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
'''
from config import (my_private_key, my_public_key, my_address, network_type)
from bitcoin.core.script import *

from utils import *

#####################
def P2PKH_scriptPubKey(address):
    ######################################################################
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    return [signature, my_public_key]
    ######################################################################


def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin_scriptPubKey = P2PKH_scriptPubKey(my_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)
    return broadcast_transaction(new_tx, network_type)


if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00001
    txid_to_spend = (
        'f92c11798cd4ab4951bda2d9fe74af30e986f7b7c866047e9d3d6e2d34909048')
    utxo_index = 8
    ######################################################################
    timelock = 1635481
    txout_scriptPubKey = [timelock, OP_CHECKLOCKTIMEVERIFY, OP_DROP,
                          OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG]
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
    '''