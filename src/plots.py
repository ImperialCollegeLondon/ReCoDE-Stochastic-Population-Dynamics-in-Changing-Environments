from simulation import Simulation
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    sns.lmplot(x="time", y="log_population", data=data, height=8)
    plt.grid(alpha=0.5)
    plt.title("Log-Transformed Population Dynamics with Regression Line", fontsize=16)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Log(Number of Alive Cells)", fontsize=14)
    plt.tight_layout()
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
