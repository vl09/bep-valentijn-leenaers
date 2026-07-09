# Theory

## The undamped mass-spring oscillator

Consider a mass $m$ attached to a spring with stiffness $k$. When the displacement $x$ from equilibrium is small, Hooke's law gives a restoring force $F = -kx$. Then Newton's second law can be used to yield the equation of motion

$$
m\ddot{x} = - kx
$$ (eq-undamped-eom)

which describes a simple harmonic oscillator. The general solution reads

$$
x(t) = A\cos(\omega_0 t + \varphi),
$$ (eq-undamped-solution)

where $A$ is the oscillation amplitude, $\varphi$ is a phase set by the initial conditions, and

$$
\omega_0 = \sqrt{\frac{k}{m}}
$$ (eq-natural-frequency)

is the natural angular frequency. Or otherwise, $f_0 = \frac{\omega_0}{2\pi}$. 

When the mass hangs from a vertical spring, its weight stretches the spring until the upward spring force balances gravity. Let $\Delta L$ denote how much longer the spring is at this equilibrium position than when it is unloaded. Force balance then gives $k\Delta L = mg$, where $g$ is the gravitational acceleration. Then the spring constant can be obtained using

$$
k = \frac{mg}{\Delta L}.
$$ (eq-static-stiffness)

Measuring $\Delta L$ therefore provides an independent estimate of $k$, and equivalently 

$$
f_0 = \frac{1}{2\pi}\sqrt{\frac{g}{\Delta L}}
$$.
