'''
here, I make some dummy data to see if we can qualitatively understand the pulse tube noise.
I at first expected that we should be able to see the pulse tube frequency in the frequency spectrum, but it is
actually the case that the PT nosie causes "sidebands" to emerge! Neat.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fft import fft, fftfreq

MAKE_NOISE = False

plt.close('all')
N = 50000
d_length = 500
fs = d_length/N
T = d_length/N
t = np.linspace(0,d_length,N)
f_carrier  =12

V = np.sin(f_carrier*np.pi*t)
if MAKE_NOISE ==False:
    rng = np.random.default_rng()
    V = rng.standard_normal(N)

pulse_freq = 0.1
pulse_time = 1/pulse_freq
num_pulses = d_length/pulse_time
for i in np.arange(int(num_pulses)):
    if i == 0 :
        _, envs = signal.gausspulse(t-i*pulse_time, fc=500, bw =0.001, retenv=True)
    else :
        _, e = signal.gausspulse(t-i*pulse_time, fc=500, bw =0.001, retenv=True)
        envs = envs+e

fig, (ax_t, ax_w) = plt.subplots(2,1)
ax_t.set_xlabel('Time (s)')
ax_t.set_ylabel('Voltage (V)')

ax_t.plot( t, envs, '-', color='firebrick', alpha=0.7)
ax_t.plot(t,V*envs, color = 'cornflowerblue', alpha=0.7)

Vf = fft(V*envs)
xf = fftfreq(N, T)[:N//2]

Vf_env = fft(envs)
xf_env = fftfreq(N, T)[:N//2]

f, Pxx_den = signal.welch(V*envs, fs, nperseg=1024)
#ax_w.plot(xf, 2.0/N * np.abs(Vf[0:N//2]), color='cornflowerblue', alpha = 0.7, label='6Hz Carrier modulated by 0.1Hz envelope')
ax_w.plot(xf, 2.0/N * np.abs(Vf[0:N//2]), color='cornflowerblue', alpha = 0.7, label='Noise modulated by 0.1Hz envelope')
ax_w.plot(xf_env, 2.0/N * np.abs(Vf_env[0:N//2]), color='firebrick', alpha = 0.7, label='0.1Hz envelope')

#ax_w.plot(f*2*np.pi, Pxx_den , color='coral', alpha = 0.7)

ax_w.set_xlabel('Frequency (cycles/s)')
ax_w.set_ylabel('|FFT| (a.u.)')
plt.grid()
plt.show()
plt.legend()
plt.tight_layout()