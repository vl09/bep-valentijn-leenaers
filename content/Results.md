(results)=
# Results & Discussion
## Accelerometer validation

### Static flip test
The raw $z$-channel voltage from the flip recording is shown in [](#fig-flip-voltage).

```{figure} figures/Flip_voltage.png
:label: fig-flip-voltage
:alt: Raw z-axis voltage during a 180 degree gravity flip

Caption: Raw $z$-channel scope voltage during the static flip test. The sensor rests at $+1\,\mathrm{g}$ for the first $\sim 6\,\mathrm{s}$, is flipped manually, and then rests at $-1\,\mathrm{g}$. Transients during the flip are excluded from the calibration windows.
```

In the upright plateau ($4$–$5\,\mathrm{s}$), the mean voltage is $\bar{V}_{+1\mathrm{g}} = 1.289\,\mathrm{V}$. In the inverted plateau ($9$–$10\,\mathrm{s}$), $\bar{V}_{-1\mathrm{g}} = 0.505\,\mathrm{V}$. From [](#eq-flip-sensitivity), the sensitivity is $S = 0.391\,\mathrm{V/g}$ ($392\,\mathrm{mV/g}$). The estimated zero-$g$ offset is $\bar{V}_0 = 0.897\,\mathrm{V}$, close to the nominal $\mathrm{V_{1P8ANA}}/2 = 0.9\,\mathrm{V}$. This value is used as the fixed offset in all later voltage-to-$g$ conversions. For the $\pm 2\,\mathrm{g}$ range, the datasheet quotes $368$–$432\,\mathrm{mV/g}$ on all three outputs (typical $400\,\mathrm{mV/g}$)[@adxl354_datasheet]. The extracted $392\,\mathrm{mV/g}$ lies within this specification and within $\sim 2\%$ of the typical value.

The same trace converted to acceleration with [](#eq-voltage-to-g) is shown in [](#fig-flip).

```{figure} figures/Flip.png
:label: fig-flip
:alt: z-axis acceleration in g during a 180 degree gravity flip

Caption: $z$-axis acceleration after applying the flip-test sensitivity and offset from [](#eq-voltage-to-g). Steady plateaus before and after the flip read $+1\,\mathrm{g}$ and $-1\,\mathrm{g}$ respectively.
```

In the graph, the upright plateau sits at $+1.0\,\mathrm{g}$ and the inverted plateau at $-1.0\,\mathrm{g}$. Large excursions during the manual flip ($\sim 6$–$7\,\mathrm{s}$) reach roughly $+1.5\,\mathrm{g}$ and $-2.3\,\mathrm{g}$ and are not used for calibration. Together, the flip test confirms that the voltage-to-$g$ conversion reproduces the known $\pm 1\,\mathrm{g}$ static levels and that the extracted sensitivity is consistent with the datasheet.

### Mass-spring ringdown
The second validation experiment records a benchtop mass-spring ringdown while a video camera captures the motion against a ruler, as described in [](#methods). This test is a sanity check on the calibrated chain: a simple oscillator with an independently measured frequency and amplitude should produce accelerations that agree with kinematics and decay as expected for a damped mass-spring system[@wilkinson2025].

+++{"no-pdf": true}

The recording is shown in [](#vid-ringdown).

```{figure} figures/ringdown.mp4
:label: vid-ringdown
:width: 50%
:align: center

Caption: Benchtop mass-spring ringdown recorded alongside the accelerometer trace. A ruler beside the apparatus provides the displacement scale.
```

+++

From the video, ten complete oscillations occur between $t = 2.24\,\mathrm{s}$ and $t = 12.29\,\mathrm{s}$, giving a window duration $\Delta t = 10.05\,\mathrm{s}$ and

$$
f = \frac{10}{\Delta t} = 0.995\,\mathrm{Hz}.
$$

With $\omega = 2\pi f$ and displacement amplitude $A = 13.5\,\mathrm{cm} = 0.135\,\mathrm{m}$ from the ruler span described in [](#methods), [](#eq-shm-peak-accel) gives a peak oscillatory acceleration of

$$
\frac{a_{\mathrm{peak}}}{g} = \frac{A\omega^2}{g} = 0.54\,\mathrm{g}.
$$

Because the $z$-axis measures gravity plus the vertical oscillation, the expected $z$-channel range is $1.0 \pm 0.54\,\mathrm{g}$, i.e. approximately $0.46\,\mathrm{g}$ to $1.54\,\mathrm{g}$.

#### Short-time wobble structure
The accelerometer trace for the first $10\,\mathrm{s}$ is shown in [](#fig-ringdown-wobble).

```{figure} figures/Ringdown_wobble_zoom.png
:label: fig-ringdown-wobble
:alt: Three-axis accelerometer ringdown trace zoomed to the first 10 seconds

Caption: Calibrated acceleration during the first $10\,\mathrm{s}$ of the ringdown. Dashed lines on $z$ mark the expected extrema from the video and ruler analysis ($0.46\,\mathrm{g}$ and $1.54\,\mathrm{g}$).
```

In this window the dominant motion is on the $z$-axis (blue). Ten full oscillation cycles fit within the $10\,\mathrm{s}$ span, consistent with the video count and $f \approx 1\,\mathrm{Hz}$. The $z$-trace swings between extrema near $0.4\,\mathrm{g}$ and $1.5\,\mathrm{g}$, in agreement with the kinematic limits marked by the dashed lines at $0.46\,\mathrm{g}$ and $1.54\,\mathrm{g}$.

Smaller periodic motion appears on the off-axis channels. The $x$-channel (red) oscillates about a negative offset near $-0.15\,\mathrm{g}$ with peak-to-peak wobble amplitude of order $0.1\,\mathrm{g}$. The $y$-channel (green) shows a similar wobble about a positive offset near $+0.15\,\mathrm{g}$. Each off-axis trace repeats on roughly the same $\sim 1\,\mathrm{Hz}$ timescale as the vertical motion, but the waveforms are not pure sinusoids: higher-frequency ripples are superposed on the main period. This is expected for a real benchtop spring-mass assembly, where slight misalignment and coupling introduce lateral modes alongside the intended vertical oscillation.

Even within this short window, the oscillation amplitudes evolve slowly. The $z$-peaks near $t = 0\,\mathrm{s}$ sit slightly above those near $t = 10\,\mathrm{s}$, and the $x$- and $y$-wobbles narrow in the same interval. The ringdown is therefore already visible at the scale of individual cycles, before the full recording is considered.

#### Full ringdown and exponential decay
[](#fig-ringdown-a-vs-t) shows the complete $600\,\mathrm{s}$ trace.

```{figure} figures/Ringdown_a_vs_t.png
:label: fig-ringdown-a-vs-t
:alt: Three-axis accelerometer ringdown trace over the full 600 second recording

Caption: Calibrated acceleration over the full ringdown recording ($600\,\mathrm{s}$). Oscillation envelopes decay on all three axes; the $z$-channel returns to a steady level near $1\,\mathrm{g}$.
```

Zooming out reveals the damping time scale. On $z$, the large $\sim 1\,\mathrm{Hz}$ oscillation about $1\,\mathrm{g}$ decays from an initial span of roughly $0.4$–$1.5\,\mathrm{g}$ to a near-constant $1\,\mathrm{g}$ by the end of the window. The $x$- and $y$-channels also show exponential decay of their wobble envelopes, from initial lateral amplitudes of order $0.1\,\mathrm{g}$ down to steady offsets near $-0.15\,\mathrm{g}$ and $+0.15\,\mathrm{g}$ respectively. Although the off-axis motion is much smaller than the vertical component, it follows the same qualitative pattern: a damped oscillation superposed on a constant bias.

This behaviour matches the lightly damped ringdown model in [](#eq-ringdown-solution), where the envelope decays as $A_0 e^{-\Gamma_m t/2}$. To make the decay explicit, an exponential envelope is fitted to the $z$-channel amplitude and overlaid on the data in [](#fig-ringdown-envelope).

```{figure} figures/Ringdown_envelope_fit.png
:label: fig-ringdown-envelope
:alt: z-axis ringdown with exponential envelope fit

Caption: $z$-axis ringdown acceleration with the analytic envelope $A_0 e^{-\Gamma_m t/2}$ from [](#eq-envelope-fit) overlaid. The fitted decay follows the slowly damped benchtop spring over the full recording ($\sim 10\,\mathrm{min}$).
```

The overlay follows the decaying $z$-oscillation over the full $600\,\mathrm{s}$ window. A decay time of order $10\,\mathrm{min}$ is consistent with the slowly damped benchtop spring used here and confirms that the accelerometer tracks the envelope of a physical mass-spring ringdown rather than a stationary offset or an artefact of the readout chain. Quantitative extraction of $\Gamma_m$ is not required for the validation goal; the agreement between kinematics, frequency, amplitude, and envelope shape is sufficient to establish confidence in the measurement chain before applying it to cryostat data.
