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



## 🔬 Core Quantum Equation & Circuit Physics

The circuit performs the transformation:

```text
|0> --H--> (|0> + |1>) / √2 --measure--> {0,1}
```

or in math:

$$
|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

---

### 1️⃣ Initial State

The qubit begins in the computational basis state:

$$
|0\rangle =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

A pure, definite state — the qubit is fully aligned with the Z‑axis (north pole of Bloch sphere).

---

### 2️⃣ Apply the Hadamard Gate \(H\)

The Hadamard creates an **equal superposition**:

$$
H =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

Applying \(H\) to \(|0\rangle\):

$$
H|0\rangle
=
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
1
\end{bmatrix}
=
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

After this, the qubit is **not “0 or 1”** — it is in a **coherent superposition of both**.

---

### 3️⃣ Measurement & Born Rule

Upon measurement, the quantum state collapses:

$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\quad\longrightarrow\quad
\begin{cases}
|0\rangle & \text{with probability } \frac{1}{2} \\
|1\rangle & \text{with probability } \frac{1}{2}
\end{cases}
$$

Born rule:

$$
\left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}
$$

> This randomness is **fundamental** — not classical chaos or noise.  
> When measured, the qubit must “choose” a single outcome.

---

### 🌐 Bloch Sphere View

| Stage | Bloch Sphere Interpretation |
|---|---|
Before Hadamard | Qubit at **north pole** (\(|0⟩\)) |
After Hadamard | Qubit on **equator**, pointing +X (equal 0/1 probability) |
Measurement | Projection to poles → **collapse to \(|0⟩\) or \(|1⟩\)** |

Superposition = qubit on equator  
Measurement = projection to poles

---

### ✅ Summary

- Prepare qubit in \(|0⟩\)
- Apply Hadamard → **superposition**
- Measure → **true quantum randomness**

This experiment showcases:
- Superposition  
- Born rule  
- Wavefunction collapse  
- Quantum randomness (not simulatable classically)

This is the **quantum coin flip** — the simplest real demonstration of quantum mechanics in action.



