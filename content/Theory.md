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

is the natural angular frequency. Or equivalently, $f_0 = \frac{\omega_0}{2\pi}$. 

When the mass hangs from a vertical spring, its weight stretches the spring until the upward spring force balances gravity. Let $\Delta L$ denote how much longer the spring is at this equilibrium position than when it is unloaded. Force balance then gives $k\Delta L = mg$, where $g$ is the gravitational acceleration. Then the spring constant can be obtained using

$$
k = \frac{mg}{\Delta L}.
$$ 

Measuring $\Delta L$ for a specific mass $m$ therefore provides an independent estimate of $k$, and equivalently 

$$
f_0 = \frac{1}{2\pi}\sqrt{\frac{g}{\Delta L}}
$$.

For simple harmonic motion at angular frequency $\omega_0$ with peak displacement amplitude $A$, the peak acceleration is $a_{\mathrm{peak}} = \omega_0^2 A$. In units of $g$,

$$
\frac{a_{\mathrm{peak}}}{g} = \frac{(2\pi f_0)^2 A}{g},
$$ (eq-shm-peak-accel)

where $A$ is in metres. This relation is used in the ringdown validation described in [](#methods) to compare the accelerometer trace against an independent kinematic estimate from video and a ruler.

Real oscillators dissipate energy. The following section introduces viscous damping and the ringdown envelope used as a sanity check on the measurement chain.

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

For the lightly damped regime ($\Gamma_m \ll \omega_0$), the solution is an exponentially decaying sinusoid:

$$
x(t) = Ae^{-\Gamma_m t/2}\cos(\tilde{\omega}_0 t + \varphi),
$$ (eq-ringdown-solution)

with damped angular frequency $\tilde{\omega}_0 = \omega_0 \sqrt{1 - (\Gamma_m/2\omega_0)^2}$. The envelope $A(t) = A_0 e^{-\Gamma_m t/2}$ decays exponentially in time. The full derivation of [](#eq-ringdown-solution) can be found in [](#appendix-derivations).

### Ringdown as a validation measurement
A ringdown measurement probes the free evolution described by [](#eq-ringdown-solution). The spring-mass system is displaced from equilibrium, released, and the acceleration is recorded as the motion decays in the absence of an external drive. Wilkinson[@wilkinson2025] applied this protocol to characterise cryogenic tuned mass damper prototypes; in the present thesis the same principle is used only as a benchtop sanity check on the accelerometer measurement chain.

The quantity of interest for validation is the ringdown time scale, obtained by fitting the amplitude envelope to

$$
A(t) = A_0 e^{-\Gamma_m t/2}.
$$ (eq-envelope-fit)

Intuitively, a smaller $\Gamma_m$ implies a slower decay, whereas a larger $\Gamma_m$ implies faster energy dissipation. The benchtop recording lasted only ten minutes, which is sufficient for a sanity check that the ringdown protocol and accelerometer chain work as intended. The oscillator continues to ring down beyond this window, but the full decay is not analysed here because quantitative ringdown characterisation lies outside the scope of this thesis. Agreement between the fitted envelope over the recorded interval, the oscillation frequency estimated from the time trace, and the kinematic peak acceleration from [](#eq-shm-peak-accel) is sufficient to confirm that the calibrated chain reproduces dynamic accelerations before it is applied to cryostat-mounted recordings.
validates the measurement chain before it is used to characterise vibrations on the pulse tube, the vibration isolation platform, and the tuned mass damper inside the Bluefors cryostat.


## Spectral analysis and periodic forcing
### Power spectral density and amplitude spectral density
Cryostat vibration measurements are analysed in the frequency domain. For a stationary acceleration signal $a(t)$, the one-sided power spectral density $S_{aa}(f)$ describes how mean-square acceleration is distributed over frequency. The variance follows from integrating over all frequencies,

$$
\sigma_a^2 = \int_0^\infty S_{aa}(f)\,\mathrm{d}f.
$$ (eq-variance-psd)

The Amplitude Spectral Density (ASD) is defined as

$$
\mathrm{ASD}(f) = \sqrt{S_{aa}(f)}.
$$

Manufacturers often quote accelerometer noise floors in ASD units, typically $\mu\mathrm{g}/\sqrt{\mathrm{Hz}}$, which allows direct comparison with measured spectra.

Spectra in this thesis are estimated with Welch's method, which averages periodograms computed on overlapping time segments. The segment length sets a trade-off between frequency resolution and the smearing of narrow-band lines. A long segment resolves closely spaced peaks but leaves a sharp periodic drive, such as the $\sim 1.5\,\mathrm{Hz}$ cryocooler fundamental, visible as a comb of lines in the spectrum. A shorter segment broadens those lines and exposes the broader mechanical structure underneath. Both views are useful, and the processing choice is stated alongside each figure in [](#results).

### Driven oscillator and harmonic content
In the operating cryostat, mechanical structures are continuously driven by the periodic cryocooler cycle rather than ringing down freely[@maisonobe2018]. For a single mode driven harmonically at angular frequency $\omega$, the steady-state equation of motion reads

$$
m\ddot{x} + c\dot{x} + kx = F_0 \cos(\omega t).
$$ (eq-driven-eom)

The resulting displacement amplitude as a function of drive frequency is[@fowles2005]

$$
X(\omega) = \frac{F_0}{k - m\omega^2 + ic\omega}.
$$ (eq-transfer-function)

The magnitude $|X(\omega)|$ exhibits a maximum near $\omega = \omega_0$. When many modes are present, each contributes a peak in $S_{aa}(f)$ at its resonance frequency. The peak width reflects damping: for small damping the full width at half maximum $\Delta f$ is related to $\Gamma_m$ by $\Gamma_m = 2\pi\,\Delta f$.

The cryocooler drive is not a pure sinusoid. A periodic displacement or force that repeats once per cycle but has a pulse-like waveform contains energy at the fundamental frequency and at integer harmonics. A spectrum of cryostat vibrations therefore shows a comb of lines spaced by the drive frequency, together with additional peaks from structural resonances excited by that drive. Harmonics can extend to frequencies well above the fundamental, which is why spectra are examined over ranges from a few hertz up to the accelerometer bandwidth.
