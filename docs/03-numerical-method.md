# Numerical method

## Overview
This code simulates a **stochastic birth-death process**, where individual cells undergo division over time. The division process follows a probabilistic model, with division times sampled from a gamma distribution. The process includes the generation of new cells (birth) and the deactivation of parent cells post-division (death). The primary objective is to study the dynamics of this process, specifically the relationship between division times and the logarithm of cell count.

## Mathematical Framework

### 1. **Cell Representation**

Each cell is represented as a dataclass:

where:
- `id`: Unique identifier for the cell.

- `born_time`: The time $ t_{\text{born}} $  at which the cell was created (birth time).
- `life_time`: The time at which the cell will die.
- `division_time`: The time $ t_{\text{div}} $ at which the cell is expected to divide.
- `is_alive`: Boolean indicating whether the cell is active (`True`) or inactive (`False`).
- `will_divide`: Boolean indicating if the cell will divide before it dies (`True`) or not (`False`).

### 2. **Division Time Sampling**
The division time for a new cell is sampled from a **gamma distribution**:
$$
t_{\text{sample}} \sim \text{Gamma}(k, \theta),
$$
where:

* $ k = 5 $: Shape parameter.
* $ \theta = 1 $: Scale parameter.

The expected value and variance of the gamma distribution are:
$$
\mathbb{E}[t_{\text{sample}}] = k \theta, \quad \text{Var}[t_{\text{sample}}] = k \theta^2.
$$

### 3. **Simulation Algorithm**

The process begins with a single cell at $ t_{\text{born}} = 0 $. At each step:
1. Identify the cell with the earliest division time $ t_{\text{next}} $.
2. Divide the selected cell, creating two daughter cells.
3. Repeat the process for a fixed number of iterations.

### 4. **Analysis of Division Times**
The simulation outputs the division times of all cells. For analysis:

- Division times are sorted in ascending order:
  
  $$
  t_{\text{div}, 1}, t_{\text{div}, 2}, \dots, t_{\text{div}, N}
  $$
  
A linear regression is performed on the relationship between $ \log(N-1) $ (logarithm of rank) and $ t_{\text{div}} $.

#### Regression Model:
$$t_{\text{div}} = \beta \log(N-1) + \alpha$$

where:

- $\beta$: Slope (regression coefficient).
- $\alpha$: Intercept.

### 5. **Monte Carlo Simulation**
To study variability in the regression parameters:

- The simulation is repeated $ 1000 $ times.
- For each run, the regression coefficients $\beta$ and intercepts $\alpha$ are stored.

### 6. **Statistical Output**

The distributions of $ \beta $ and $ \alpha $ are analyzed:

- Histograms of $ \beta $ illustrate the variability in the growth rate of division times.
- A compressed NumPy file stores the coefficients and intercepts for further analysis.

## Mathematical Results

### Key Observations:
1. The stochastic birth-death process results in an exponentially increasing number of cells over time.
2. The relationship between division times $t_{\text{div}}$ and logarithm of rank $\log(N-1)$ is approximately linear for sufficiently large $N$, as suggested by the regression model.

### Regression Interpretation:
The slope $\beta$ reflects the rate of increase in division times as the population grows, while the intercept $ \alpha $ represents the baseline division time.

Analysis Method Overview
We analyze the stochastic birth-death process using linear regression to study the relationship between division times and logarithmic cell count. The regression model is given by:

$$
t_{\mathrm{div}}=\beta \log (N-1)+\alpha
$$

where:

* $t_{\text {div }}$ is the division time,
* $N$ is the total number of cells,
* $\beta$ (slope) represents the growth rate $k$,
* $\alpha$ (intercept) represents the effective initial population size parameter $b$.

We estimate $\beta$ and $\alpha$ using least squares regression, fitting the observed division times to the logarithm of cell count.


## Conclusion
This simulation provides a detailed mathematical model for understanding cell division dynamics in a stochastic setting. The use of gamma distributions for division times introduces variability, mimicking real biological systems. By analyzing the relationship between division times and cell count, the model offers insights into the temporal evolution of the system.
