## 🔒 ANU Quantum Random Number Generator (QRNG)

This project fetches **true quantum-generated randomness** from the Australian National University’s public QRNG API.

Unlike pseudorandom algorithms, this entropy comes from **quantum vacuum fluctuations** — an inherently unpredictable physical process guaranteed by quantum mechanics.

### 🧠 How It Works

At the quantum level, empty space is not “empty” — it constantly fluctuates. ANU:

1. Shines a laser into a vacuum chamber  
2. Measures unpredictable vacuum photon fluctuations  
3. Converts that noise directly into **random bytes**  
4. Publishes them via a public API

This randomness is **non-deterministic, non-repeatable, and cannot be predicted or reproduced**.

### ✅ Why Use True Quantum Randomness?

| Feature | ANU QRNG | Software PRNG |
|--------|---------|---------------|
Source | Quantum vacuum noise | Mathematical algorithm |
Predictable | ❌ Impossible | ✅ Possible in principle |
Entropy | Physical entropy | Computed entropy |
Best Use | Cryptography, security research, randomness studies, simulation | Games, general apps, non-security RNG |

### 🚀 Minimal Python Example

```python
import requests

def get_qrng_bytes(length=32):
    url = f"https://qrng.anu.edu.au/API/jsonI.php?length={length}&type=uint8"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    qrng_raw = data["data"]
    qrng_bytes = bytes(qrng_raw)
    print("Quantum bytes:", qrng_bytes.hex())
    return qrng_bytes

get_qrng_bytes(32)
