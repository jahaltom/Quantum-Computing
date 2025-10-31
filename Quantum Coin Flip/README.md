# Quantum Coin Flip (IBM Quantum Runtime)

This project demonstrates a **true quantum coin flip** using IBM Quantum's real superconducting qubit hardware.

## 🧠 Quantum Idea

A classical coin flip is based on chaotic physics but is ultimately deterministic if fully known.  
A **quantum coin flip** uses **qubit superposition**:

|0⟩ --H--> (|0⟩ + |1⟩) / √2

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

## 🚀 Run the coin flip

```python
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import Sampler
import matplotlib.pyplot as plt

service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=1)

qc = QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

sampler = Sampler(mode=backend)
job = sampler.run([qc], shots=2000)
counts = job.result()[0].join_data().get_counts()

print(counts)

plt.bar(counts.keys(), counts.values())
plt.title(f"Quantum Coin Flip on {backend.name}")
plt.xlabel("Outcome"); plt.ylabel("Counts");
plt.show()
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

If this showed `50/50`, congrats — you generated **real quantum entropy** ⚡🧠
