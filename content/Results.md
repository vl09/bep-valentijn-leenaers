(results)=
# Results
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

In the graph, the upright plateau sits at $+1.0\,\mathrm{g}$ and the inverted plateau at $-1.0\,\mathrm{g}$. Large excursions during the manual flip ($\sim 6$–$7\,\mathrm{s}$) reach roughly $+1.5\,\mathrm{g}$ and $-2.3\,\mathrm{g}$ and are not used for calibration.

### Mass-spring ringdown
The second validation experiment records a benchtop mass-spring ringdown while a video camera captures the motion against a ruler, as described in [](#methods).

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

The accelerometer trace for the first $10\,\mathrm{s}$ is shown in [](#fig-ringdown-wobble). In the graph, the $z$-channel (blue) oscillates at roughly $1\,\mathrm{Hz}$ between extrema near $0.4\,\mathrm{g}$ and $1.5\,\mathrm{g}$. The dashed lines mark the kinematic limits $0.46\,\mathrm{g}$ and $1.54\,\mathrm{g}$. Smaller wobbles appear on the $x$- and $y$-channels at the same frequency.

```{figure} figures/Ringdown_wobble_zoom.png
:label: fig-ringdown-wobble
:alt: Three-axis accelerometer ringdown trace zoomed to the first 10 seconds

Caption: Calibrated acceleration during the first $10\,\mathrm{s}$ of the ringdown. Dashed lines on $z$ mark the expected extrema from the video and ruler analysis ($0.46\,\mathrm{g}$ and $1.54\,\mathrm{g}$).
```

[](#fig-ringdown-a-vs-t) shows the full $600\,\mathrm{s}$ recording. The $z$-channel amplitude decays slowly over the window; the $x$- and $y$-components remain small throughout.

```{figure} figures/Ringdown_a_vs_t.png
:label: fig-ringdown-a-vs-t
:alt: Three-axis accelerometer ringdown trace over the full 600 second recording

Caption: Calibrated acceleration over the full ringdown recording ($600\,\mathrm{s}$). Oscillation on $z$ decays gradually; off-axis wobbles stay small.
```

