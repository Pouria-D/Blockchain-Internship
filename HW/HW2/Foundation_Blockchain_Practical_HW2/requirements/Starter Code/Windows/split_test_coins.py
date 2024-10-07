from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from config import (my_private_key, my_public_key, my_address,
    alice_secret_key_BTC, alice_public_key_BTC, alice_address_BTC,
    bob_secret_key_BTC, bob_public_key_BTC, bob_address_BTC,
    alice_secret_key_BCY, alice_public_key_BCY, alice_address_BCY,
    bob_secret_key_BCY, bob_public_key_BCY, bob_address_BCY,
    faucet_address, network_type)

from utils import create_txin, create_txout, broadcast_transaction



def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO: set these parameters correctly
    private_key = bob_secret_key_BCY
    public_key = bob_secret_key_BCY.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)

    amount_to_send = 0.009
    txid_to_spend = (
        '9f23561b5fa3ad386b706a84a55eeead1a9809cb78f21991d63ccf363042a3a8')
    utxo_index = 0
    n = 10
    # For n, choose a number larger than what you immediately need, 
    # in case you make mistakes.
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network_type)
