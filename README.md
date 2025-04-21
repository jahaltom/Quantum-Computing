# Quantum Random Seed Generator using IBM Qiskit Runtime

This project uses **IBM's real quantum computers** to generate **true quantum random numbers**, which are then used to seed NumPy's random number generator. Unlike classical pseudo-random generators, this method relies on the **fundamental indeterminacy of quantum measurement** to produce entropy.

---

## 🚀 What This Script Does

- Connects to the IBM Quantum platform using `QiskitRuntimeService`.
- Selects the least-busy real backend with at least 16 qubits.
- Builds a 16-qubit quantum circuit that places each qubit in superposition.
- Measures all qubits, collapsing the system to a truly random 16-bit binary string.
- Converts that binary string into an integer seed.
- Uses the seed to initialize `numpy.random`.

You can then use NumPy in your simulations, machine learning models, or cryptographic experiments — now seeded with **genuine quantum entropy**.

---

## 🧠 Quantum Mechanics Breakdown

At the core of this script is a simple but powerful quantum phenomenon:

### 1. **Hadamard Gates: Superposition**

Each qubit starts in the ground state \(|0\rangle\). A **Hadamard gate** is applied:

<pre> ```
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
``` </pre>

This places the qubit into an **equal superposition** of 0 and 1. For 16 qubits, the full system state becomes:

\[
|\psi\rangle = \frac{1}{\sqrt{2^{16}}} \sum_{i=0}^{65535} |i\rangle
\]

This represents **all 65,536 possible 16-bit binary strings** simultaneously.

---

### 2. **Measurement: True Randomness**

When you measure the qubits, the wavefunction **collapses** to a single classical bitstring — for example, `0101011010110101`.

This collapse is **fundamentally probabilistic**, governed by the **Born rule**:

\[
P(\text{bitstring}) = |\langle \text{bitstring}|\psi\rangle|^2
\]

This is not due to noise, chaos, or ignorance — it’s pure quantum indeterminacy.

---

### 3. **Hardware Entropy Source**

You are running the circuit on a real superconducting quantum device (like `ibm_sherbrooke`), not a simulator. This guarantees:
- Unpredictability from the environment.
- No pseudorandom number generation.
- Direct sampling from a quantum system.

---

## 🧪 Example Output

