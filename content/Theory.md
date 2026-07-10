# Theory
## The undamped mass-spring oscillator

Consider a mass $m$ attached to a spring with stiffness $k$. When the displacement $x$ from equilibrium is small, Hooke's law gives a restoring force $F = -kx$. Then Newton's second law can be used to yield the equation of motion

$$
m\ddot{x} = - kx
$$ (eq-undamped-eom)

which describes a simple harmonic oscillator. The general solution reads

$$
x(t) = A\cos(\omega_0 t + \varphi),
$$ 
where $A$ is the oscillation amplitude, $\varphi$ is a phase set by the initial conditions, and

$$
\omega_0 = \sqrt{\frac{k}{m}}
$$ (eq-natural-frequency)

is the natural angular frequency. Or otherwise, $f_0 = \frac{\omega_0}{2\pi}$. 

When the mass hangs from a vertical spring, its weight stretches the spring until the upward spring force balances gravity. Let $\Delta L$ denote how much longer the spring is at this equilibrium position than when it is unloaded. Force balance then gives $k\Delta L = mg$, where $g$ is the gravitational acceleration. Then the spring constant can be obtained using

$$
k = \frac{mg}{\Delta L}.
$$ 

Measuring $\Delta L$ for a specific mass $m$ therefore provides an independent estimate of $k$, and equivalently 

$$
f_0 = \frac{1}{2\pi}\sqrt{\frac{g}{\Delta L}}
$$.

This ideal scenario described above does not account for friction or other mechanical energy losses. In real life, however, energy losses are adamant and need to be accounted for. 

## Damped motion
### Equation of motion
To describe how the oscillation decays, a dissipative force proportional to velocity is added to the model. This viscous damping force points opposite to the motion and reads

$$
F_d = -c\dot{x},
$$ 

with damping coefficient $c$ in $[Ns/m]$. Combining the spring and damping forces with Newton's second law gives

$$
m\ddot{x} + c\dot{x} + kx = 0.
$$ (eq-damped-eom)

It is convenient to write this in terms of the mass-normalised damping rate

$$
\Gamma_m = \frac{c}{m},
$$ (eq-gamma-definition)

where $\Gamma_m$ has units of $Hz$. Substituting [](#eq-gamma-definition) into [](#eq-damped-eom) yields

$$
\ddot{x} + \Gamma_m \dot{x} + \omega_0^2 x = 0.
$$ (eq-damped-normalised)

For the lightly damped regime relevant to the cryostat structures ($\Gamma_m \leq 2\omega_0$), the solution is an exponentially decaying sinusoid:

$$
x(t) = Ae^{-\Gamma_m t/2}\cos(\tilde{\omega}_0 t + \varphi),
$$ (eq-ringdown-solution)

with damped angular frequency

$$
\tilde{\omega}_0 = \omega_0 \sqrt{1 - \left(\frac{\Gamma_m}{2\omega_0}\right)^2}.
$$ (eq-damped-frequency)

When $\Gamma_m \leq 2\omega_0$, the oscillation frequency remains close to $\omega_0$ and the envelope $A(t) = A_0 e^{-\Gamma_m t/2}$ decays exponentially in time.
