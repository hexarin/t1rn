from web3 import Web3
from eth_account import Account
import time
import sys

# Detail jaringan
private_key = '#'  # Ganti dengan private key Anda
rpc_url = 'https://sepolia.optimism.io'
chain_id = 11155420
contract_address = '0xF221750e52aA080835d2957F2Eed0d5d7dDD8C38'
my_address = '#'  # Ganti dengan address Anda

# Koneksi ke jaringan
web3 = Web3(Web3.HTTPProvider(rpc_url))
if not web3.is_connected():
    raise Exception("Tidak dapat terhubung ke jaringan")

# Buat akun dari private key
account = Account.from_key(private_key)

# Data transaksi untuk bridge
data = '0x56591d59617262740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004CBB1421DF1CF362DC618d887056802d8adB7BC000000000000000000000000000000000000000000000000000237cd2a2bacb0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002386f26fc10000'

# Fungsi untuk membuat dan mengirim transaksi
def send_bridge_transaction():
    # Ambil nonce untuk alamat pengirim
    nonce = web3.eth.get_transaction_count(my_address)

    # Estimasi gas
    try:
        gas_estimate = web3.eth.estimate_gas({
            'to': contract_address,
            'from': my_address,
            'data': data,
            'value': web3.to_wei(0.01, 'ether')  # Mengirim 0.01 ETH
        })
        gas_limit = gas_estimate + 10000  # Tambahkan buffer gas
    except Exception as e:
        print(f"Error estimating gas: {e}")
        return None

    # Buat transaksi
    transaction = {
        'nonce': nonce,
        'to': contract_address,
        'value': web3.to_wei(0.01, 'ether'),  # Mengirim 0.01 ETH
        'gas': gas_limit,
        'gasPrice': web3.eth.gas_price,
        'chainId': chain_id,
        'data': data
    }

    # Tanda tangani transaksi dengan private key
    try:
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
    except Exception as e:
        print(f"Error signing transaction: {e}")
        return None

    # Kirim transaksi
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return web3.to_hex(tx_hash)
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

# Jalankan script sampai dihentikan secara manual
successful_txs = 0

try:
    while True:
        tx_hash = send_bridge_transaction()
        if tx_hash:
            successful_txs += 1
            print(f"Tx Hash: {tx_hash} | Total Tx Sukses: {successful_txs}")
        time.sleep(60)  # Delay 60 detik setiap transaksi
except KeyboardInterrupt:
    print("\nScript dihentikan oleh pengguna.")
    print(f"Total transaksi sukses: {successful_txs}")
    sys.exit(0)
