# 🇨🇭 IDQ Quantum Random Number Generator (QRNG)

This module demonstrates **true quantum random numbers** sourced from **ID Quantique (IDQ)** hardware — a real physical quantum random number generator developed in Switzerland.

Unlike pseudorandom number generators (PRNGs), IDQ's device does **not** rely on algorithms or seeds. Its randomness comes directly from the fundamental uncertainty of quantum mechanics.

---

## 🧠 Physics Behind IDQ QRNG

IDQ QRNGs operate using **single-photon quantum behavior**:

1. A photon source emits **individual photons**
2. Each photon hits a **50/50 beam splitter**
3. Quantum mechanics gives each path a **50% probability**
4. Photon is detected in **Path A or Path B**
5.  
   - Detector A → outputs bit `0`  
   - Detector B → outputs bit `1`

There are **no hidden variables, no classical noise, and no simulation**.

This randomness arises from:

- **Wavefunction superposition**
- **Born rule probabilities**
- **Wavefunction collapse at detection**

> Each bit is fundamentally unpredictable, and can never be reproduced — even by the device itself.

This makes IDQ a **true physical quantum entropy source**.

---

## ✅ Why This Is True Quantum Randomness

| Property | IDQ QRNG | Software RNG |
|---|---|---|
Randomness Source | Single photon path choice | Algorithm |
Predictable? | ❌ Impossible | ✅ Yes |
Reproducible? | ❌ Never | ✅ With seed |
Physics Guarantee | ✅ Quantum mechanics | ❌ None |
Certifications | ETSI / Common Criteria / NIST tested | ❌ Not applicable |

---

## 📦 Code Example (Python)

```python
import requests

def get_idq_qrng_bytes(length=32):
    url = f"https://lfdr.de/qrng_api/qrng?length={length}&format=HEX"
    r = requests.get(url, timeout=8)
    r.raise_for_status()
    hex_str = r.json()["qrn"]
    qbytes = bytes.fromhex(hex_str)[:length]
    return qbytes

# Get 32 quantum bytes
qb = get_idq_qrng_bytes(32)
print("Quantum bytes:", qb.hex())
print("As integer:", int.from_bytes(qb, "big"))
