---
numbering:
  figure:
    enumerator: "5.%s"
---
(conclusion)=
# Conclusion

## Summary and key findings

In this thesis, a reliable three-axis ADXL354 measurement chain was designed and validated, then used to characterise vibrations on the final cold stage of a DIY dry 4K fridge cooled by a Gifford–McMahon cryocooler.

The calibrated chain reproduces known static and dynamic accelerations. A gravity-flip test yields a sensitivity of $S = 392\ \mathrm{mV/g}$ and a zero-$g$ offset of $\bar{V}_0 = 0.897\ \mathrm{V}$, within the datasheet band of $368$–$432\ \mathrm{mV/g}$ and within $\sim 2\%$ of the typical $400\ \mathrm{mV/g}$[@adxl354_datasheet]. A benchtop mass-spring ringdown oscillates at $f = 0.995\ \mathrm{Hz}$ with $z$-channel extrema consistent with the kinematic estimate of $0.46$–$1.54\ \mathrm{g}$.

With the GM cooler off, the final-stage ASD is dominated by electrical pickup: a $50\ \mathrm{Hz}$ mains line reaching approximately $14$, $6$, and $12\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$, $y$, and $z$, together with a broadband floor of order $100$–$110\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ between $60$ and $90\ \mathrm{Hz}$, roughly five times the datasheet noise density of $22.5\ \mu\mathrm{g}/\sqrt{\mathrm{Hz}}$. With the cooler on, a periodic thud–thud, pause, thud, pause heartbeat with period $1.00\ \mathrm{s}$ appears in the time domain. In the frequency domain this drive produces a comb of lines spaced by $\approx 1\ \mathrm{Hz}$. The strongest low-frequency cooler lines reach $1.77\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $5\ \mathrm{Hz}$ and $1.67\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $7\ \mathrm{Hz}$, roughly $15$–$18$ times the cooler-off floor at the same frequencies. Across $0$–$120\ \mathrm{Hz}$, the largest cooler-on peaks sit near $99\ \mathrm{Hz}$ ($41.1\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$) and near $71\ \mathrm{Hz}$ ($19$–$20\ \mathrm{mg}/\sqrt{\mathrm{Hz}}$ on all three channels). Higher-frequency structure is axis-dependent, consistent with mode shapes of an extended cold plate rather than a single lumped oscillator. The $50\ \mathrm{Hz}$ mains line remains comparable with the cooler on and off, confirming that it is a separate electrical contribution.

In conclusion, a reliable three-axis ADXL354 chain can characterise the acceleration spectral density on the final stage of a GM cryocooler relative to the cooler-off baseline. The cooler drive is a clear $\approx 1\ \mathrm{Hz}$ harmonic comb standing well above that baseline.

## Recommendations for further improvements
It should be noted that the accelerometer was mounted near the plate edge, that many spectral peaks remain unassigned without modal information, and that the scope readout floor was not reduced to the datasheet noise density. The strongest cooler bursts briefly approach the $\pm 2\ \mathrm{g}$ sensor limit, and features near $\sim 2.2\ \mathrm{kHz}$ may partly reflect the ADXL354 transfer-function resonance. It might be worth exploring the same sensor on an experimental platform or on a cryogenic mass-spring isolation platform, and comparing centre versus edge placement. Further research could use a hammer impact with audio recording for modal hints.

Practically assigning every peak to a structural component, and bringing the electrical floor down to the datasheet limit, remain significant challenges for future work.
