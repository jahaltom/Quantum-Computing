# Quantum Coin Flip (IBM Quantum Runtime)

This project demonstrates a **true quantum coin flip** using IBM Quantum's real superconducting qubit hardware.

## 🧠 Quantum Idea

A classical coin flip is based on chaotic physics but is ultimately deterministic if fully known.  
A **quantum coin flip** uses **qubit superposition**:



$|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}$


|0⟩

- A qubit in state zero — the quantum version of a classical bit 0.

  - Not random yet

  - Fully known, fully classical-looking state

  - Think: a coin resting on tails before flipping.


Then we **measure**, collapsing the qubit to either `0` or `1` with ~50/50 probability.

This randomness is **fundamental**, not classical noise.

## ⚙️ How It Works

1. Initialize a qubit in state |0⟩
2. Apply a Hadamard gate `H` to create equal superposition
3. Measure the qubit
4. Repeat many times (shots) to build statistics

## 🧪 Circuit

```
|0> ── H ── ●  → measure
```

H = Hadamard gate, puts qubit into superposition  
● = measurement

## 📦 Environment Setup

```bash
pip install qiskit qiskit-ibm-runtime matplotlib
```

## 🔑 IBM Token Setup

Replace YOUR_TOKEN with your IBM Quantum API token:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token="YOUR_TOKEN", overwrite=True)
```




## 📈 Expected Output

Approximately:

```
0: ~1000
1: ~1000
```

Small bias possible due to qubit noise and readout error.

## 🧬 Quantum Concept Summary

| Concept | Meaning |
|--------|--------|
Superposition | Qubit exists in |0⟩ and |1⟩ simultaneously
Measurement | Collapses state to classical bit
Hadamard gate | Creates equal probability amplitudes
Quantum randomness | Fundamentally unpredictable

## 🔗 References

- IBM Quantum Runtime Docs
- Qiskit Textbook
- Wheeler’s delayed-choice experiment inspiration: **randomness from measurement**

---


