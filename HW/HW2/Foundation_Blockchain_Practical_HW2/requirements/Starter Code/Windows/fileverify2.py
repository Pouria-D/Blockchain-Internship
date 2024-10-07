import hashlib
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import (my_private_key, my_public_key, my_address, network_type)
from bitcoin.core.script import *

# main structure is from ex1 code ; changing the receiver address ...

# Hashing a file
##############################################################
def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.digest()
##############################################################

def P2PKH_scriptPubKey(address):

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
    # in ex1 the receiver is faucet ; now replce it by address which is produced by hash file :
    SelectParams('testnet')
    filename = 'data.hex'
    secretkey = CBitcoinSecret.from_secret_bytes(sha256sum(filename))
    destination_address = P2PKHBitcoinAddress.from_pubkey(secretkey.pub)

    #############################################################
    amount_to_send = 0.00000001
    txid_to_spend = (
        'f92c11798cd4ab4951bda2d9fe74af30e986f7b7c866047e9d3d6e2d34909048')
    utxo_index = 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(destination_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)


