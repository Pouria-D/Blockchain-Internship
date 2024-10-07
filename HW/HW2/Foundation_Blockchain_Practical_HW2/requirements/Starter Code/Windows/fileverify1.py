import hashlib
from bitcoin import SelectParams
from config import (my_private_key, my_public_key, my_address, network_type)
import requests
from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160
from bitcoin.core.script import *
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH


def send_from_custom_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey,txout_scriptPubKey2):
    txout1 = create_txout(amount_to_send, txout_scriptPubKey)
    txout2 = create_txout(0, txout_scriptPubKey2)
    txin = create_txin(txid_to_spend, utxo_index)

    txin_scriptSig = [create_OP_CHECKSIG_signature(txin, txout1, txout2, txin_scriptPubKey,my_private_key), my_public_key]
    new_tx = create_signed_transaction(txin, txout1, txout2, txin_scriptPubKey,
                                       txin_scriptSig)
    return broadcast_transaction(new_tx)


def create_txin(txid, utxo_index):
    return CMutableTxIn(COutPoint(lx(txid), utxo_index))


def create_txout(amount, scriptPubKey):
    return CMutableTxOut(amount*COIN, CScript(scriptPubKey))


def create_OP_CHECKSIG_signature(txin, txout1,txout2, txin_scriptPubKey, seckey):
    tx = CMutableTransaction([txin], [txout1, txout2])
    sighash = SignatureHash(CScript(txin_scriptPubKey), tx,
                            0, SIGHASH_ALL)
    sig = seckey.sign(sighash) + bytes([SIGHASH_ALL])
    return sig


def create_signed_transaction(txin: object, txout1: object, txout2: object, txin_scriptPubKey: object,
                              txin_scriptSig: object) -> object:
    """

    :rtype:
    """
    tx = CMutableTransaction([txin], [txout1, txout2])
    txin.scriptSig = CScript(txin_scriptSig)
    VerifyScript(txin.scriptSig, CScript(txin_scriptPubKey),
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    return tx


def broadcast_transaction(tx):
    raw_transaction = b2x(tx.serialize())
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    return requests.post(
        'https://api.blockcypher.com/v1/btc/test3/txs/push',
        headers=headers,
        data='{"tx": "%s"}' % raw_transaction)

###########################################################

#this code copied from the last HW
#use this function for hashing a file
##############################################################
def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.digest()
##############################################################

if __name__ == '__main__':
    ######################################################################
    SelectParams('testnet')
    filename = 'data.hex'
    message=sha256sum(filename)
    amount_to_send = 0.00000001
    txid_to_spend = (
        'f92c11798cd4ab4951bda2d9fe74af30e986f7b7c866047e9d3d6e2d34909048')
    # second tx id  'fb549c431a5d3b8fe4ef67bb21625b0c468bf55dc75305fcee7176574603962c'
    utxo_index = 1
    ######################################################################

    txout_scriptPubKey =[OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG]
    txout_scriptPubKey2 = [OP_RETURN, message]

    txin_scriptPubKey = [OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG]
    txin = create_txin(txid_to_spend, utxo_index)


    response=send_from_custom_transaction(amount_to_send,txid_to_spend, utxo_index,
                                          txin_scriptPubKey,txout_scriptPubKey, txout_scriptPubKey2)
    print(response.status_code, response.reason)
    print(response.text)


