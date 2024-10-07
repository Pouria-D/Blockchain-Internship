from bitcoin.core.script import *

######################################################################

def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [OP_DUP, OP_HASH160, hash_of_secret, OP_EQUAL, OP_IF, OP_DROP, public_key_recipient, OP_CHECKSIG, OP_ELSE, OP_2,
            public_key_recipient, public_key_sender, OP_2, OP_CHECKMULTISIG, OP_ENDIF]


# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [sig_recipient, secret]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [OP_0, sig_sender, sig_recipient]

######################################################################

######################################################################
#
# Configured for your addresses


alice_txid_to_spend     = "c8f357eef428daedcf1cbe97af77b01a662a1d6a8bfe430d87936c139bcc255d"
alice_utxo_index        = 1
alice_amount_to_send    = 0.000001

bob_txid_to_spend       = "4cbb29bec08bd4b3ae40d20f5e3e3ec490079fdbac193a4ae2b8b2397e0e978f"
bob_utxo_index          = 0
bob_amount_to_send      = 0.000001

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height  = 1635564

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height   = 2675691

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

broadcast_transactions = False
alice_redeems = True

######################################################################
