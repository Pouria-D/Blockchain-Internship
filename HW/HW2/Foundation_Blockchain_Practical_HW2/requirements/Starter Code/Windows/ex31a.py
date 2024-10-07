from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *
from ex1 import send_from_P2PKH_transaction

######################################################################
txout_scriptPubKey = [OP_DEPTH, OP_3, OP_EQUAL, OP_IF, OP_2, my_public_key, Faraz_public_key, OP_2, OP_CHECKMULTISIG, OP_ELSE,
                        OP_1, my_public_key, Faraz_public_key, OP_2, OP_CHECKMULTISIGVERIFY,
                        OP_3, Shareholder1_public_key, Shareholder2_public_key, Shareholder3_public_key, Shareholder4_public_key, Shareholder5_public_key, OP_5, OP_CHECKMULTISIG, OP_ENDIF]
######################################################################
if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00001
    txid_to_spend = (
        'e82b87bc764dd31e4fe50f158b63f4fd55e815dde6ac79271b5efd6c522f68f4')
    utxo_index = 1
    ######################################################################
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
