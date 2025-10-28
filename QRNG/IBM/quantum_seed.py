from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
import numpy as np

# Initialize the Qiskit Runtime service
service = QiskitRuntimeService(channel="ibm_cloud")

# Select an operational backend with at least 16 qubits
backends = service.backends(
    filters=lambda b: not b.configuration().simulator and b.status().operational and b.configuration().n_qubits >= 16
)
backend = sorted(backends, key=lambda b: b.status().pending_jobs)[0]
print(f"Using backend: {backend.name}")

def get_real_quantum_random_bits(num_bits=16):
    # Create a quantum circuit with Hadamard gates and measurements
    qc = QuantumCircuit(num_bits)
    qc.h(range(num_bits))
    qc.measure_all()

    # Transpile the circuit for the selected backend
    transpiled_circuit = transpile(qc, backend=backend, optimization_level=0)

    # Initialize the Sampler with the selected backend
    sampler = Sampler(mode=backend)

    # Run the circuit using the Sampler
    job = sampler.run([transpiled_circuit])
    result = job.result()

    # Retrieve counts from the result
    counts = result[0].data.meas.get_counts()

    # Get the most frequent bitstring
    bitstring = max(counts, key=counts.get)
    return [int(bit) for bit in bitstring.zfill(num_bits)]

# Generate quantum random bits and seed NumPy's RNG
quantum_bits = get_real_quantum_random_bits(16)
quantum_seed = int("".join(map(str, quantum_bits)), 2)

print("Quantum bits:", quantum_bits)
print("Quantum seed:", quantum_seed)

np.random.seed(quantum_seed)
