---
abstract: |
    To be written.
numbering:
  figure:
    enumerator: "1.%s"
---
(introduction)=
# Introduction

## Optomechanics and cryogenic noise

Optomechanics is a technique that uses light trapped in a cavity to probe and control the motion of a mechanical resonator at the quantum level[@steeleLabResearch]. In microwave optomechanics, superconducting circuits cooled to millikelvin temperatures trap microwave photons and couple them to high-quality-factor mechanical resonators. Reaching and sustaining those temperatures for long periods is now routinely done with dry cryostats, which replace a continuous liquid-helium supply by a closed-cycle cryocooler[@radebaugh2009; @atrey2020]. The same experiments must still contend with noise that limits how precisely phonon motion can be read out and controlled[@vanSoest2025]. One contribution to that noise is mechanical vibration of the cold stages on which the devices are mounted.

## Cryocooler-induced vibrations

A cryocooler runs a repeating thermodynamic cycle: a working fluid, typically helium, is compressed and expanded so that heat is transported from a cold stage inside the cryostat to a warmer reject stage at ambient temperature. Displacers, valves, or remote motors move on each stroke. That motion couples into the surrounding frame, thermal links, and support structures, so the cooling cycle is also a periodic mechanical drive. Literature on dry cryostats with pulse-tube precooling reports a narrow-band component near $1.4\ \mathrm{Hz}$ and its harmonics[@maisonobe2018]. Wilkinson[@wilkinson2025] describes the related periodic ticking from helium-pump strokes in such a system. Cooling itself proceeds through a cascade of thermal stages rather than at a single temperature. Flexible links and passive isolation stages can attenuate high-frequency content, but the low-frequency periodic drive of the cooler remains a common disturbance along the chain[@wilkinson2025]. Sensitive devices sit at the lowest accessible stage, so the acceleration environment there sets part of the experimental noise floor.

## Vibration isolation and prior work

Passive vibration isolation is a standard response to a narrow-band cooler drive. A platform suspended on springs can be tuned so that its resonance lies away from the cooler line, reducing motion transmitted to the experiment. Prior work in SteeleLab has designed and characterised cryogenic mass-spring isolators for this purpose[@wilkinson2025]. Designing such an isolator, however, requires knowing what drive the fridge structure actually imposes. The cold plate of a cryostat is not itself a simple mass-spring oscillator: plates, supports, and thermal links form an extended elastic structure with many modes, so the acceleration spectrum at a mount point mixes cooler harmonics with structural resonances and, in a real measurement, electrical pickup from the readout chain.

## Scope and structure of the thesis

The objective of this thesis is to design a reliable three-axis ADXL354 measurement chain and to use it to quantify the acceleration environment on a DIY dry 4 K fridge stage cooled by a Gifford–McMahon (GM) cryocooler, relative to the baseline with the cooler off. SteeleLab operates several refrigeration systems for optomechanical work[@steeleLabResearch]; the present measurements use that DIY platform. Like pulse-tube systems, a GM cooler imposes a periodic mechanical drive on the cold stage, with a fundamental set by the cold-head cycle, typically of order $1$--$2\ \mathrm{Hz}$[@atrey2020]. The thesis is complementary to Wilkinson's isolator study: it does not measure a cryogenic mass-spring isolator. Instead, it characterises the drive on the fridge stage that such an isolator would see. A three-axis ADXL354 MEMS accelerometer is interfaced and calibrated, then mounted on the cold plate. Recordings with the GM cooler off establish an electrical and environmental baseline. Recordings with the cooler on are compared with that baseline in both the time domain and the frequency domain, using amplitude spectral density (ASD) estimated by Welch's method.

This research has four main focusses. First, interfacing and reading out the ADXL354 reliably in three axes. Second, validating that the calibrated chain reproduces known static and dynamic accelerations, using a gravity-flip test and a benchtop mass-spring ringdown as a sanity check. Third, measuring the ASD on the fridge stage with the GM cooler off. Fourth, quantifying the additional vibration that appears with the GM cooler on, relative to that baseline, including partial interpretation of spectral features where the evidence is clear.

The main research question addressed in this thesis is:

> What acceleration spectral density does a GM cryocooler impose on a fridge stage, relative to the baseline with the cooler off?

This thesis begins by establishing the theoretical background relevant to cryogenic vibration characterisation. The experimental approach is then described. Results and discussion follow, before a conclusion summarises the findings. The thesis guides the reader through the theoretical background and the methodological approach, then through the results and their implications. It concludes by discussing the impact of these findings and suggestions for future research directions.

This thesis has been written as part of the Bachelor End Project of Applied Physics at Delft University of Technology, in the SteeleLab group under supervision of prof. dr. Gary Steele and daily supervision of Postdoc Thomas Clark.
