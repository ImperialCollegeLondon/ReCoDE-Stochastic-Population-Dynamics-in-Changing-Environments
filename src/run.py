import numpy as np
import pandas as pd
from utils import cos_sample, exponential_lifetime, fixed_lifetime
from simulation import Simulation
from sklearn.linear_model import LinearRegression
from plots import plot_population_dynamics, log_population_regression, compare_multi_runs, plot_distribution

def set_seed(seed: int) -> None:
    """
    Sets the random seed for reproducibility.

    Args:
        seed (int): The seed value to set.
    """
    np.random.seed(seed)

def single_run(epoch: int, division_func: callable, lifetime_func: callable) -> Simulation:
    """
    Runs a single simulation and returns the Simulation object.

    Args:
        epoch (int): Number of steps to run the simulation.
        division_func (callable): Function to determine division times.
        lifetime_func (callable): Function to determine lifetime of cells.

    Returns:
        Simulation: The simulation object after running the epochs.
    """
    sim = Simulation(name="SingleRun", division_func=division_func, lifetime_func=lifetime_func)
    for _ in range(epoch):
        sim.run()
    return sim


def multi_run(epoch: int, num_runs: int, division_func: callable, lifetime_func: callable) -> list[Simulation]:
    """
    Runs multiple simulations and collects results.

    Args:
        epoch (int): Number of steps to run each simulation.
        num_runs (int): Number of simulations to run.
        division_func (callable): Function to determine division times.
        lifetime_func (callable): Function to determine lifetime of cells.

    Returns:
        list: List of Simulation objects from the runs.
    """
    sims = []
    for i in range(num_runs):
        sim = single_run(epoch, division_func, lifetime_func)
        sims.append(sim)
    return sims


def extract_regression_results(simulations):
    """
    Performs linear regression on the log-transformed population dynamics
    for a list of simulations and extracts the slope and intercept.

    Args:
        simulations (list[Simulation]): List of simulation objects.

    Returns:
        pd.DataFrame: DataFrame containing valid regression slopes and intercepts.
    """
    results = []
    for sim in simulations:
        # Extract time and population data
        time_population_data = np.array(sim.get_time_population_curve())
        times = time_population_data[:, 0]
        populations = time_population_data[:, 1]

        # Exclude invalid or insufficient data
        if len(times) < 2 or np.any(populations <= 0):
            continue  # Skip invalid simulations

        # Log-transform the population data
        log_population = np.log(populations)

        # Perform linear regression
        regr = LinearRegression()
        times_reshaped = times.reshape(-1, 1)
        regr.fit(times_reshaped, log_population)
        slope = regr.coef_[0]
        intercept = regr.intercept_

        # Append the regression results
        results.append((slope, intercept))

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results, columns=['coef', 'intercept'])
    return results_df


# Main execution
if __name__ == "__main__":
    # Define division and lifetime functions
    division_func = lambda x: exponential_lifetime(x, mean_lifetime=5.0)
    lifetime_func = lambda x: exponential_lifetime(x, mean_lifetime=15.0)

    # Run a single simulation
    sim = single_run(epoch=200, division_func=division_func, lifetime_func=lifetime_func)

    # Visualize single simulation
    plot_population_dynamics(sim)
    log_population_regression(sim)

    # Run multiple simulations
    sims = multi_run(epoch=50, num_runs=40, division_func=division_func, lifetime_func=lifetime_func)

    # Compare results from multiple runs
    compare_multi_runs(sims)

    data_independent = extract_regression_results(sims)

    # Plot the distributions for coefficients
    plot_distribution(data_independent, column='coef', binwidth=0.01, color='coral',
                      xlabel='Coefficient', ylabel='Frequency',
                      title='Distribution of Regression Coefficients')

    # Plot the distributions for intercepts
    plot_distribution(data_independent, column='intercept', binwidth=0.1, color='teal',
                      xlabel='Intercept', ylabel='Frequency',
                      title='Distribution of Regression Intercepts')