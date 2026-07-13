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

In the upright plateau ($4$–$5\,\mathrm{s}$), the mean voltage is $\bar{V}_{+1\mathrm{g}} = 1.289\,\mathrm{V}$. In the inverted plateau ($9$–$10\,\mathrm{s}$), $\bar{V}_{-1\mathrm{g}} = 0.505\,\mathrm{V}$. From [](#eq-flip-sensitivity), the sensitivity is $S = 0.391\,\mathrm{V/g}$ ($390\,\mathrm{mV/g}$). The estimated zero-$g$ offset is $\bar{V}_0 = 0.897\,\mathrm{V}$, close to the nominal $\mathrm{V_{1P8ANA}}/2 = 0.9\,\mathrm{V}$. The extracted value lies within $\sim 3\%$ of the datasheet typical of $400\,\mathrm{mV/g}$[@adxl354_datasheet].

The same trace converted to acceleration with [](#eq-voltage-to-g) is shown in [](#fig-flip).

```{figure} figures/Flip.png
:label: fig-flip
:alt: z-axis acceleration in g during a 180 degree gravity flip

Caption: $z$-axis acceleration after applying the flip-test sensitivity and offset from [](#eq-voltage-to-g). Steady plateaus before and after the flip read $+1\,\mathrm{g}$ and $-1\,\mathrm{g}$ respectively.
```

In the graph, the upright plateau sits at $+1.0\,\mathrm{g}$ and the inverted plateau at $-1.0\,\mathrm{g}$. Large excursions during the manual flip ($\sim 6$–$7\,\mathrm{s}$) reach roughly $+1.5\,\mathrm{g}$ and $-2.3\,\mathrm{g}$ and are not used for calibration.

```{figure} figures/Ringdown_a_vs_t.png
:label: fig-ringdown-a-vs-t
```

```{figure} figures/Ringdown_ASD.png
:label: fig-ringdown-asd
```

```{figure} figures/Ringdown_ASD_zoomed.png
:label: fig-ringdown-asd-zoomed
```
