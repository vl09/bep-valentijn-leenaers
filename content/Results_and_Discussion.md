---
numbering:
  figure:
    enumerator: "4.%s"
  equation:
    enumerator: "4.%s"
---
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

In the upright plateau ($4$–$5\ \mathrm{s}$), the mean voltage is $\bar{V}_{+1\ \mathrm{g}} = 1.289\ \mathrm{V}$. In the inverted plateau ($9$–$10\ \mathrm{s}$), $\bar{V}_{-1\ \mathrm{g}} = 0.505\ \mathrm{V}$. Both plateaus are steady over their $1\ \mathrm{s}$ windows and bracket a $2\ \mathrm{g}$ span, as expected for $\pm 1\ \mathrm{g}$ orientations. The estimated zero-$g$ offset is $\bar{V}_0 = 0.897\ \mathrm{V}$, close to the nominal $\mathrm{V_{1P8ANA}}/2 = 0.9\ \mathrm{V}$. This value is used as the fixed offset in all later voltage-to-$g$ conversions. From [](#eq-flip-sensitivity), the sensitivity is $S = 0.392\ \mathrm{V/g}$ ($392\ \mathrm{mV/g}$). For the $\pm 2\ \mathrm{g}$ range, the datasheet quotes $368$–$432\ \mathrm{mV/g}$ on all three outputs (typical $400\ \mathrm{mV/g}$)[@adxl354_datasheet]. The extracted $392\ \mathrm{mV/g}$ lies within this min–max band and within $\sim 2\%$ of the typical value. 

That deviation is small compared with the datasheet min–max sensitivity band ($368$–$432\ \mathrm{mV/g}$). Further uncertainty arises from manual handling during the flip and scope digitisation. Sensitivity was taken from a single flip recording, without repeated runs to quantify scatter; for the validation goal here, confirming that the chain reproduces the known $\pm 1\ \mathrm{g}$ plateaus and yields a sensitivity consistent with the datasheet, one measurement is sufficient. 

The datasheet quotes predicted sensitivity repeatability over a $10$-year life of $0.16\%$ on $x$ and $y$ and $0.3\%$ on $z$[@adxl354_datasheet], including shifts from high-temperature operating life ($150$ °C), temperature cycling ($-55$ to $+125$ °C), velocity random walk, broadband noise, and temperature hysteresis; repeatability with time follows a square-root law[@adxl354_datasheet]. The sensors used here are new, so these ageing specifications do not bound the present flip test. A temperature coefficient of $\pm 0.01\ \%$ per degree Celsius over $-40$ to $+125$ °C[@adxl354_datasheet] means that a few degrees of laboratory temperature change cannot account for the $2\%$ offset from typical. Cross-axis coupling ($1\%$), nonlinearity ($0.1\%$ at $\pm 2\ \mathrm{g}$), and the use of one $z$-axis calibration for all three channels are further minor sources. 

For the scope of this thesis, however, which targets vibration frequencies and relative spectral structure rather than absolute $g$ metrology, these residual calibration uncertainties are acceptable: narrow-band peaks and harmonic spacing depend primarily on timing and shape, not on the few-percent difference between the extracted and nominal sensitivities.

Applying [](#eq-voltage-to-g) with the extracted $S$ and $\bar{V}_0$ converts the plateaus to $+1.0\ \mathrm{g}$ and $-1.0\ \mathrm{g}$, as required by the known $\pm 1\ \mathrm{g}$ gravity reference. The $\pm 1\ \mathrm{g}$ levels are reproduced to within the resolution set by the $1\ \mathrm{s}$ averaging windows and the datasheet sensitivity tolerance ($368$–$432\ \mathrm{mV/g}$)[@adxl354_datasheet], well inside the needs of the subsequent vibration analysis. Together, the flip test confirms that the voltage-to-$g$ conversion reproduces the known static levels and that the extracted sensitivity is consistent with the datasheet.

(results-mass-spring-ringdown)=
### Mass-spring ringdown
The second validation experiment records a benchtop mass-spring ringdown while a video camera captures the motion against a ruler, as described in [](#methods-mass-spring-ringdown). This test is a sanity check on the calibrated chain: a simple oscillator with an independently measured frequency and amplitude should produce accelerations that agree with kinematics and decay as expected for a damped mass-spring system[@wilkinson2025]. The apparatus is shown in [](#fig-mass-spring-setup).

+++{"no-pdf": true}

The recording is shown in [](#vid-ringdown).

```{figure} figures/ringdown.mp4
:label: vid-ringdown
:enumerated: false
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

In this window the dominant motion is on the $z$-axis (blue). The video count in [](#methods-mass-spring-ringdown) gives ten complete oscillations between $t = 2.24\ \mathrm{s}$ and $t = 12.29\ \mathrm{s}$, consistent with $f \approx 1\ \mathrm{Hz}$ and visible in the first $15\ \mathrm{s}$ of the trace. The $z$-trace swings between extrema near $0.4\ \mathrm{g}$ and $1.5\ \mathrm{g}$, consistent within uncertainty with the kinematic limits marked by the dashed lines at $0.46\ \mathrm{g}$ and $1.54\ \mathrm{g}$. Those reference levels are approximate: the ruler-based displacement amplitude in [](#methods-mass-spring-ringdown) was read only roughly, so the inferred extrema need not match the trace exactly. For this validation step, the agreement in frequency and approximate amplitude is nevertheless sufficient to support applying the calibrated chain from scope acquisition through [](#eq-voltage-to-g) to the cryostat recordings.

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

During the first $\sim 100\ \mathrm{s}$ the peak amplitudes drop more quickly than the dashed envelope. As discussed in [](#amplitude-dependent-damping), stronger dissipation at large displacement means a constant-$\Gamma_m$ fit chosen for $t \gtrsim 100\ \mathrm{s}$ sits above the early peaks. For $t \gtrsim 100\ \mathrm{s}$ the overlay and peaks agree. The fit is therefore a qualitative check on the decay time scale, not a full dynamical model of the ringdown, yet it suffices for validation: the trace shows the expected damped oscillation at the measured frequency and amplitude, rather than a stationary offset or readout artefact.

#### Ringdown spectra
After the time-domain checks, the ringdown recording is examined in the frequency domain. [](#fig-ringdown-asd-low) shows the Welch ASD of the $z$-channel from $0$ to $5\ \mathrm{Hz}$.

```{figure} figures/Ringdown_ASD_0-5Hz_3ch.png
:label: fig-ringdown-asd-low
:alt: z-axis ringdown ASD from 0 to 5 Hz

Welch ASD of the $z$-channel ringdown ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$) from $0$ to $5\ \mathrm{Hz}$. The horizontal line marks the datasheet noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$[@adxl354_datasheet].
```

The $z$-channel shows a sharp peak near $1\ \mathrm{Hz}$, in line with the video count ($f = 0.995\ \mathrm{Hz}$) and the $\sim 1\ \mathrm{Hz}$ oscillation in [](#fig-ringdown-wobble). Harmonic lines appear at integer multiples of the fundamental ($2\ \mathrm{Hz}$, $3\ \mathrm{Hz}$, and $4\ \mathrm{Hz}$ at the edge of the band). The comb confirms a coherent mechanical oscillation at the expected frequency rather than broadband readout noise.

The horizontal line in [](#fig-ringdown-asd-low) marks the typical ADXL354 noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ from the datasheet[@adxl354_datasheet]. Every $z$-channel spectral line sits orders of magnitude above this reference. For this validation dataset the mechanical signal therefore dominates the sensor intrinsic noise floor, as intended for a sanity check on a macroscopic oscillator.

[](#fig-ringdown-asd-z) zooms the $z$-channel ASD out to $20\ \mathrm{Hz}$.

```{figure} figures/Ringdown_ASD_Z_0-20Hz.png
:label: fig-ringdown-asd-z
:alt: z-axis ringdown ASD from 0 to 20 Hz

Welch ASD of the $z$-channel ringdown from $0$ to $20\ \mathrm{Hz}$ ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$). Harmonic lines above the $\sim 1\ \mathrm{Hz}$ fundamental are spaced by approximately integer multiples of the drive frequency. The datasheet noise floor is shown for comparison.
```

Above the fundamental, lines continue at approximately integer multiples of $\sim 1\ \mathrm{Hz}$ up to the $20\ \mathrm{Hz}$ limit of the plot. The peaks at even multiples ($2\ \mathrm{Hz}$, $4\ \mathrm{Hz}$, and beyond) and at $3\ \mathrm{Hz}$ stand above those at $5\ \mathrm{Hz}$, $7\ \mathrm{Hz}$, $9\ \mathrm{Hz}$, and $11\ \mathrm{Hz}$. This pattern is expected when the motion is periodic but not a pure sinusoid: a slightly asymmetric waveform about its mean (for example from amplitude-dependent spring friction or the small mounting tilt seen in [](#fig-mass-spring-mount)) couples more strongly into low even harmonics and the third harmonic than into higher odd harmonics. The structure mirrors the richer waveform already visible in the $x$- and $y$-channels of [](#fig-ringdown-wobble). The harmonics remain well above the datasheet noise floor across the plotted band.

The datasheet noise floor is a useful reference, but it does not by itself set the lowest line observed in every configuration. In the cryostat baseline measurements discussed later, the measured broadband floor with the cooler off lies roughly a factor of five above $22.5 \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$, likely because the Rigol scope readout adds broadband noise on top of the sensor. That offset is not resolved here; for the ringdown validation the relevant point is that the $\sim 1\ \mathrm{Hz}$ fundamental and its harmonics stand clearly above both the datasheet floor and the expected readout contribution. Together, the flip test, ringdown time traces, envelope decay, and spectra confirm that the three-axis chain reproduces known static and dynamic accelerations before it is applied to the fridge-mounted recordings.

(results-baseline)=
## Baseline with the GM cooler off

With the measurement chain validated on the bench, the accelerometer is mounted on the DIY dry 4K cryostat as described in [](#cryostat-vibration-measurements). The first cryostat recording keeps the GM cryocooler **off**, so that electrical pickup and any residual environmental vibration define a reference spectrum before the periodic cooler drive is introduced. This baseline addresses the third research question: what acceleration spectral density is present on the fridge stage when the cooler is not running?

Three contiguous scope segments ($1800\ \mathrm{s}$ total) are concatenated and converted to acceleration using the flip-test calibration from [](#results-static-flip-test). Welch ASD estimates use $n_{\mathrm{perseg}} = 60\ \mathrm{s}$, as in [](#methods) and the ringdown spectra above. [](#fig-baseline-asd) shows the result from $0$ to $120\ \mathrm{Hz}$ on all three channels, with the typical ADXL354 noise floor marked for comparison[@adxl354_datasheet].

```{figure} figures/Baseline_ASD_0-120Hz_3ch.png
:label: fig-baseline-asd
:alt: Three-axis baseline ASD with GM cooler off from 0 to 120 Hz

Welch ASD on the DIY 4K cold plate with the GM cooler off ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$, $1800\ \mathrm{s}$ trace). The horizontal line marks the datasheet noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$[@adxl354_datasheet].
```

The dominant narrow-band feature is a line at $50\ \mathrm{Hz}$ on all three channels, with peak ASD values of approximately $14\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$, $6\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $y$, and $12\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$. Harmonics appear at $100\ \mathrm{Hz}$ and $150\ \mathrm{Hz}$ with the same qualitative ordering: $x$ and $z$ are stronger than $y$ at $50\ \mathrm{Hz}$, while all three remain well above the datasheet reference. The $100\ \mathrm{Hz}$ peaks reach roughly $1.4\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$, $1.2\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $y$, and $1.8\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$.

These lines are consistent with mains-frequency electrical interference at $50\ \mathrm{Hz}$ and its integer harmonics. The criterion in [](#distinguishing-electrical-from-mechanical-vibration) applies: the features appear at the same frequencies on every channel with comparable spectral shape, differing mainly in overall scale rather than in unrelated peak patterns. A line near $2.4\ \mathrm{Hz}$ is also visible on all three axes at a much lower level (of order $0.2\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$) and is treated the same way.

Between the harmonic lines, the spectrum shows a broad elevated region in the $15$–$25\ \mathrm{Hz}$ band on all channels, with local peaks near $25\ \mathrm{Hz}$ of order $0.3\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ ($\sim 0.33\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$, $\sim 0.32\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $y$, and $\sim 0.35\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$). Because this structure tracks all three axes similarly, it is referred to as "noise mountain" and is likely dominated by electrical pickup rather than a single mechanical mode of the cold plate. The same feature is traced directly against the cooler-on spectra in [](#fig-running-overlay-mid). Away from the narrow lines, the median ASD between $60$ and $90\ \mathrm{Hz}$ sits near $100$–$110\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ on each channel. This broadband level is roughly a factor of five above the datasheet noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$, suggesting additional broadband noise from the scope readout chain on top of the sensor intrinsic floor. The origin of that offset is not resolved here; it is nevertheless small compared with the $50\ \mathrm{Hz}$ line and the cooler-on spectra presented in the next section.

A few weaker peaks differ between axes. On $x$, a line near $38\ \mathrm{Hz}$ reaches $\sim 0.18\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$, slightly above the corresponding features on $y$ ($\sim 0.13\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ near $42\ \mathrm{Hz}$) and $z$ ($\sim 0.13\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ near $38\ \mathrm{Hz}$). That pattern is more axis-dependent than the $50\ \mathrm{Hz}$ family and may reflect a weak mechanical response of the extended plate, but individual modes are not assigned without further modal information. Overall, the cooler-off spectrum establishes an electrical and environmental reference floor: narrow $50\ \mathrm{Hz}$ harmonics and a broadband readout contribution well below the levels that appear once the GM cryocooler is switched on.

(results-running-time)=
## GM cooler on: time domain
With the electrical and environmental floor established, the same three segments are recorded with the GM cryocooler running, addressing the fourth research question: what additional vibration appears once the cooler is switched on, relative to the baseline. [](#fig-running-time) shows the first $10\ \mathrm{s}$ of the calibrated three-axis trace, with dashed lines marking the $\pm 2\ \mathrm{g}$ sensor range from [](#adxl354-accelerometer).

```{figure} figures/Running_time_10s_3ch.png
:label: fig-running-time
:alt: Three-axis accelerometer trace with GM cooler running, first 10 seconds, with plus/minus 2 g limit lines

Calibrated acceleration during the first $10\ \mathrm{s}$ with the GM cooler running. Dashed lines mark the $\pm 2\ \mathrm{g}$ sensor range.
```

On $z$, sharp repeated bursts appear on top of the $\sim 1\ \mathrm{g}$ gravitational offset, roughly twice per second. The $x$- and $y$-channels show correlated bursts of the same timing, oscillating about a near-zero mean with excursions of order $\pm 0.5$–$0.6\ \mathrm{g}$ before decaying back to the quiet baseline within roughly $0.1\ \mathrm{s}$. All three channels stay within the dashed $\pm 2\ \mathrm{g}$ lines throughout this window.

[](#fig-running-heartbeat) zooms into a single $z$-channel drive cycle, spanning $1.1\ \mathrm{s}$.

```{figure} figures/Running_GM_heartbeat_zoom.png
:label: fig-running-heartbeat
:alt: Zoomed z-axis trace showing one GM cryocooler cycle with a strong and a weak tick-back-tick pair

Calibrated $z$-axis acceleration over one GM drive cycle. Two double-spike (tick-back-tick) events appear per cycle: a strong pair near $t = 1.4\ \mathrm{s}$ and a weaker pair near $t = 1.86\ \mathrm{s}$.
```

Each cycle repeats with a period of $1.00\ \mathrm{s}$ and contains two double-spike events, consistent with the tick-back-tick signature predicted for the GM displacer and valve motion in [](#gifford-mcmahon-cryocooler-drive). The stronger pair reaches $1.86\ \mathrm{g}$ and $1.76\ \mathrm{g}$, separated by $\sim 54\ \mathrm{ms}$; the weaker pair, $\sim 0.47\ \mathrm{s}$ later in the same cycle, peaks near $1.47\ \mathrm{g}$. Between events, the $z$-channel settles back to the $\sim 1\ \mathrm{g}$ gravitational plateau within $\sim 0.1\ \mathrm{s}$.

Across the full $1800\ \mathrm{s}$ recording, the $z$-channel briefly exceeds $+2\ \mathrm{g}$ in $93$ of $9 \times 10^6$ samples ($< 0.002\%$ of the trace), all coincident with the strongest tick events. The bulk of the periodic drive therefore stays comfortably inside the sensor's linear range, with only the extreme tail of the strongest bursts approaching the $\pm 2\ \mathrm{g}$ limit.

(results-running-spectra)=
## GM cooler on: spectral analysis
The time-domain bursts in [](#fig-running-heartbeat) point to a periodic drive near $1\ \mathrm{Hz}$. [](#fig-running-overlay-low-z) compares the $z$-channel Welch ASD ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$) with the cooler on and off, from $0$ to $20\ \mathrm{Hz}$.

```{figure} figures/Running_baseline_overlay_Z_0-20Hz.png
:label: fig-running-overlay-low-z
:alt: z-axis ASD comparison between GM cooler on and off from 0 to 20 Hz

Welch ASD of the $z$-channel ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$) from $0$ to $20\ \mathrm{Hz}$, cooler off (grey) and cooler on (blue).
```

With the cooler on, a comb of lines spaced by $\approx 1\ \mathrm{Hz}$ appears, matching the $1.00\ \mathrm{s}$ cycle period read from the time trace. The strongest lines reach $1.77\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $5\ \mathrm{Hz}$, $1.67\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $7\ \mathrm{Hz}$, and $\sim 1.4\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $8$–$10\ \mathrm{Hz}$, roughly $15$–$18\times$ above the flat cooler-off floor at the same frequencies ($\sim 0.1\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$). The mechanical drive comb dominates the electrical baseline throughout this band.

[](#fig-running-overlay-mid) widens the comparison to all three channels from $0$ to $120\ \mathrm{Hz}$.

```{figure} figures/Running_baseline_overlay_0-120Hz.png
:label: fig-running-overlay-mid
:alt: Three-axis ASD comparison between GM cooler on and off from 0 to 120 Hz

Welch ASD on all three channels ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$) from $0$ to $120\ \mathrm{Hz}$, cooler off (grey, all axes) and cooler on (coloured).
```

The $1\ \mathrm{Hz}$ comb continues across the full band. The $50\ \mathrm{Hz}$ mains line is visible at a comparable level with the cooler on and off ($16.0$ vs $13.6\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$; $4.9$ vs $6.4\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $y$; $16.8$ vs $12.4\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$), consistent with the electrical-pickup criterion of [](#distinguishing-electrical-from-mechanical-vibration): a feature unaffected by the cooler state is not driven by the cooler.

The baseline noise mountain from [](#results-baseline) is also visible in [](#fig-running-overlay-mid). In the grey cooler-off traces it appears as the same broad elevation centred near $25\ \mathrm{Hz}$. With the cooler on, the coloured traces in that band sit above the grey curves by factors of $\sim 3$–$11$ at the local crest (e.g. $\sim 0.35$ vs $3.7\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$ near $26\ \mathrm{Hz}$), because the $1\ \mathrm{Hz}$ GM comb places a drive line at every integer frequency and therefore superposes mechanical content on the cooler-independent electrical bump. Unlike the comb region below $\sim 20\ \mathrm{Hz}$, where cooler-on levels exceed the baseline by more than an order of magnitude, the grey and coloured curves remain closer together near $\sim 25\ \mathrm{Hz}$. The noise mountain therefore persists as a recognizable cooler-off reference in the overlay, but is partially masked once GM harmonics at $24$–$26\ \mathrm{Hz}$ are added.

Between $70$ and $90\ \mathrm{Hz}$, a broad elevated region appears on all channels (median $\sim 200$–$240\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ with the cooler on, roughly double the cooler-off floor there), with sharp peaks reaching $20$–$26\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ near $80$–$82\ \mathrm{Hz}$ on $x$ and $y$.

[](#fig-running-asd-mid) shows the cooler-on spectrum alone on the same $0$–$120\ \mathrm{Hz}$ band, with the datasheet noise floor for reference.

```{figure} figures/Running_ASD_0-120Hz_3ch.png
:label: fig-running-asd-mid
:alt: Three-axis ASD with GM cooler running from 0 to 120 Hz

Welch ASD on all three channels with the GM cooler running ($n_{\mathrm{perseg}} = 60\ \mathrm{s}$), $0$ to $120\ \mathrm{Hz}$. The horizontal line marks the datasheet noise floor of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$[@adxl354_datasheet].
```

The strongest individual lines in this band sit near $99\ \mathrm{Hz}$ ($41.1\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$, $30.0\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$) and near $71\ \mathrm{Hz}$ ($19$–$20\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on all three channels), each several orders of magnitude above the $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ datasheet floor.

[](#fig-running-asd-wide) coarsens the segment length to $n_{\mathrm{perseg}} = 2\ \mathrm{s}$ and extends the range to $200\ \mathrm{Hz}$.

```{figure} figures/Running_ASD_0-200Hz_3ch.png
:label: fig-running-asd-wide
:alt: Three-axis ASD with GM cooler running from 0 to 200 Hz, coarser resolution

Welch ASD on all three channels with the GM cooler running ($n_{\mathrm{perseg}} = 2\ \mathrm{s}$), $0$ to $200\ \mathrm{Hz}$.
```

The coarser segmentation trades frequency resolution for a smoother view, as discussed in [](#spectral-analysis): the narrow $1\ \mathrm{Hz}$-spaced comb broadens into overlapping humps of elevated broadband structure that extend up to $\sim 200\ \mathrm{Hz}$, distinct from the $\sim 25\ \mathrm{Hz}$ noise mountain identified in [](#results-baseline). The humps are axis-dependent: $x$ peaks near $99\ \mathrm{Hz}$ ($9.3\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$) and $171\ \mathrm{Hz}$ ($11.4\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$), while $y$ peaks near $82\ \mathrm{Hz}$ ($7.9\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$) and $z$ near $99\ \mathrm{Hz}$ ($12.7\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$), matching the axis-dependent mode picture of [](#mechanical-response-of-extended-structures).

Finally, [](#fig-running-asd-full) extends the same $2\ \mathrm{s}$-segment spectrum to the full $0$–$2.5\ \mathrm{kHz}$ sensor bandwidth.

```{figure} figures/Running_ASD_0-2500Hz_3ch.png
:label: fig-running-asd-full
:alt: Three-axis ASD with GM cooler running from 0 to 2500 Hz

Welch ASD on all three channels with the GM cooler running ($n_{\mathrm{perseg}} = 2\ \mathrm{s}$), $0$ to $2.5\ \mathrm{kHz}$.
```

Distinct, axis-dependent peaks persist well above $200\ \mathrm{Hz}$. The $x$-channel shows peaks near $677\ \mathrm{Hz}$ ($3.7\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$) and $2209\ \mathrm{Hz}$ ($2.9\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$) that are not prominent on $y$ or $z$. Conversely, $y$ and $z$ share peaks near $488\ \mathrm{Hz}$ ($2.3$ and $10.9\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$, respectively) and near $1290\ \mathrm{Hz}$ ($3.2$ and $4.7\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$) that $x$ does not show at comparable strength. This pattern is consistent with the mode-shape picture of an extended structure from [](#mechanical-response-of-extended-structures): different resonances of the cold plate couple more strongly to some axes than others, rather than one lumped oscillator responding equally on every channel.

It should be noted that the $\sim 2.2\ \mathrm{kHz}$ feature on $x$ lies close to the $\sim 2.5\ \mathrm{kHz}$ resonance of the ADXL354 transfer function itself ([](#fig-adxl354-transfer)), so this peak may partly reflect the sensor response rather than the cryostat structure alone. More generally, individual peaks in [](#fig-running-asd-wide) and [](#fig-running-asd-full) are not assigned to specific structural components without further modal information; the honest summary is that the GM cooler drives a rich, axis-dependent harmonic and broadband response that stands clearly above both the datasheet noise floor and the cooler-off baseline, while the mains-frequency line and its harmonics remain identifiable as a separate, cooler-independent electrical contribution throughout.
