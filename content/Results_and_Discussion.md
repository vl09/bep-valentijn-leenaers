(results)=
# Results & Discussion
## Accelerometer validation
(results-static-flip-test)=
### Static flip test
The raw $z$-channel voltage from the static gravity-flip calibration in [](#methods-static-flip-test) is shown in [](#fig-flip-voltage).

```{figure} figures/Flip_voltage.png
:label: fig-flip-voltage
:alt: Raw z-axis voltage during a 180 degree gravity flip

Raw $z$-channel scope voltage during the static flip test. The sensor rests at $+1\ \mathrm{g}$ for the first $\sim 6\ \mathrm{s}$, is flipped manually, and then rests at $-1\ \mathrm{g}$. Transients during the flip are excluded from the calibration windows.
```

In the upright plateau ($4$–$5\ \mathrm{s}$), the mean voltage is $\bar{V}_{+1\ \mathrm{g}} = 1.289\ \mathrm{V}$. In the inverted plateau ($9$–$10\ \mathrm{s}$), $\bar{V}_{-1\ \mathrm{g}} = 0.505\ \mathrm{V}$. Both plateaus are steady over their $1\ \mathrm{s}$ windows and bracket a $2\ \mathrm{g}$ span, as expected for $\pm 1\ \mathrm{g}$ orientations. From [](#eq-flip-sensitivity), the sensitivity is $S = 0.392\ \mathrm{V/g}$ ($392\ \mathrm{mV/g}$). The estimated zero-$g$ offset is $\bar{V}_0 = 0.897\ \mathrm{V}$, close to the nominal $\mathrm{V_{1P8ANA}}/2 = 0.9\ \mathrm{V}$. This value is used as the fixed offset in all later voltage-to-$g$ conversions. For the $\pm 2\ \mathrm{g}$ range, the datasheet quotes $368$–$432\ \mathrm{mV/g}$ on all three outputs (typical $400\ \mathrm{mV/g}$)[@adxl354_datasheet]. The extracted $392\ \mathrm{mV/g}$ lies within this min–max band and within $\sim 2\%$ of the typical value. 

That deviation is small compared with the $\pm 16\%$ production spread quoted in the datasheet. Additional contributors include the single benchtop measurement (no repeatability statistics), manual handling during the flip, scope digitisation, and unit-to-unit spread: the datasheet gives $z$-axis sensitivity repeatability of $0.3\%$ and a temperature coefficient of $\pm 0.01\ \%$ per degree Celsius over $-40$ to $+125$ °C[@adxl354_datasheet], so a few degrees of laboratory temperature change cannot account for the $2\%$ offset from typical. Cross-axis coupling ($1\%$), nonlinearity ($0.1\%$ at $\pm 2\ \mathrm{g}$), and the use of one $z$-axis calibration for all three channels are further minor sources. 

For the scope of this thesis, however, which targets vibration frequencies and relative spectral structure rather than absolute $g$ metrology, these residual calibration uncertainties are acceptable: narrow-band peaks and harmonic spacing depend primarily on timing and shape, not on the few-percent difference between the extracted and nominal sensitivities.

Applying [](#eq-voltage-to-g) with the extracted $S$ and $\bar{V}_0$ converts the plateaus to $+1.0\ \mathrm{g}$ and $-1.0\ \mathrm{g}$, as required by the known $\pm 1\ \mathrm{g}$ gravity reference. The $\pm 1\ \mathrm{g}$ levels are reproduced to within the resolution set by the $1\ \mathrm{s}$ averaging windows and the datasheet sensitivity tolerance ($368$–$432\ \mathrm{mV/g}$)[@adxl354_datasheet], well inside the needs of the subsequent vibration analysis. Together, the flip test confirms that the voltage-to-$g$ conversion reproduces the known static levels and that the extracted sensitivity is consistent with the datasheet.

(results-mass-spring-ringdown)=
### Mass-spring ringdown
The second validation experiment records a benchtop mass-spring ringdown while a video camera captures the motion against a ruler, as described in [](#methods-mass-spring-ringdown). This test is a sanity check on the calibrated chain: a simple oscillator with an independently measured frequency and amplitude should produce accelerations that agree with kinematics and decay as expected for a damped mass-spring system[@wilkinson2025].

+++{"no-pdf": true}

The recording is shown in [](#vid-ringdown).

```{figure} figures/ringdown.mp4
:label: vid-ringdown
:width: 50%
:align: center

Benchtop mass-spring ringdown recorded alongside the accelerometer trace. A ruler beside the apparatus provides the displacement scale.
```

+++

From the video, ten complete oscillations occur between $t = 2.24\ \mathrm{s}$ and $t = 12.29\ \mathrm{s}$, giving a window duration $\Delta t = 10.05\ \mathrm{s}$ and

$$
f = \frac{10}{\Delta t} = 0.995\ \mathrm{Hz}.
$$

With $\omega = 2\pi f$ and displacement amplitude $A = 13.5\ \mathrm{cm} = 0.135\ \mathrm{m}$ from the ruler span described in [](#methods-mass-spring-ringdown), [](#eq-shm-peak-accel) gives a peak oscillatory acceleration of

$$
\frac{a_{\mathrm{peak}}}{g} = \frac{A\omega^2}{g} = 0.54\ \mathrm{g}.
$$

Because the $z$-axis measures gravity plus the vertical oscillation, the expected $z$-channel range is $1.0 \pm 0.54\ \mathrm{g}$, i.e. approximately $0.46\ \mathrm{g}$ to $1.54\ \mathrm{g}$.

#### Short-time wobble structure
The accelerometer trace for the first $15\ \mathrm{s}$ is shown in [](#fig-ringdown-wobble).

```{figure} figures/Ringdown_wobble_zoom.png
:label: fig-ringdown-wobble
:alt: Three-axis accelerometer ringdown trace zoomed to the first 15 seconds

Calibrated acceleration during the first $15\ \mathrm{s}$ of the ringdown. Dashed lines on $z$ mark the expected extrema from the video and ruler analysis ($0.46\ \mathrm{g}$ and $1.54\ \mathrm{g}$).
```

In this window the dominant motion is on the $z$-axis (blue). The video count in [](#methods-mass-spring-ringdown) gives ten complete oscillations between $t = 2.24\ \mathrm{s}$ and $t = 12.29\ \mathrm{s}$, consistent with $f \approx 1\ \mathrm{Hz}$ and visible in the first $15\ \mathrm{s}$ of the trace. The $z$-trace swings between extrema near $0.4\ \mathrm{g}$ and $1.5\ \mathrm{g}$, in agreement with the kinematic limits marked by the dashed lines at $0.46\ \mathrm{g}$ and $1.54\ \mathrm{g}$. Because the independently derived frequency, amplitude, and extrema all match the accelerometer readout after flip-test calibration, this comparison validates the full measurement chain from scope acquisition through [](#eq-voltage-to-g) before it is applied to the cryostat recordings.

Smaller periodic motion appears on the off-axis channels. The $x$-channel (red) oscillates about a negative offset near $-0.15\ \mathrm{g}$ with peak-to-peak wobble amplitude of order $0.1\ \mathrm{g}$. The $y$-channel (green) shows a similar wobble about a positive offset near $+0.15\ \mathrm{g}$. Each off-axis trace repeats on roughly the same $\sim 1\ \mathrm{Hz}$ timescale as the vertical motion, but the waveforms are not pure sinusoids: higher-frequency ripples are superposed on the main period. This is expected for a real benchtop spring-mass assembly, where slight misalignment and coupling introduce lateral modes alongside the intended vertical oscillation.

Even within this short window, the oscillation amplitudes evolve slowly. The $z$-peaks near $t = 0\ \mathrm{s}$ sit slightly above those near $t = 15\ \mathrm{s}$, and the $x$- and $y$-wobbles narrow in the same interval. The ringdown is therefore already visible at the scale of individual cycles, before the full recording is considered.

#### Full ringdown and exponential decay
[](#fig-ringdown-a-vs-t) shows the complete three-axis ringdown accelerometer trace over the full $600\ \mathrm{s}$ scope recording.

```{figure} figures/Ringdown_a_vs_t.png
:label: fig-ringdown-a-vs-t
:alt: Three-axis accelerometer ringdown trace over the full 600 second recording

Calibrated acceleration over the full ringdown recording ($600\ \mathrm{s}$). Oscillation envelopes decay on all three axes; the $z$-channel settles to a steady level slightly below $1\ \mathrm{g}$ because of a small mounting tilt.
```

Zooming out reveals the damping time scale. On $z$, the large $\sim 1\ \mathrm{Hz}$ oscillation decays from an initial span of roughly $0.4$–$1.5\ \mathrm{g}$ to a near-constant level by the end of the window. That final level sits slightly below $1\ \mathrm{g}$ (near $0.95\ \mathrm{g}$ in [](#fig-ringdown-envelope)), because the accelerometer on the oscillating mass was not mounted perfectly level with respect to Earth's gravitational field: a small tilt reduces the $z$-component of gravity while projecting a fraction onto $x$ and $y$. The resulting steady offsets near $-0.15\ \mathrm{g}$ on $x$ and $+0.15\ \mathrm{g}$ on $y$ are consistent with this misalignment. The $x$- and $y$-channels also show exponential decay of their wobble envelopes, from initial lateral amplitudes of order $0.1\ \mathrm{g}$ down to these bias levels. Although the off-axis motion is much smaller than the vertical component, it follows the same qualitative pattern: a damped oscillation superposed on a constant bias.

This behaviour matches the lightly damped ringdown model in [](#eq-ringdown-solution), where the envelope decays as $A_0 e^{-\Gamma_m t/2}$. To illustrate the decay, the analytic envelope from [](#eq-envelope-fit) is overlaid on the $z$-channel trace in [](#fig-ringdown-envelope) with parameters chosen by eye to follow the decaying peaks from roughly $t = 100\ \mathrm{s}$ onward.

```{figure} figures/Ringdown_envelope_fit.png
:label: fig-ringdown-envelope
:alt: z-axis ringdown with exponential envelope overlay

$z$-axis ringdown acceleration (blue) with the envelope $C \pm A_0 e^{-\Gamma_m t/2}$ overlaid (dashed). Parameters $C = 0.95\ \mathrm{g}$, $A_0 = 0.38\ \mathrm{g}$, and $\Gamma_m = 9.9\ \mathrm{mHz}$ ($\tau_A = 2/\Gamma_m \approx 200\ \mathrm{s}$) are set by eye.
```

In the first $\sim 100\ \mathrm{s}$, the oscillation peaks fall faster than the dashed envelope. This is consistent with amplitude-dependent damping on the benchtop spring: friction and air drag are stronger at the large initial displacement, so the effective decay rate is higher early on and approaches a slower rate once the motion has settled. A brief release transient when the mass is let go may contribute to the same interval. From roughly $t = 100\ \mathrm{s}$ onward, the envelope tracks the peaks well. A single exponential is therefore a qualitative guide rather than a full model of the ringdown. It is nevertheless sufficient for the validation goal: the accelerometer reproduces the frequency, amplitude, and decaying oscillation expected of a mass-spring system, rather than a stationary offset or a readout artefact.

#### Ringdown spectra
After the time-domain checks, the ringdown recording is examined in the frequency domain. [](#fig-ringdown-asd-low) shows the Welch ASD of the $z$-channel from $0$ to $5\ \mathrm{Hz}$.

```{figure} figures/Ringdown_ASD_0-5Hz_3ch.png
:label: fig-ringdown-asd-low
:alt: z-axis ringdown ASD from 0 to 5 Hz

Welch ASD of the $z$-channel ringdown ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$) from $0$ to $5\ \mathrm{Hz}$. The horizontal line marks the datasheet noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$[@adxl354_datasheet].
```

The $z$-channel shows a sharp peak near $1\ \mathrm{Hz}$, in line with the video count ($f = 0.995\ \mathrm{Hz}$) and the $\sim 1\ \mathrm{Hz}$ oscillation in [](#fig-ringdown-wobble). Additional lines appear at integer multiples of the fundamental ($2\ \mathrm{Hz}$, $3\ \mathrm{Hz}$, $4\ \mathrm{Hz}$, and higher). The peaks at even multiples ($2\ \mathrm{Hz}$, $4\ \mathrm{Hz}$, and beyond) and at $3\ \mathrm{Hz}$ stand above those at $5\ \mathrm{Hz}$, $7\ \mathrm{Hz}$, $9\ \mathrm{Hz}$, and $11\ \mathrm{Hz}$. This pattern is expected when the motion is periodic but not a pure sinusoid: a slightly asymmetric waveform about its mean (for example from the initial release transient, amplitude-dependent spring friction, or the small mounting tilt seen in [](#fig-ringdown-a-vs-t)) couples more strongly into low even harmonics and the third harmonic than into higher odd harmonics. The comb nevertheless confirms a coherent mechanical oscillation rather than broadband readout noise.

The horizontal line in [](#fig-ringdown-asd-low) marks the typical ADXL354 noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ from the datasheet[@adxl354_datasheet]. Every $z$-channel spectral line sits orders of magnitude above this reference. For this validation dataset the mechanical signal therefore dominates the sensor intrinsic noise floor, as intended for a sanity check on a macroscopic oscillator.

[](#fig-ringdown-asd-z) zooms the $z$-channel ASD out to $20\ \mathrm{Hz}$.

```{figure} figures/Ringdown_ASD_Z_0-20Hz.png
:label: fig-ringdown-asd-z
:alt: z-axis ringdown ASD from 0 to 20 Hz

Welch ASD of the $z$-channel ringdown from $0$ to $20\ \mathrm{Hz}$ ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$). Harmonic lines above the $\sim 1\ \mathrm{Hz}$ fundamental are spaced by approximately integer multiples of the drive frequency. The datasheet noise floor is shown for comparison.
```

Above the fundamental, a comb of lines appears at approximately $2\ \mathrm{Hz}$, $3\ \mathrm{Hz}$, $4\ \mathrm{Hz}$, and higher frequencies up to the plotted band. The spacing follows the fundamental period: each additional line lies near an integer multiple of $\sim 1\ \mathrm{Hz}$. This harmonic content is expected when the motion is periodic but not perfectly sinusoidal, and it mirrors the richer structure already visible in the $x$- and $y$-wobbles of [](#fig-ringdown-wobble). The harmonics remain well above the datasheet noise floor across the $0$–$20\ \mathrm{Hz}$ band shown here.

The datasheet noise floor is a useful reference, but it does not by itself set the lowest line observed in every configuration. In the cryostat baseline measurements discussed later, the measured broadband floor with the cooler off lies roughly a factor of five above $22.5 \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$, likely because the Rigol scope readout adds broadband noise on top of the sensor. That offset is not resolved here; for the ringdown validation the relevant point is that the $\sim 1\ \mathrm{Hz}$ fundamental and its harmonics stand clearly above both the datasheet floor and the expected readout contribution. Together, the flip test, ringdown time traces, envelope decay, and spectra confirm that the three-axis chain reproduces known static and dynamic accelerations before it is applied to the fridge-mounted recordings.

