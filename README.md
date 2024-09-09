---

# TirnBot - Bot Auto Bridge dari Optimism Sepolia ke antar chain Sepolia lainnya

TirnBot adalah sebuah bot otomatis yang memudahkan proses bridging token dari jaringan **Arbitrum Sepolia** ke **Base Sepolia**. Bot ini dikembangkan untuk mendukung pengguna yang ingin mengotomatisasi proses perpindahan aset antara dua jaringan testnet tersebut.

## Fitur
- **Auto Bridging:** Mengotomatisasi seluruh proses bridging token dari Arbitrum Sepolia ke Base Sepolia.
- **Real-time Transaction Feedback:** Menampilkan hasil transaksi yang berhasil dengan informasi hash transaksi secara real-time.
- **Koneksi Aman:** Menggunakan private key yang dienkripsi untuk memastikan keamanan transaksi.

## Persyaratan Sistem
- Python 3.7 atau lebih tinggi
- `web3.py` library
- `eth_account` library

## Instalasi

1. **Clone repository ini** ke dalam direktori lokal Anda:

   ```bash
   git clone https://github.com/vinskasenda/TirnBot.git
   ```

2. **Masuk ke direktori proyek**:

   ```bash
   cd TirnBot
   ```

3. **Install dependencies** yang diperlukan untuk menjalankan bot tanpa masalah:

   ```bash
   pip install web3 eth-account
   ```

## Konfigurasi

1. Buka file `bot.py` menggunakan text editor.
2. Temukan bagian berikut dalam kode:
   ```python
   private_key = 'YOUR_PRIVATE_KEY'
   my_address = 'YOUR_WALLET_ADDRESS'
   ```
3. Ganti `YOUR_PRIVATE_KEY` dan `YOUR_WALLET_ADDRESS` dengan private key dan alamat wallet Anda.

> **Catatan:** Pastikan untuk menjaga kerahasiaan private key Anda. Jangan membagikan atau menyimpan private key di tempat yang tidak aman.

## Penggunaan

Setelah melakukan konfigurasi, Anda dapat menjalankan bot dengan perintah berikut:

   ```bash
   python bot.py
   ```

Bot akan mulai berjalan dan secara otomatis melakukan bridging dari Arbitrum Sepolia ke Base Sepolia. Anda dapat memantau hasil transaksi di terminal dengan tampilan hash transaksi yang berhasil.

## Kontribusi

Kami menerima kontribusi dari siapapun yang ingin membantu pengembangan TirnBot. Jika Anda ingin berkontribusi:

1. Fork repository ini.
2. Buat branch baru untuk fitur atau perbaikan Anda.
3. Lakukan perubahan dan kirim pull request.

## Lisensi

TirnBot dilisensikan di bawah [MIT License](LICENSE).

---

README ini telah diperbaiki dengan struktur yang lebih rapi, informasi tambahan terkait keamanan, dan instruksi yang jelas.
