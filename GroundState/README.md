Even though the optimization loop is classical, what happens inside each energy evaluation is deeply quantum:

When you prepare ∣ψ(θ,φ)⟩, your qubits are in a coherent combination of all possible electron configurations simultaneously.

For H₂, these configurations correspond roughly to:

- |00⟩ = both electrons on nucleus A,

- |11⟩ = both on nucleus B,

- |01⟩ and |10⟩ = one electron on each, with different spin orientations.

The Hamiltonian’s Pauli terms (like XX, YY, ZZ) act on those superpositions.
Each measurement collapses the state to one of those configurations, but by repeating many times, you infer how those amplitudes interfere — giving you the expectation value of the molecule’s energy.

So the “quantum advantage” here is that the system naturally encodes and processes all electron configurations in parallel amplitudes — something a classical computer must explicitly enumerate or approximate.



# 🧪 Quantum Hydrogen: Finding the Ground State of H₂ on a Real IBM QPU

This project demonstrates a **hardware-based Variational Quantum Eigensolver (VQE)** that estimates the **ground-state energy** of the hydrogen molecule (H₂) using **real IBM Quantum hardware** (the free tier).  

It’s a compact, pedagogical example of how quantum computers use **superposition**, **interference**, and **measurement statistics** to reproduce the **stability of molecular bonds** — the same physics that holds atoms together in nature.

---

## ⚛️ What This Notebook Does

1. **Connects to a real IBM QPU**  
   The notebook automatically picks a small, operational backend (e.g. `ibm_oslo` or `ibm_torino`) using `SamplerV2` in direct mode — no simulator is used.

2. **Builds a quantum model of H₂**  
   The two-qubit Hamiltonian:
   \[
   H = c_0 I + c_1 ZI + c_2 IZ + c_3 ZZ + c_4 XX + c_5 YY
   \]
   represents the total energy of the two-electron hydrogen molecule in a minimal STO-3G basis.

3. **Prepares a parameterized quantum state**
   A two-parameter ansatz creates a superposition of the four possible electron configurations:

   \[
   |\psi(\theta,\phi)\rangle = a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle
   \]

   Each choice of angles \((\theta, \phi)\) defines a different *trial wavefunction*.

4. **Measures the energy on the real device**  
   The circuit is transpiled to the backend’s **native gate set (ISA)**, run multiple times, and the expectation values ⟨ZZ⟩, ⟨XX⟩, ⟨YY⟩ … are reconstructed from raw counts.

5. **Classically tunes parameters**  
   A small classical optimizer iteratively adjusts (θ, φ) to minimize the measured energy — the hybrid **quantum-classical loop** known as VQE.

6. **Finds the ground state**  
   The lowest measured average energy corresponds to the **molecular ground-state energy**, i.e. the most stable electronic configuration that H₂ can adopt.

---

## 🧠 Quantum-Mechanical Insight

### Superposition and Amplitudes
The two qubits simultaneously represent all possible electron configurations (00, 01, 10, 11).  
Their quantum amplitudes \(a,b,c,d\) encode how much each configuration contributes to the total wavefunction.

### Measurement and Collapse
Each measurement *collapses* the superposition randomly into one of those basis states.  
But because the amplitudes aren’t equal, some outcomes appear more often than others.  
Repeating many times reveals a **non-uniform probability distribution** — the statistical fingerprint of the wavefunction.

### Interference and Energy
The relative **phases** between amplitudes determine how contributions from different configurations interfere.  
By tuning (θ, φ), the interference pattern is adjusted until destructive interference cancels high-energy components and constructive interference reinforces the low-energy bonding configuration.

### Variational Principle
The variational theorem guarantees:
\[
E(\theta,\phi) = \langle \psi(\theta,\phi) | \hat{H} | \psi(\theta,\phi) \rangle \ge E_0
\]
so the measured energy can only approach — never fall below — the true ground-state energy \(E_0\).

At the optimal parameters, the **average of many collapses** equals the **lowest possible energy** that your circuit can represent.

---

## 🔬 Conceptual Summary

| Concept | In a real molecule | On the quantum computer |
|----------|--------------------|--------------------------|
| Ground state | Electrons dynamically relax to the lowest energy | Qubits are *programmed* into the mathematical form of that state |
| Collapse | Not relevant (molecule stays in its orbital) | Random projection of the wavefunction during measurement |
| Stability | Achieved through energy dissipation | Achieved through parameter tuning that minimizes average energy |
| Energy minimum | True physical equilibrium | Statistical expectation from thousands of quantum measurements |

---

## 🧰 How to Run

1. Open the notebook in Google Colab.  
2. Install dependencies:  
   ```bash
   !pip install qiskit qiskit-ibm-runtime matplotlib

