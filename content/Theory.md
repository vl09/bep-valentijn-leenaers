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

## Damped motion and Ringdown
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

For the lightly damped regime relevant to the cryostat structures ($\Gamma_m \lt 2\omega_0$), the solution is an exponentially decaying sinusoid:

$$
x(t) = Ae^{-\Gamma_m t/2}\cos(\tilde{\omega}_0 t + \varphi),
$$ (eq-ringdown-solution)

with damped angular frequency

$$
\tilde{\omega}_0 = \omega_0 \sqrt{1 - \left(\frac{\Gamma_m}{2\omega_0}\right)^2}.
$$ (eq-damped-frequency)

When $\Gamma_m \lt 2\omega_0$, the oscillation frequency remains close to $\omega_0$ and the envelope $A(t) = A_0 e^{-\Gamma_m t/2}$ decays exponentially in time.

### Ringdown protocol

A ringdown measurement probes the free evolution described by [](#eq-ringdown-solution). The spring-mass system is displaced from equilibrium, released, and the acceleration or displacement is recorded as the motion decays in the absence of an external drive. This protocol was used by Wilkinson[@wilkinson2025] to characterise the tuned mass damper prototypes, and the same principle is applied in the benchtop validation of the accelerometer measurement chain described later in this thesis.

The quantity extracted from a ringdown is $\Gamma_m$: the rate at which the oscillation envelope loses amplitude. In the time domain, an estimate of $\Gamma_m$ is obtained by fitting the envelope to

$$
A(t) = A_0 e^{-\Gamma_m t/2}.
$$ (eq-envelope-fit)

The envelope can be constructed from band-pass filtered acceleration data by means of the analytic signal and Hilbert transform, which removes the rapid oscillation at $f_0$ and leaves a smooth curve tracing $|A(t)|$. A linear fit to $\ln A(t)$ then gives slope $-\Gamma_m/2$.

Intuitively, a smaller $\Gamma_m$ implies a slower decay and a sharper resonance, whereas a larger $\Gamma_m$ implies faster energy dissipation and a broader spectral peak. Prior work on the cryogenic tuned mass damper reported baseline values $\Gamma_m \approx 4$–$5\,\mathrm{mHz}$ for a similar single mass-spring reference configuration, increasing when absorber and eddy-current damping elements were added[@wilkinson2025].

## Frequency-domain response and linewidth
### Driven oscillator and transfer function

In the operating cryostat, mechanical structures are continuously driven by periodic helium-pump motion near $1.4\,\mathrm{Hz}$ rather than ringing down freely[@maisonobe2018]. For a single mode driven harmonically at angular frequency $\omega$, the steady-state equation of motion reads

$$
m\ddot{x} + c\dot{x} + kx = F_0 \cos(\omega t).
$$ (eq-driven-eom)

The resulting displacement amplitude as a function of drive frequency is[@fowles2005]

$$
X(\omega) = \frac{F_0}{k - m\omega^2 + ic\omega}.
$$ (eq-transfer-function)

The magnitude $|X(\omega)|$ exhibits a maximum near $\omega = \omega_0$. For small damping, this resonance appears as a narrow peak in spectra derived from measured acceleration data.

### Power spectral density and the Lorentzian peak

For a stationary random acceleration signal $a(t)$, the one-sided power spectral density $S_{aa}(f)$ describes how mean-square acceleration is distributed over frequency. The variance follows from integrating over all frequencies,

$$
\sigma_a^2 = \int_0^\infty S_{aa}(f)\,\mathrm{d}f.
$$ (eq-variance-psd)

A lightly damped ringdown of a single mechanical mode produces a dominant peak in $S_{aa}(f)$ centred at $f_0$. Near resonance the PSD can be approximated by a Lorentzian,

$$
S_{aa}(f) \approx \frac{A}{(f - f_0)^2 + (\Delta f/2)^2},
$$ (eq-lorentzian)

where $A$ is a peak amplitude set by the excitation level and $\Delta f$ is the full width at half maximum (FWHM) in $Hz$.

For the normalised equation of motion [](#eq-damped-normalised), the FWHM in cyclic frequency is related to the mass-normalised damping rate by

$$
\Gamma_m = 2\pi\,\Delta f.
$$ (eq-gamma-fwhm)

This is the same $\Gamma_m$ that governs the exponential envelope in [](#eq-ringdown-solution). An equivalent statement is that the quality factor

$$
Q = \frac{f_0}{\Delta f} = \frac{\omega_0}{\Gamma_m}
$$ (eq-quality-factor)

measures how many radians of oscillation occur before the energy decays appreciably. Large $Q$ (small $\Gamma_m$) corresponds to a tall, narrow resonance peak; small $Q$ corresponds to a broad, low peak.

The Amplitude Spectral Density (ASD), defined as $\sqrt{S_{aa}(f)}$, is often used when comparing vibration measurements to sensor noise floors quoted by manufacturers. Both representations carry the same resonance frequency $f_0$ and linewidth $\Delta f$.

## Relating time-domain and frequency-domain estimates of $\Gamma_m$

The damping rate $\Gamma_m$ can therefore be extracted in two independent ways from the same ringdown recording. In the time domain, $\Gamma_m$ follows from fitting the exponential envelope in [](#eq-envelope-fit). In the frequency domain, the resonance peak in the PSD is fitted with [](#eq-lorentzian), and $\Gamma_m$ follows from [](#eq-gamma-fwhm) using the fitted FWHM.

For a linear, time-invariant oscillator and consistent processing (band-pass filtering around $f_0$, sufficient data time-wise, and removal of transients from manual excitation), the two estimates should agree within experimental uncertainty. Wilkinson[@wilkinson2025] reported agreement to within roughly $23\%$ between ringdown and PSD linewidth fits for the single mass-spring reference system. Differences can arise from finite record length, non-ideal band-pass filtering, sensor noise near the ADXL354 noise floor, and weak nonlinearities such as amplitude-dependent friction. 

In this thesis, the ringdown analysis applies will be analyzing the results of the two previously described methos. First, the Hilbert envelope yields $\Gamma_m$ from the decaying time series. Second, a Lorentzian fit to the periodogram near $f_0 \approx 0.9\,\mathrm{Hz}$ yields $\Gamma_m$ from the spectral linewidth. Agreement between the two values validates the measurement chain before it is used to characterise vibrations on the pulse tube, the vibration isolation platform, and the tuned mass damper inside the Bluefors cryostat.
