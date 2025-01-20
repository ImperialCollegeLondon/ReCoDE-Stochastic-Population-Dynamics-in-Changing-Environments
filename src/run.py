import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils import cos_sample, exponential_lifetime, fixed_lifetime
from simulation import Simulation
from sklearn.linear_model import LinearRegression

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


def plot_population_dynamics(sim: Simulation) -> None:
    """
    Plots the number of alive cells over time for a single simulation.

    Args:
        sim (Simulation): The simulation object containing the results.
    """
    # Extract data
    time_population_data = np.array(sim.get_time_population_curve())
    times = time_population_data[:, 0]
    populations = time_population_data[:, 1]

    # Plot
    plt.figure(figsize=(14, 8))
    plt.plot(times, populations, 'o--', label="Population Dynamics")
    plt.grid(alpha=0.3)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Number of Alive Cells", fontsize=14)
    plt.title("Population Dynamics Over Time", fontsize=16)
    plt.legend(fontsize=12)
    plt.show()


def log_population_regression(sim: Simulation) -> None:
    """
    Performs log regression on the population dynamics and visualizes the results.

    Args:
        sim (Simulation): The simulation object containing the results.
    """
    # Extract data
    time_population_data = np.array(sim.get_time_population_curve())
    times = time_population_data[:, 0]
    populations = time_population_data[:, 1]

    # Log transform the population data
    log_population = np.log(populations)

    # Create a DataFrame for seaborn
    data = pd.DataFrame({"time": times, "log_population": log_population})

    # Plot
    plt.figure(figsize=(16, 9))
    sns.lmplot(x="time", y="log_population", data=data, height=8)
    plt.grid(alpha=0.5)
    plt.title("Log-Transformed Population Dynamics with Regression Line", fontsize=16)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Log(Number of Alive Cells)", fontsize=14)
    plt.show()


def compare_multi_runs(simulations: list[Simulation]) -> None:
    """
    Compares the population dynamics from multiple simulation runs.

    Args:
        simulations (list): List of Simulation objects.
    """
    plt.figure(figsize=(14, 8))

    for i, sim in enumerate(simulations):
        # Extract data
        time_population_data = np.array(sim.get_time_population_curve())
        times = time_population_data[:, 0]
        populations = time_population_data[:, 1]

        # Plot
        plt.plot(times, populations, label=f"Run {i + 1}")

    plt.grid(alpha=0.3)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Number of Alive Cells", fontsize=14)
    plt.title("Comparison of Population Dynamics Across Runs", fontsize=16)
    plt.legend(fontsize=12)
    plt.show()

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
def plot_distribution(data, column, binwidth, color, xlabel, ylabel, title):
    """
    Plots the distribution of a specified column in the DataFrame.

    Args:
        data (pd.DataFrame): Data containing the column to be plotted.
        column (str): Column name to plot.
        binwidth (float): Bin width for histogram.
        color (str): Color for the histogram.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(10, 8))
    sns.histplot(data, x=column, binwidth=binwidth, kde=True, color=color)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)
    plt.grid(alpha=0.5)
    plt.show()

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