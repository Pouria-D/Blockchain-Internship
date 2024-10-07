from sys import exit
from bitcoin.core.script import *
from utils import *
from config import *
from ex1 import send_from_P2PKH_transaction
######################################################################
'''
Redeem_script = [OP_1, my_public_key, Faraz_public_key, OP_2, OP_CHECKMULTISIGVERIFY,
                  OP_3, Shareholder1_public_key, Shareholder2_public_key, Shareholder3_public_key,
                      Shareholder4_public_key, Shareholder5_public_key, OP_5, OP_CHECKMULTISIG]
txout_scriptPubKey = [OP_HASH160, hashlib.sha160(str(Redeem_script).encode()), OP_EQUAL]
'''
txout_scriptPubKey = [OP_1, my_public_key, Faraz_public_key, OP_2, OP_CHECKMULTISIGVERIFY,
                        OP_3, Shareholder1_public_key, Shareholder2_public_key, Shareholder3_public_key,
                        Shareholder4_public_key, Shareholder5_public_key, OP_5, OP_CHECKMULTISIG]
######################################################################
if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00001
    txid_to_spend = (
        'f92c11798cd4ab4951bda2d9fe74af30e986f7b7c866047e9d3d6e2d34909048')
    utxo_index = 3
    ######################################################################
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
