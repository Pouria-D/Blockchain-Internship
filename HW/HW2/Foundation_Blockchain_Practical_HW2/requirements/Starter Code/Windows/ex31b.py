from sys import exit
from bitcoin.core.script import *
from utils import *
from config import *
from ex31a import txout_scriptPubKey

######################################################################
amount_to_send = 0.00000001
txid_to_spend = (
        '5352f40cb8599ea67a63b335fd6f8df12f9747f66fc358e452dba3a541c3c024')
utxo_index = 0
######################################################################
txin_scriptPubKey = txout_scriptPubKey
######################################################################
txin = create_txin(txid_to_spend, utxo_index)
txout = create_txout(amount_to_send, txout_scriptPubKey)
######################################################################

# First Case ; 2 Owners sign Tx:
# building script sig and response
txout_scriptPubKey = [OP_DUP, OP_HASH160, faucet_address, OP_EQUALVERIFY, OP_CHECKSIG]
txout = create_txout(amount_to_send, txout_scriptPubKey)
txin = create_txin(txid_to_spend, utxo_index)
txin_scriptSig = [OP_0, create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key),
create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, Faraz_private_key)
]
new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
txin_scriptSig)
response = broadcast_transaction(new_tx, 'btc-test3')
'''
# second Case ; 1 Owner & 3 Shareholders:
# building script sig and response
txout_scriptPubKey = [OP_DUP, OP_HASH160, faucet_address, OP_EQUALVERIFY, OP_CHECKSIG]
txout = create_txout(amount_to_send, txout_scriptPubKey)
txin = create_txin(txid_to_spend, utxo_index)
txin_scriptSig = [OP_0, create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, Shareholder1_private_key),
                          create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, Shareholder2_private_key),
                          create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, Shareholder3_private_key),
                          OP_0, create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key)
                          ]
new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
txin_scriptSig)
response = broadcast_transaction(new_tx, 'btc-test3')
'''
print(response.status_code, response.reason)
print(response.text)
