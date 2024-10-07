from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

#network_type = 'bcy-test'
network_type = 'btc-test3'
######################################################################
my_private_key = CBitcoinSecret(
    'cPf66MAw7hssQy7ae9QpRRL4qk4Bfb53vVoBYnomYWbMwcKB5wtC')
# address : mjuqa6AoyGUGREJiZ13sDkUV55WeiRcoGd
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################
#####  For Question3 :
Faraz_private_key=CBitcoinSecret(
    'cRwC2yiQpZPSXn6M5Y2iHM9T3f9iRn6ECxhQNCHYU3H9j7667YTd')
# address : n2bVt3P2CZt3CY564D8JLHiPxTWjnXN4Bv
Faraz_public_key=Faraz_private_key.pub
Faraz_address=P2PKHBitcoinAddress.from_pubkey(Faraz_public_key)

Shareholder1_private_key=CBitcoinSecret(
    'cPhKb76XFWWUCdA2oNNV92ikrjKZkscY8KHW7uhYuaYGPZomF9W3')
# address : mmJWHmzopDBZcC5kV8YEUWn8qUcJoojiP5
Shareholder1_public_key = Shareholder1_private_key.pub
Shareholder1_address = P2PKHBitcoinAddress.from_pubkey(Shareholder1_public_key)

Shareholder2_private_key=CBitcoinSecret(
    'cRhufdrPY7jE9fnXM5eMZUr9XKwo9fzQFVCutKDqnXLRKkoXsmNL')
# address : mmTxH2tCUXcfZw6haD9gfA42dDVpj8r2xC
Shareholder2_public_key = Shareholder2_private_key.pub
Shareholder2_address = P2PKHBitcoinAddress.from_pubkey(Shareholder2_public_key)

Shareholder3_private_key=CBitcoinSecret(
    'cVVpbZDihYzVNn11QypSrU8n9mtKQF7Dv7QC9VtHEyv5NVYjvDsx')
# address : n47Wjox17KTXpScE2x1ph1L1kJJH4gUJ5s
Shareholder3_public_key = Shareholder3_private_key.pub
Shareholder3_address = P2PKHBitcoinAddress.from_pubkey(Shareholder3_public_key)

Shareholder4_private_key=CBitcoinSecret(
    'cT9etKbfPo3vNyzA5FCaXnDrdgjNQBWozvxxygr6u5t6rzoxwrJh')
# address : n39Psb8si6UbZn7xtomzeb6mdj3CUtHgsY
Shareholder4_public_key = Shareholder4_private_key.pub
Shareholder4_address = P2PKHBitcoinAddress.from_pubkey(Shareholder4_public_key)

Shareholder5_private_key=CBitcoinSecret(
    'cRkZ2EcF4BEvZiv27TxcXKEMAaWK4vMS9bS4izisgs811LE1hWfp')
# address : mzKDL1yweKQUgyxjKQpmX4X6muYWSWEfNv
Shareholder5_public_key = Shareholder5_private_key.pub
Shareholder5_address = P2PKHBitcoinAddress.from_pubkey(Shareholder5_public_key)

######################################################################

# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cTbQ1CJXjoeghgio9uupfMRbc5Rg6vtN1JiSEfi1s9hpov45nL3V')
# address : mfnEbwyEV4EAxeF3nfyj7LohsjiewCw152
# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cNkn3KrCuhAEswNtvTnmuPPRfFJ9ABdL2onAqpwfkimBiFoxEDkn')
# address : mh64z9ZsGTF5dEVqxWv3XCMJXL6QBYGX1S
# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)

######################################################################
'''
alice :
"private": "67d643f999f181e51654e9399ced7354503663f919cb4257cd364aa971d864e2",
  "public": "03b8b727874acdcd409d78f6b29ea5972f367644a78d6fe7633f938864aae57891",
  "address": "CEHymfA1prp8EFhZZ2uJAW1JzcEbvy1FY1",
  "wif": "Brosn5TUrG4Vq7cZSqdpFfjFvVdHaAGwu7BjzC94tw4dq32CBSTf"
  
  "tx_ref": "5e39618c138067ad11afcd65ab32a034b6b10eb81061bf5ded30073184b2ff01"
    
bob:
 "private": "2387e08d4da0d54d1e950666c0ddac31222e16a7f8f8b79f7013f63f8e5bf5df",
  "public": "02e415b0034424f0124cdeab828f7bf280e19cf94447690e57cc187bd73dd46e88",
  "address": "C2hbVcAz6xLBWsxXoWCLQw22ny2Gywieuc",
  "wif": "BpX6dkoBq96R6ibvpsK7et6cYP5YKuv8mLsV4HRsdeN8LEqzS56w"
  
  "tx_ref": "9f23561b5fa3ad386b706a84a55eeead1a9809cb78f21991d63ccf363042a3a8"
  
'''

######################################################################

# Only to be imported by alice.py

alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('67d643f999f181e51654e9399ced7354503663f919cb4257cd364aa971d864e2'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('2387e08d4da0d54d1e950666c0ddac31222e16a7f8f8b79f7013f63f8e5bf5df'))

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################