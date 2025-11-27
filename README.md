# EVM Wallet Generator - Advanced Edition

Script Python untuk generate multiple EVM-compatible wallet (Ethereum, BSC, Polygon, dll) dengan mnemonic phrase dan private key. Dilengkapi dengan CLI interface yang user-friendly dan multiple output format.

## ✨ Fitur Utama

- **Batch Generation** - Generate ribuan wallet sekaligus dengan cepat
- **Multiple Output Format** - TXT, JSON, dan CSV
- **Flexible Mnemonic** - Support 12 words (128-bit) dan 24 words (256-bit)
- **CLI & Interactive Mode** - Command-line arguments atau interactive prompt
- **Progress Tracking** - Real-time progress indicator untuk batch besar
- **Colored Output** - Terminal output dengan ANSI colors untuk readability
- **Performance Stats** - Menampilkan statistik waktu generation

## 🔧 Requirements
```bash
pip install eth-account mnemonic
```

Atau install dari `requirements.txt`:
```bash
pip install -r requirements.txt
```

## 🚀 Cara Penggunaan

### Interactive Mode (Recommended)
```bash
python generate.py
```
Script akan menanyakan:
- Jumlah wallet yang ingin digenerate
- Mnemonic strength (12 atau 24 kata)
- Format output (TXT/JSON/CSV)
- Tampilkan output di console atau tidak

### Command Line Mode
```bash
# Generate 10 wallet dengan 12 words mnemonic, output TXT
python generate.py -n 10

# Generate 50 wallet dengan 24 words mnemonic, output JSON, quiet mode
python generate.py -n 50 -s 256 -f json -q

# Generate dengan custom output directory
python generate.py -n 100 -o my_wallets -f csv
```

### Command Line Options
```
-n, --number      Jumlah wallet yang akan digenerate
-s, --strength    Mnemonic strength: 128 (12 kata) atau 256 (24 kata)
-f, --format      Output format: txt, json, atau csv
-q, --quiet       Quiet mode (tidak tampilkan wallet di console)
-o, --output      Custom output directory (default: wallets/)
```

## 📂 Output Files

### Format TXT (Default)
Menghasilkan 3 file terpisah:
- `wallet_[timestamp]_mnemonic.txt` - Mnemonic phrases
- `wallet_[timestamp]_privatekeys.txt` - Private keys (hex)
- `wallet_[timestamp]_addresses.txt` - Wallet addresses

### Format JSON
Menghasilkan 1 file JSON dengan struktur:
```json
[
  {
    "wallet_number": 1,
    "mnemonic": "witch collapse practice...",
    "private_key": "0x1234...",
    "address": "0xabcd...",
    "created_at": "2024-01-15T10:30:00"
  }
]
```

### Format CSV
Menghasilkan 1 file CSV dengan kolom:
```
Wallet_Number,Mnemonic,Private_Key,Address
```

## 📊 Performance

- **Speed**: ~0.15-0.3 detik per wallet (tergantung hardware)
- **Batch**: Dapat generate 1000+ wallet dalam hitungan menit
- **Progress**: Real-time progress indicator untuk batch > 10 wallet

## 🔐 Kompatibilitas Blockchain

Script ini generate wallet yang kompatibel dengan semua EVM-based blockchain:

- ✅ Ethereum (ETH)
- ✅ Binance Smart Chain (BSC)
- ✅ Polygon (MATIC)
- ✅ Avalanche C-Chain
- ✅ Fantom Opera
- ✅ Arbitrum
- ✅ Optimism
- ✅ Dan semua EVM-compatible chain lainnya

## 💡 Use Cases

- Development & Testing environments
- Airdrop preparation (multiple addresses)
- Batch wallet creation untuk project
- Cold wallet generation (offline usage)

## ⚠️ Security Warning

**SANGAT PENTING - BACA INI:**

1. **JANGAN PERNAH** upload file output ke GitHub atau cloud storage
2. **JANGAN SHARE** private key atau mnemonic phrase kepada siapapun
3. **GUNAKAN** di environment yang aman (offline recommended untuk production)
4. **BACKUP** file dengan encryption jika perlu disimpan
5. **DELETE** file setelah import ke wallet manager

### Tambahkan ke `.gitignore`:
```gitignore
# Wallet files - NEVER COMMIT THESE
wallets/
*.txt
*.json
*.csv
*_mnemonic*
*_privatekeys*
*_addresses*
```

## 📋 Installation

1. Clone repository:
```bash
git clone https://github.com/Jauhar40/Generate-EVM-Wallet.git
cd evm-wallet-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run script:
```bash
python generate.py
```

## 🛠️ Technology Stack

- **eth-account** - Ethereum account management
- **mnemonic** - BIP39 mnemonic generation
- **Python 3.7+** - Core language

## 📖 Example Usage
```bash
# Generate 5 wallet untuk testing
python generate.py -n 5 -f json

# Generate 100 wallet untuk airdrop
python generate.py -n 100 -q -f csv -o airdrop_wallets

# Generate dengan 24-word mnemonic untuk extra security
python generate.py -n 10 -s 256 -f json
```

## 🎯 Output Example
```
╔═══════════════════════════════════════════════════════════════╗
║              EVM Wallet Generator - Advanced Edition         ║
║                     Created by Flexoryn                       ║
╚═══════════════════════════════════════════════════════════════╝

⚙️  Generating 5 EVM wallets...

🔐 Wallet #1
🧠 Mnemonic    : witch collapse practice feed shame...
🔑 Private Key : 0x1234567890abcdef...
🏦 Address     : 0xAbCdEf1234567890...

✅ Generation Complete!
📊 Summary:
   • Total wallets: 5
   • Time elapsed: 1.23 seconds
   • Output directory: /path/to/wallets
```

## ⚖️ License

MIT License - Free to use for personal and commercial projects

## ⚠️ Disclaimer

Tool ini dibuat untuk keperluan **development dan testing**. Author tidak bertanggung jawab atas:
- Kehilangan aset akibat penggunaan yang tidak aman
- Penyalahgunaan tool untuk tujuan illegal
- Keamanan wallet yang digenerate

**Selalu gunakan hardware wallet atau cold storage untuk menyimpan aset crypto dalam jumlah besar.**

---

**Created by Flexoryn** | [Report Issues](https://github.com/Jauhar40/Generate-EVM-Wallet.git)
