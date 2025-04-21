# ⚛️ Quantum Random Seed Generator with IBM Qiskit Runtime

This project uses **IBM Quantum’s real superconducting hardware** to generate truly random numbers by exploiting **quantum superposition and measurement collapse**. These quantum-derived bits are used to seed Python’s NumPy random number generator.

Unlike classical pseudo-random seeds, this method harnesses **true entropy** directly from quantum mechanics.

---

## 🚀 What the Script Does

- Connects to IBM’s real quantum devices via `QiskitRuntimeService`
- Chooses a backend with at least 16 available qubits
- Builds a 16-qubit quantum circuit with Hadamard gates
- Measures the quantum state to get a single 16-bit random outcome
- Converts that into a base-10 seed
- Sets NumPy’s RNG with this seed

You can now use `np.random` in any Python application with quantum randomness at its core.

---

## 🧠 Quantum Mechanics Breakdown

### 1. Hadamard Gates and Superposition

Each qubit starts in the classical state `|0⟩`. Applying a **Hadamard gate (H)** transforms it into a quantum superposition:

H|0⟩ = (1/√2)(|0⟩ + |1⟩)
