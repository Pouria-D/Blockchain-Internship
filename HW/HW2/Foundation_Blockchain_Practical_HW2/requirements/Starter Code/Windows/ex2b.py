from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from ex1 import P2PKH_scriptPubKey
from ex2a import Q2a_txout_scriptPubKey


######################################################################
amount_to_send = 0.000000001
txid_to_spend = (
        '29503bdb1d7795f468e00e27ab8c6650918288479982d25045ddac7a245864a8')
utxo_index = 0
######################################################################
txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
txin_scriptSig = [8047, 1563]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
