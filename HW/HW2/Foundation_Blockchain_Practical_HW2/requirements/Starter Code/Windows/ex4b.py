
from sys import exit
from bitcoin.core.script import *

from utils4 import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from ex1 import (P2PKH_scriptPubKey, P2PKH_scriptSig)


######################################################################
amount_to_send = 0.00000001
txid_to_spend = (
        'f9fec11f69efec81243437f7fea949f28bf1ae9c6b13295f222eec382d2b83b4')
utxo_index = 0

txin_scriptPubKey = [1635710,
    OP_CHECKLOCKTIMEVERIFY,
    OP_DROP,
    OP_DUP,
    OP_HASH160,
    my_address,
    OP_EQUALVERIFY,
    OP_CHECKSIG]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)
txin = create_txin(txid_to_spend, utxo_index)
txin.nSequence = 0x00000000
signature = create_OP_CHECKSIG_signature(txin, txout, txout_scriptPubKey, my_private_key)
txin_scriptSig = [signature, my_public_key]
response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
