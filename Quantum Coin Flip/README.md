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


# Quantum Coin Flip — Understanding the Equation & Circuit

This project demonstrates the simplest real quantum algorithm:  
a **quantum coin flip** run on IBM Quantum hardware.

A qubit is:

1. Prepared in state `|0⟩`
2. Put into **superposition** with a Hadamard gate `H`
3. Measured — forcing nature to choose `0` or `1`

This produces **true quantum randomness**, not pseudo‑random numbers.

---

## 🔬 Core Quantum Equation

The circuit performs the following transformation:

```text
|0> --H--> (|0> + |1>) / √2 --measure--> {0,1}
```

Mathematically:

$$
|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

This means:

- The qubit **starts definitely** as `|0⟩`
- After `H`, it becomes a **superposition**  
- Measurement collapses it into `0` or `1` with equal probability

---

## 1️⃣ Initial State

A qubit initialized in `|0⟩` is:

$$
|0\rangle =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

A pure basis state — fully “up” on the Bloch sphere.

---

## 2️⃣ Apply the Hadamard Gate \(H\)

The Hadamard gate creates equal superposition:

$$
H =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

Apply it to the starting state:

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

At this point the qubit is **in both states at once**.

---

## 3️⃣ Measurement & Born Rule

Upon measurement:

$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\quad\longrightarrow\quad
\begin{cases}
|0\rangle & \text{with probability } \tfrac{1}{2} \\
|1\rangle & \text{with probability } \tfrac{1}{2}
\end{cases}
$$

Born rule calculation:

$$
\left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}
$$

> The randomness is **fundamental**, not due to noise or lack of information.

---

## 🌐 Bloch Sphere Interpretation

| Stage | Bloch Sphere Meaning |
|---|---|
Before `H` | State at **north pole** (`|0⟩`) |
After `H` | Point on **equator** — equal probability |
Measurement | Projection to poles = collapse to `0` or `1` |

---

## ✅ Summary

- Start at `|0⟩`
- Apply `H` → superposition
- Measure → `0` or `1` with 50% probability each

This simple circuit reveals the core of quantum mechanics:

> **Quantum states exist in multiple possibilities until you observe them.**

✅ Clean LaTeX  
✅ GitHub‑compatible  
✅ Clear physics explanation  

Paste this file as your `README.md` in GitHub.

