from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import (my_private_key, my_public_key, my_address, network_type)
from bitcoin.core.script import *

from merkle import *

##############################################################
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

# generating address based on merkle root hash : ( copied structure from keygen )

    SelectParams('testnet')
    Number_of_files = 20
    merkleroot = MerkleTreeCalculator.calculate_merkle_root(True, Number_of_files)
    # private = merkle = cViNbssmQTHeZBWMpwATAnQPhnpVbPv57FmkoAU72YQkmhMN5cFa
    # address = cda62b150893906987147762964a1bd64dbef4d8714f0abcf04dd871692ab528
    seckey = CBitcoinSecret.from_secret_bytes(merkleroot)
    address = P2PKHBitcoinAddress.from_pubkey(seckey.pub)
    print('private key: %s' % seckey)
    Reciever_address = address
    #############################################
    amount_to_send = 0.00000001
    txid_to_spend = (
        'f92c11798cd4ab4951bda2d9fe74af30e986f7b7c866047e9d3d6e2d34909048')
    # second tx id  'fb549c431a5d3b8fe4ef67bb21625b0c468bf55dc75305fcee7176574603962c'
    utxo_index = 4
    ######################################################################
    txout_scriptPubKey = P2PKH_scriptPubKey(Reciever_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)

