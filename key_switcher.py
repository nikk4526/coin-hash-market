"""
Key Switcher — определяет, использовался ли разный публичный ключ для одного адреса (через multisig или reuse).
"""

import sys
import requests

def fetch_transactions(address):
    url = f"https://blockstream.info/api/address/{address}/txs"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

def extract_pubkeys(tx):
    pubkeys = set()
    for vin in tx.get("vin", []):
        scriptsig = vin.get("scriptsig_asm", "")
        if "OP_PUSHBYTES_33" in scriptsig or "OP_PUSHBYTES_65" in scriptsig:
            parts = scriptsig.split()
            for part in parts:
                if len(part) in [66, 130]:  # compressed or uncompressed pubkey
                    pubkeys.add(part)
    return pubkeys

def main(address):
    print(f"🔍 Анализ адреса: {address}")
    try:
        txs = fetch_transactions(address)
    except Exception as e:
        print("❌ Ошибка при получении данных:", e)
        return

    all_pubkeys = set()
    for tx in txs:
        keys = extract_pubkeys(tx)
        all_pubkeys.update(keys)

    print(f"🔑 Найдено уникальных публичных ключей: {len(all_pubkeys)}")
    if len(all_pubkeys) > 1:
        print("⚠️ ВНИМАНИЕ: Похоже, что адрес использовался с разными ключами.")
    elif len(all_pubkeys) == 1:
        print("✅ Публичный ключ не менялся.")
    else:
        print("ℹ️ Публичные ключи не обнаружены (возможно, это bech32 или multisig адрес).")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python key_switcher.py <bitcoin_address>")
        sys.exit(1)
    main(sys.argv[1])
