(appendix-derivations)=
# Derivations
## Damped harmonic oscillator
Starting from the normalised equation of motion

$$
\ddot{x} + \Gamma_m \dot{x} + \omega_0^2 x = 0,
$$

substitute the trial solution $x(t) = e^{\lambda t}$. This gives the characteristic equation

$$
\lambda^2 + \Gamma_m \lambda + \omega_0^2 = 0,
$$

with roots

$$
\lambda_\pm = -\frac{\Gamma_m}{2} \pm \sqrt{\left(\frac{\Gamma_m}{2}\right)^2 - \omega_0^2}.
$$

For the underdamped case ($\Gamma_m < 2\omega_0$), the roots are complex conjugates and the real solution is

$$
x(t) = e^{-\Gamma_m t/2}\left(C_1 \cos\tilde{\omega}_0 t + C_2 \sin\tilde{\omega}_0 t\right),
$$

with $\tilde{\omega}_0 = \sqrt{\omega_0^2 - (\Gamma_m/2)^2}$. Equivalently, this is written as $x(t) = A e^{-\Gamma_m t/2}\cos(\tilde{\omega}_0 t + \varphi)$ with constants $A$ and $\varphi$ fixed by the initial displacement and velocity.
