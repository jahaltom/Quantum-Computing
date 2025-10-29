Even though the optimization loop is classical, what happens inside each energy evaluation is deeply quantum:

When you prepare ∣ψ(θ,φ)⟩, your qubits are in a coherent combination of all possible electron configurations simultaneously.

For H₂, these configurations correspond roughly to:

- |00⟩ = both electrons on nucleus A,

- |11⟩ = both on nucleus B,

- |01⟩ and |10⟩ = one electron on each, with different spin orientations.

The Hamiltonian’s Pauli terms (like XX, YY, ZZ) act on those superpositions.
Each measurement collapses the state to one of those configurations, but by repeating many times, you infer how those amplitudes interfere — giving you the expectation value of the molecule’s energy.

So the “quantum advantage” here is that the system naturally encodes and processes all electron configurations in parallel amplitudes — something a classical computer must explicitly enumerate or approximate.
