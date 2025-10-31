# ⚛️ Quantum Random Seed Generator with IBM Qiskit Runtime

This project uses **IBM Quantum’s real superconducting hardware** to generate truly random numbers by exploiting **quantum superposition and measurement collapse**. These quantum-derived bits are used to seed Python’s NumPy random number generator.

Unlike classical pseudo-random seeds, this method harnesses **true entropy** directly from quantum mechanics.

---

## Open in Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/jahaltom/Quantum-Computing/blob/main/QRNG/IBM/IBM_QRNG.ipynb
)


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



After applying H to **16 qubits**, the entire system is in a superposition of **all possible 16-bit strings**:

|ψ⟩ = (1/√65536) × (|0000000000000000⟩ + ... + |1111111111111111⟩)



This is a uniform superposition over `2^16 = 65,536` basis states.

---

### 2. Measurement and Collapse

When you measure a quantum state, it **collapses** to a single classical result. The probability of each result is determined by the **Born rule**:

P(result) = |⟨result|ψ⟩|²



This is **true randomness** — not pseudorandomness, not chaos, not thermal noise — but a **fundamental feature of quantum mechanics**.

---

### 3. Real Quantum Hardware

This randomness comes from a real quantum processor, like IBM’s `ibm_sherbrooke`, which has 127 superconducting qubits. No simulator is used.

You are literally pulling entropy from the quantum vacuum — the truest source of randomness we know.

---
## Quantum circuit for generating a 16-bit quantum random number seed
```
         ┌───┐ ░ ┌─┐                                             
    q_0: ┤ H ├─░─┤M├─────────────────────────────────────────────
         ├───┤ ░ └╥┘┌─┐                                          
    q_1: ┤ H ├─░──╫─┤M├──────────────────────────────────────────
         ├───┤ ░  ║ └╥┘┌─┐                                       
    q_2: ┤ H ├─░──╫──╫─┤M├───────────────────────────────────────
         ├───┤ ░  ║  ║ └╥┘┌─┐                                    
    q_3: ┤ H ├─░──╫──╫──╫─┤M├────────────────────────────────────
         ├───┤ ░  ║  ║  ║ └╥┘┌─┐                                 
    q_4: ┤ H ├─░──╫──╫──╫──╫─┤M├─────────────────────────────────
         ├───┤ ░  ║  ║  ║  ║ └╥┘┌─┐                              
    q_5: ┤ H ├─░──╫──╫──╫──╫──╫─┤M├──────────────────────────────
         ├───┤ ░  ║  ║  ║  ║  ║ └╥┘┌─┐                           
    q_6: ┤ H ├─░──╫──╫──╫──╫──╫──╫─┤M├───────────────────────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║ └╥┘┌─┐                        
    q_7: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫─┤M├────────────────────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐                     
    q_8: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫─┤M├─────────────────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐                  
    q_9: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├──────────────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐               
   q_10: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├───────────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐            
   q_11: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├────────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐         
   q_12: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├─────────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐      
   q_13: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├──────
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐   
   q_14: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├───
         ├───┤ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐
   q_15: ┤ H ├─░──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫──╫─┤M├
         └───┘ ░  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ └╥┘
meas: 16/═════════╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩═
                  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15

```
## 📦 Requirements

- Python 3.8+
- `qiskit`
- `qiskit-ibm-runtime`
- An IBM Quantum account and API token

Install dependencies:

```
pip install qiskit qiskit-ibm-runtime qiskit-aer
```
## 🔐 Setup
Log in to (https://quantum.ibm.com) and copy your API token.

Save it using:

```
from qiskit_ibm_runtime import QiskitRuntimeService

# Replace 'MY_TOKEN' with your actual token from the IBM Quantum dashboard
QiskitRuntimeService.save_account(channel="ibm_quantum", token="MY_TOKEN", overwrite=True)
```
## 🧬 Usage
Run the script:

```
python quantum_seed.py
```
Example output:

```
Using backend: ibm_sherbrooke
Quantum bits: [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0]
Quantum seed: 39620
```
This seed is now available for all NumPy random operations:

```
np.random.seed(quantum_seed)
```
## 💡 Why Use Quantum Seeds?
🎲 Randomized model initializations

🧬 Monte Carlo simulations

🔐 Cryptographic or lottery applications

📈 Reproducible but high-entropy ML pipelines

🧪 Experimental protocols in computational science

## 📚 References

- [Qiskit Runtime Migration Guide](https://docs.quantum.ibm.com/migration-guides/qiskit-runtime)
- [Qiskit Sampler API Documentation](https://docs.quantum.ibm.com/api/qiskit-ibm-runtime/sampler)
- [Born Rule – Wikipedia](https://en.wikipedia.org/wiki/Born_rule)
- [IBM Quantum Hardware Overview](https://quantum-computing.ibm.com/)



⚠️ Disclaimer
This script depends on IBM Quantum device availability and internet/cloud access. Ensure your account is properly configured before use.
