
# Quantum Coin Flip — Friendly Physics Walkthrough (No Code)

This project demonstrates a **quantum coin flip** performed on a real IBM Quantum computer.

Unlike a classical coin, which is always either heads or tails (even while spinning in the air),  
a **quantum coin** can exist in a combination of both possibilities *at the same time* until measured.

This experiment showcases the deepest ideas in quantum mechanics:

> A quantum state can exist in multiple possibilities simultaneously,  
> and **measurement forces reality to choose**.

---

## 🌟 What Happens in a Quantum Coin Flip?

We use a single quantum bit — a **qubit** — and perform three steps:

1. Start in the state `|0⟩`  
2. Apply a Hadamard gate `H` to create a **superposition**  
3. Measure the qubit → it collapses to `0` or `1` with equal probability

This gives us **true quantum randomness**, not a simulation or pseudo‑randomness.

---

## 🔬 The Core Quantum Transformation

Text form:

```
|0> --H--> (|0> + |1>) / √2 --measure--> {0, 1}
```

Mathematical form:

$$
|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

Meaning:

- Start in definite state `|0⟩`
- Hadamard places the qubit into **equal superposition**
- Measurement collapses it to `0` or `1`, each with 50% probability

---

## 🎓 Understanding the Physics

### ✅ 1. Superposition

Classically, a bit is either 0 or 1.  
A qubit can be both:

$$
\alpha |0\rangle + \beta |1\rangle
$$

For a fair quantum coin:

$$
\alpha = \beta = \frac{1}{\sqrt{2}}
$$

So:

$$
|\psi\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

The qubit is not “undecided” — it is **genuinely in both states at once**.

---

### ✅ 2. Born Rule & Collapse

When we measure, the wavefunction **collapses** to a definite value:

$$
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
\longrightarrow
\begin{cases}
|0\rangle & \text{with probability } \frac{1}{2} \\\\
|1\rangle & \text{with probability } \frac{1}{2}
\end{cases}
$$

Probability comes from the squared amplitude:

$$
\left| \frac{1}{\sqrt{2}} \right|^2 = \frac{1}{2}
$$

> This randomness is **fundamental**, not mechanical or chaotic.  
> Nature genuinely makes a choice at measurement time.

---

### ✅ 3. Bloch Sphere Picture

The Bloch sphere is a 3D representation of a qubit.

| Stage | Bloch Sphere Meaning |
|-------|----------------------|
| Start | At the **north pole** (`|0⟩`) |
| After H | On the **equator** (equal mix of `|0⟩` and `|1⟩`) |
| Measurement | Collapse to **north** (`|0⟩`) or **south** (`|1⟩`) pole |

This equator state is what makes the qubit behave like a **perfectly fair coin**.

---

## 🧠 Why This Is Beautiful

With a single qubit and one gate, we capture the heart of quantum mechanics:

- **Superposition** — multiple possibilities at once  
- **Born rule** — probability from amplitudes  
- **Wavefunction collapse** — observation creates a definite outcome  
- **Quantum randomness** — real unpredictability from physics itself  

Classical randomness is a trick; quantum randomness is **reality unfolding**.

In this simple experiment, you are watching **the universe roll its own dice**.

---

## ✨ Final Thought

A classical coin flips in *space*.  
A quantum coin flips in the **space of possibilities**.

This is why quantum computing is not just faster — it is **fundamentally different**.

Welcome to quantum physics. ⚛️🌈  
