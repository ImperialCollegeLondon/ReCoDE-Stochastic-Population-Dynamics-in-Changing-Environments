<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js"></script>

# Appendix 1 - Mathematical Analysis for the Time-Independent Case

## Problem Definition

We consider a population of cells where each cell can either divide at a rate $\gamma(\tau)$ or die at a rate 
$\delta(\tau)$, both dependent only on the cell's age $\tau$. In this scenario, the McKendrick–Von Foerster 
equation governing the population dynamics is:

$$
\begin{aligned}
\left(\partial_t + \partial_\tau\right) n(\tau, t) &= -\left(\gamma(\tau) + \delta(\tau)\right) n(\tau, t), \\
n(0, t) &= 2 \int_0^\infty \gamma(\tau) n(\tau, t) \, d\tau.
\end{aligned}
$$

### Key Components:
1. **Cell Division ($\gamma(\tau)$)**: A cell can divide at an age-dependent rate.
2. **Cell Death ($\delta(\tau)$)**: A cell can die before dividing, also at an age-dependent rate.
3. **Birth Condition**: Division creates two new cells of age zero, forming the boundary condition at $n(0, t)$.

Our goal is to determine the population dynamics $n(\tau, t)$, particularly the asymptotic growth rate $\lambda$, 
under the assumption of time-independent division and death rates.

---

## Separation of Variables

To solve the PDE, we assume the solution can be expressed as:
$$
n(\tau, t) = \sum_\lambda N_\lambda(t) \pi_\lambda(\tau),
$$
where:
- $N_\lambda(t)$: Time-dependent population size associated with eigenvalue $\lambda$.
- $\pi_\lambda(\tau)$: Age distribution for the eigenvalue $\lambda$.

Substituting into the PDE and separating variables, we obtain:
$$
\frac{\pi_\lambda'(\tau)}{\pi_\lambda(\tau)} + \left(\gamma(\tau) + \delta(\tau)\right) = -\frac{N_\lambda'(t)}{N_\lambda(t)} = -\lambda.
$$

From this, we solve the time-dependent and age-dependent parts separately:
$$
\begin{aligned}
N_\lambda(t) &= N_\lambda(0) e^{\lambda t}, \\
\pi_\lambda(\tau) &= \pi_\lambda(0) e^{-\lambda \tau} e^{-\int_0^\tau \left(\gamma(s) + \delta(s)\right) \, ds}.
\end{aligned}
$$

The eigenvalue $\lambda$ determines the growth or decay rate of the population. It is obtained from the boundary condition:
$$
n(0, t) = 2 \int_0^\infty \gamma(\tau) n(\tau, t) \, d\tau.
$$

Substituting the expression for $n(\tau, t)$, we arrive at:
$$
\pi_\lambda(0) = 2 \int_0^\infty \gamma(\tau) \pi_\lambda(\tau) \, d\tau.
$$

---

## Deriving the Euler-Lotka Equation

To further simplify, we define the **division probability density function** $\phi(\tau)$ and the **death survival function** $\varphi(\tau)$ as follows:
1. Division rate as a hazard function:
   $$
   \gamma(\tau) = \frac{\phi(\tau)}{1 - \int_0^\tau \phi(s) \, ds}, \quad \phi(\tau) = \gamma(\tau) e^{-\int_0^\tau \gamma(s) \, ds}.
   $$
2. Death survival function:
   $$
   \varphi(\tau) = 2 e^{-\int_0^\tau \delta(s) \, ds}.
   $$

Combining these, the boundary condition reduces to the **Euler-Lotka equation**:
$$
1 = \int_0^\infty e^{-\lambda \tau} \phi(\tau) \varphi(\tau) \, d\tau,
$$
where:
- $e^{-\lambda \tau}$: Discount factor due to exponential population growth.
- $\phi(\tau)$: Probability density of division at age $\tau$.
- $\varphi(\tau)$: Probability of survival from death up to age $\tau$.

The equation can be solved numerically or analytically for $\lambda$, depending on the specific forms of $\gamma(\tau)$ and $\delta(\tau)$.

---

## Special Cases

### 1. Immortal Cells ($\delta(\tau) = 0$)

If cells do not die, the division rate is constant, $\gamma(\tau) = R$. The probability density function of division is:
$$
\phi(\tau) = R e^{-R \tau}, \quad \varphi(\tau) = 2.
$$

The Euler-Lotka equation becomes:
$$
1 = 2R \int_0^\infty e^{-(\lambda + R) \tau} \, d\tau.
$$
Evaluating the integral:
$$
1 = \frac{2R}{\lambda + R}.
$$
Solving for $\lambda$:
$$
\lambda = R.
$$
This result shows that the population growth rate equals the division rate when no cells die.

---

### 2. Normal Cells ($\delta(\tau) = D$)

If cells die at a constant rate $D$, the death survival function becomes:
$$
\varphi(\tau) = 2 e^{-D \tau}.
$$

The Euler-Lotka equation becomes:
$$
1 = 2R \int_0^\infty e^{-(\lambda + R + D) \tau} \, d\tau.
$$
Evaluating the integral:
$$
1 = \frac{2R}{\lambda + R + D}.
$$
Solving for $\lambda$:
$$
\lambda = R - D.
$$

### Interpretation

1. When $R > D$, the population grows at a rate $\lambda = R - D$.
2. When $R = D$, the population size remains constant ($\lambda = 0$).
3. When $R < D$, the population declines ($\lambda < 0$).