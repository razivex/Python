from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic

wallet_name = 'segwit_wallet_example'
w = Wallet.create(wallet_name, witness_type='segwit', keys=Mnemonic().generate(), network='bitcoin')

key = w.get_key()

print("Private Key:", key.wif)
print("Bitcoin Address:", key.address)
