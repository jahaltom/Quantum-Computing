# Quantum Coin Flip — IBM Quantum Hardware Demo (GitHub‑Optimized)

This README explains the **equation** and the **circuit** for a one‑qubit, Hadamard‑based quantum coin flip run on IBM Quantum hardware — with equations formatted to render cleanly on GitHub (MathJax).

---

## 🔬 Core Transformation

```text
|0> --H--> (|0> + |1>) / √2 --measure--> {0, 1}
```

Mathematically:

$$
|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

This means the qubit starts as a definite basis state, is placed into **equal superposition** by \(H\), and then **collapses** to a classical bit on measurement.

---

## 1️⃣ Initial State

A qubit initialized in \(|0\rangle\) is represented as the column vector:

$$
|0\rangle =
\begin{bmatrix}
1 \\\\
0
\end{bmatrix}
$$

This is a **pure basis state** (north pole on the Bloch sphere).

---

## 2️⃣ Hadamard Gate \(H\)

The Hadamard gate creates an equal superposition of \(|0\rangle\) and \(|1\rangle\):

$$
H =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\\\
1 & -1
\end{bmatrix}
$$

Applied to \(|0\rangle\):

$$
H|0\rangle
=
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\\\
1
\end{bmatrix}
=
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

After this step, the qubit is **not** “0 or 1”; it is a **coherent superposition** of both.

---

## 3️⃣ Measurement & Born Rule

Measuring the superposed state forces a definite classical result:

$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\;\longrightarrow\;
\begin{cases}
|0\rangle & \text{with probability } \tfrac{1}{2}, \\\\
|1\rangle & \text{with probability } \tfrac{1}{2}.
\end{cases}
$$

Born rule check:

$$
\Bigl|\tfrac{1}{\sqrt{2}}\Bigr|^2 = \tfrac{1}{2}.
$$

> The randomness here is **fundamental** (quantum), not classical noise or ignorance.

---

## 🌐 Bloch Sphere View

| Stage        | Interpretation                                                                 |
|--------------|---------------------------------------------------------------------------------|
| Before \(H\) | State at **north pole** (\(|0\rangle\)).                                        |
| After \(H\)  | State on the **equator**, pointing along \(+X\) (equal 0/1 amplitudes).        |
| Measure      | **Projection** to the \(Z\) axis (collapse to \(|0\rangle\) or \(|1\rangle\)). |

> Tip: Using inline math \(\,|0\rangle\,\) inside tables avoids breaking the pipe `|` delimiters.

---

## 🧪 Minimal Working Code (Qiskit Runtime)

```python
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=1)

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

sampler = Sampler(mode=backend)
job = sampler.run([qc], shots=2000)
counts = job.result()[0].join_data().get_counts()

print(counts)
plt.bar(list(counts.keys()), list(counts.values()))
plt.title(f"Quantum Coin Flip on {backend.name}")
plt.xlabel("Outcome"); plt.ylabel("Counts")
plt.show()
```

---

## ✅ Rendering Notes (GitHub Math)

- Use `$$ ... $$` for **block** math and `\(...\)` for **inline** math.  
- Inside **tables and headings**, prefer inline forms like `\(|0\rangle\)` to avoid breaking Markdown pipes `|`.  
- Avoid mixing code fences and math for the same formula (pick one).

---

## 📈 Expected Outcome

Roughly equal counts for `0` and `1` (hardware may show small bias due to noise/readout):

```
{'0': ~1000, '1': ~1000}   # for 2000 shots
```

---

## 🧩 Concepts Recap

- **Superposition:** amplitudes over \(|0\rangle\) and \(|1\rangle\).  
- **Born rule:** probability = amplitude magnitude squared.  
- **Collapse:** measurement projects the state to a basis vector.  
- **Bloch sphere:** geometric picture of single‑qubit states.

---

Happy quantum flipping! ⚛️
