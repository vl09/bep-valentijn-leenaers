---
numbering:
  figure:
    enumerator: "5.%s"
---
(conclusion)=
# Summary & Outlook

## Summary

In this thesis, a reliable three-axis ADXL354 measurement chain was designed and validated, then used to characterise vibrations on the final cold stage of a DIY dry 4K fridge cooled by a Gifford–McMahon cryocooler.

The calibrated chain reproduces known static and dynamic accelerations. A gravity-flip test yields a sensitivity of $S = 392\,\mathrm{mV/g}$ and a zero-$g$ offset of $\bar{V}_0 = 0.897\,\mathrm{V}$, within the datasheet band of $368$–$432\,\mathrm{mV/g}$ and within $\sim 2\%$ of the typical $400\,\mathrm{mV/g}$[@adxl354_datasheet]. A benchtop mass-spring ringdown oscillates at $f = 0.995\,\mathrm{Hz}$ with $z$-channel extrema consistent with the kinematic estimate of $0.46$–$1.54\,\mathrm{g}$.

With the GM cooler off, the final-stage ASD is dominated by electrical pickup: a $50\,\mathrm{Hz}$ mains line reaching approximately $14$, $6$, and $12\,\mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $x$, $y$, and $z$, together with a broadband floor of order $100$–$110\,\mu\mathrm{g}/\sqrt{\mathrm{Hz}}$ between $60$ and $90\,\mathrm{Hz}$, roughly five times the datasheet noise density of $22.5\,\mu\mathrm{g}/\sqrt{\mathrm{Hz}}$. With the cooler on, a periodic thud–thud, pause, thud, pause heartbeat with period $1.00\,\mathrm{s}$ appears in the time domain. In the frequency domain this drive produces a comb of lines spaced by $\approx 1\,\mathrm{Hz}$. The strongest low-frequency cooler lines reach $1.77\,\mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $5\,\mathrm{Hz}$ and $1.67\,\mathrm{mg}/\sqrt{\mathrm{Hz}}$ at $7\,\mathrm{Hz}$, roughly $15$–$18$ times the cooler-off floor at the same frequencies. Across $0$–$120\,\mathrm{Hz}$, the largest cooler-on peaks sit near $99\,\mathrm{Hz}$ ($41.1\,\mathrm{mg}/\sqrt{\mathrm{Hz}}$ on $z$) and near $71\,\mathrm{Hz}$ ($19$–$20\,\mathrm{mg}/\sqrt{\mathrm{Hz}}$ on all three channels). Higher-frequency structure is axis-dependent, consistent with mode shapes of an extended cold plate. The $50\,\mathrm{Hz}$ mains line remains comparable with the cooler on and off, confirming that it is a separate electrical contribution.

A reliable three-axis ADXL354 chain can therefore characterise the acceleration spectral density on the final stage of a GM cryocooler relative to the cooler-off baseline. The cooler drive is a clear $\approx 1\,\mathrm{Hz}$ harmonic comb standing well above that baseline.

## Outlook
Microwave optomechanics relies on millikelvin environments in which phonon motion can be read out through coupling to a superconducting cavity[@steeleLabResearch]. Closed-cycle cryocoolers sustain these temperatures, but their periodic stroke is also a mechanical drive on the cold stages. Passive mass-spring isolation is the standard response[@wilkinson2025]; before its effectiveness can be judged, the disturbance at the mount point must be measured. That was the starting point of this thesis.

On the final cold stage, plates, supports, and thermal links form an extended structure with many modes, so the spectrum at a mount point mixes cooler harmonics, structural resonances, and electrical pickup. This work showed that a calibrated ADXL354 chain can separate the GM cooler drive from a cooler-off baseline on a DIY dry 4K fridge and recorded that drive in both time and frequency. The edge-mounted spectra in [](#fig-cryostat-mount) map that environment at room temperature, not yet the field at $4\,\mathrm{K}$ on an isolated platform.

Several gaps remain: peaks are not yet assigned to structural modes, the scope readout floor exceeds the datasheet limit, the strongest cooler bursts approach $\pm 2\,\mathrm{g}$, and crests near $\sim 2.2\,\mathrm{kHz}$ may partly follow the ADXL354 transfer function. The cooler-on comb and its axis-dependent harmonics nevertheless lie well above the cooler-off baseline, and closing these gaps motivates the measurements outlined below.

A light hammer impact with simultaneous phone audio could assign unidentified peaks and give coarse modal hints where acceleration alone is ambiguous. The same protocol at centre and edge positions on the DIY4K plate ([](#fig-cryostat-mount)) would test how local mode shapes change the spectrum. Spectroscopy should be repeated at nominal $4\,\mathrm{K}$: peaks above $\sim 70\,\mathrm{Hz}$ may shift once the plate is cold through thermal expansion and changed elastic moduli, whereas the $\approx 1\,\mathrm{Hz}$ GM drive period is expected to be far less temperature-sensitive. Cold operation would also require a gravity flip or another reference acceleration, because datasheet sensitivity guarantees do not extend to cryogenic use.

SteeleLab's main experiments run on Bluefors dilution refrigerators precooled by pulse-tube cryocoolers[@steeleLabResearch], where literature reports a component near $1.4\,\mathrm{Hz}$ and its harmonics[@maisonobe2018], distinct from the $\approx 1\,\mathrm{Hz}$ GM comb measured here. The same ADXL354 chain on a Bluefors stage would test whether that difference persists; measuring at the pulse-tube stage itself would characterise the precooler drive and allow comparison with spectra at lower mounting spots.

The cryogenic mass-spring platform in [](#fig-isolator-mount)[@wilkinson2025] offers the most direct test of passive isolation. Cooler-on spectra recorded at the spring attachment and on the isolated copper mass would show how much of the cooler drive passes through the mass-spring system before it reaches the experiment.

```{figure} figures/cryogenic_isolator_mount.png
:label: fig-isolator-mount
:width: 50%
:align: center

Cryogenic mass-spring isolation chain in a SteeleLab dilution refrigerator. From top to bottom: an eye bolt on a cold plate; a carabiner; a spring passing through the next plate; a fishing line through a lower plate; a second eye bolt on a cylindrical copper mass; and the experimental platform inside a magnetic shield suspended below the mass.
```

In conclusion, cryostat vibration limits how precisely phonon motion can be read out in microwave optomechanics, and the cooler cycle is a periodic part of that disturbance. This thesis showed that a calibrated ADXL354 chain can measure acceleration on a GM-cooled final stage relative to a cooler-off baseline. The spectra recorded here are room-temperature commissioning data on one fridge at one mount point, enough to justify carrying the same chain forward to colder plate temperatures, other cryostats, and the cryogenic mass-spring platforms SteeleLab uses to shield sensitive devices from this drive.
