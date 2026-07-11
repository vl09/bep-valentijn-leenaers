# Experimental Method
In this chapter, the measurement chain and the procedures used to characterise vibrations are described. A static gravity-flip test first validates the ADXL354 accelerometer and the voltage-to-acceleration conversion. A mass-spring ringdown and cryostat-mounted noise spectroscopy then apply the calibrated chain to the systems introduced in the Introduction.

## Measurement setup
The three-axis accelerometer is an ADXL354 (Analog Devices), configured for the $\pm 2\,\mathrm{g}$ full-scale range. Each analog output is ratiometric to the on-chip $1.8\,\mathrm{V}$ analog supply $\mathrm{V1P8ANA}$: the zero-$g$ bias is nominally $\mathrm{V1P8ANA}/2 = 0.9\,\mathrm{V}$, and the datasheet quotes a typical sensitivity of $400\,\mathrm{mV/g}$ at this range[@adxl354_datasheet].

For all measurements reported here, the $x$, $y$, and $z$ outputs are connected to channels 1, 2, and 3 of a Rigol DS1054Z digital oscilloscope. The scope is controlled over Ethernet via PyVISA, and waveforms are transferred to a Python analysis environment. The scope operates in high-resolution acquisition mode with DC coupling. Channel offsets of $-0.9\,\mathrm{V}$ on channels 1 and 2, and $-1.2\,\mathrm{V}$ on channel 3, place the zero-$g$ bias near the centre of the oscilloscope grid, matching the $\mathrm{V1P8ANA}/2$ reference. A vertical scale of $0.1\,\mathrm{V/div}$ is used on all three channels. Deep-memory acquisitions store up to $3 \times 10^6$ points per channel. Recordings are saved as time series of voltage in `.npz` format for offline analysis; the acquisition and analysis notebooks are listed in [](#appendix-code).

### Alternative readout hardware
A Red Pitaya board with PyRPL was available as an alternative readout path. It offers a flexible lock-in style interface but records only two analog inputs per unit. Because simultaneous capture of all three accelerometer axes was required, the Rigol DS1054Z was used for the measurements reported in this thesis.

## Accelerometer validation
Three experiments are performed in sequence. First, sensor sensitivity is determined with a static gravity flip. Second, a mass-spring ringdown on the bench exercises the calibrated chain on a dynamic signal. Third, the same chain is applied to cryostat-mounted recordings for noise spectroscopy. The first two are described below; cryostat acquisition follows in a later section.

### Static flip test for sensitivity calibration
The flip test uses gravity as a known, steady $1\,\mathrm{g}$ acceleration. With the sensor at rest on the bench, the $z$-axis output corresponds to $+1\,\mathrm{g}$. After a manual $180^\circ$ rotation about the $z$-axis, the same axis reads $-1\,\mathrm{g}$. The change in output voltage between the two orientations spans $2\,\mathrm{g}$ and defines the sensitivity $S$ in $\mathrm{V/g}$.

A $12\,\mathrm{s}$ trace is recorded while the sensor is held steady in the upright orientation, flipped, and held steady again upside down. Transients during the flip are not used. Mean voltages $\bar{V}_{+1\mathrm{g}}$ and $\bar{V}_{-1\mathrm{g}}$ are taken from $1\,\mathrm{s}$ windows in the upright and inverted plateaus (from $4$ to $5\,\mathrm{s}$ and from $10$ to $11\,\mathrm{s}$ in the recording). Because the scope channels are referenced to $\mathrm{V1P8ANA}/2$, the plateau values are symmetric about zero. The sensitivity follows from

$$
S = \frac{|\bar{V}_{+1\mathrm{g}}| + |\bar{V}_{-1\mathrm{g}}|}{2}.
$$ (eq-flip-sensitivity)

The zero-$g$ offset is estimated as $\bar{V}_0 = (\bar{V}_{+1\mathrm{g}} + \bar{V}_{-1\mathrm{g}})/2$ and subtracted from all three channels. Acceleration in units of $g$ is then obtained from

$$
a_i = \frac{V_i - \bar{V}_0}{S},
$$ (eq-voltage-to-g)

where $V_i$ is the measured voltage on axis $i$. Equivalently, when a fixed datasheet offset $V_0 = \mathrm{V1P8ANA}/2 = 0.9\,\mathrm{V}$ is used instead of the measured $\bar{V}_0$, the same sensitivity value applies to subsequent recordings taken with the same supply voltage. The extracted $S$ and offset are reported in [](#results) and used for all later conversions.

### Mass-spring ringdown
The second experiment uses a vertical mass-spring oscillator of the type described in [](#theory). The ADXL354 is mounted on the oscillating mass. The mass is displaced from equilibrium, released, and the free ringdown is recorded on the Rigol scope while a video camera films the motion. A ruler placed alongside the system provides a length scale in the recording.

The ringdown trace is converted to acceleration using [](#eq-voltage-to-g) with the flip-test sensitivity and $V_0 = 0.9\,\mathrm{V}$. In parallel, the video is analysed to obtain two kinematic quantities: the oscillation frequency $f$, counted as the number of cycles per second in the early part of the motion, and the peak displacement amplitude $A$ of the mass relative to its equilibrium position, read from the ruler. Peak acceleration from kinematics is computed with [](#eq-shm-peak-accel) and compared to the accelerometer peak in the first few seconds of the recording; the outcome is reported in [](#results). The same trace is also analysed in the time domain: $f$ is read from a zoomed trace, and the amplitude envelope is fitted with [](#eq-envelope-fit) as described in [](#theory).
