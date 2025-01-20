# Mathematical Introduction to the Simulation Method

To model the stochastic dynamics of cell populations under time-dependent division and death rates, we require a rigorous mathematical framework. Here, we address the challenges and methods used to simulate such systems in continuous time.

### Stochastic Nature of Events

The division and death processes are modeled as independent Poisson processes with time-varying rates:
- Division rate: $\gamma(\tau, t)$, dependent on cell age $\tau$ and time $t$.
- Death rate: $\delta(\tau, t)$, also dependent on $\tau$ and $t$.

For a cell born at time $t_i$, the probability density of the next division or death event at time $t$ is given by:
$$
P_{\text{event}}(t) = \left[\gamma(\tau, t) + \delta(\tau, t)\right] e^{-\int_{t_i}^{t} \left[\gamma(\tau, s) + \delta(\tau, s)\right] \, ds},
$$
where $\tau = t - t_i$. The actual event (division or death) is determined by comparing $\gamma(\tau, t)$ and $\delta(\tau, t)$ at the sampled event time.

### Challenges in Time-Dependent Environments

1. **Non-Constant Intensity Functions:** In time-dependent environments, rates $\gamma(\tau, t)$ and $\delta(\tau, t)$ vary continuously, necessitating dynamic sampling algorithms.
2. **Continuous-Time Events:** Unlike discrete simulations, events occur at irregular intervals sampled from exponential distributions with non-uniform rates.
3. **Event Selection:** For each cell, the next event is determined by comparing division and death times, adding complexity to the simulation.

### Thinning Method for Time-Dependent Rates

To handle non-constant rates, we employ the **thinning method**, which generates event times for inhomogeneous Poisson processes.

1. **Identify Maximum Rate:**
   Compute $\gamma_{\max}$, the upper bound of $\gamma(\tau, t)$ over the relevant time interval $[t_i, T]$:
   $$
   \gamma_{\max} \geq \gamma(\tau, t) \quad \forall \, t \in [t_i, T].
   $$

2. **Sample Candidate Event Time:**
   Propose a time $\tau^*$ sampled from an exponential distribution with rate $\gamma_{\max}$:
   $$
   \tau^* = -\frac{1}{\gamma_{\max}} \ln(U_1), \quad U_1 \sim \text{Uniform}(0, 1).
   $$

3. **Acceptance-Rejection Step:**
   Accept $\tau^*$ as the next event time if:
   $$
   U_2 < \frac{\gamma(\tau^*, t_i + \tau^*)}{\gamma_{\max}}, \quad U_2 \sim \text{Uniform}(0, 1).
   $$
   Otherwise, repeat the sampling process.

4. **Determine Event Type:**
   At $\tau^*$, compare $\gamma(\tau^*, t_i + \tau^*)$ and $\delta(\tau^*, t_i + \tau^*)$ to decide whether the event is a division or a death.

### Incorporating Death Rates

To include death rates, the algorithm samples both the division and death times for each cell:
- Compute the time until the next event, $\tau_{\text{event}} = \min(\tau_{\text{division}}, \tau_{\text{death}})$.
- If $\tau_{\text{event}} = \tau_{\text{division}}$, the cell divides; otherwise, it dies.

Newly created cells are treated as independent entities, with their division and death times sampled afresh.

### Simulation Goals

The simulation evaluates the population growth rate $k$ and the effective initial population size parameter $b$ across thousands of events. By comparing time-dependent and time-independent environments, we study the impact of oscillatory rates and their periods on long-term population behavior. 

This rigorous stochastic framework allows us to model continuous-time dynamics accurately, despite the computational complexity.