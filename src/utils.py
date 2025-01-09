import numpy as np
from scipy.stats import gamma

def uniform_sample(born_time):
    """
    Generates a random division time sampled uniformly within a range.

    Parameters:
        born_time (float): The time the cell is born.

    Returns:
        float: The division time, sampled uniformly.
    """
    low = 5.0  # Minimum division time
    high = 15.0  # Maximum division time
    return born_time + np.random.uniform(low, high)


def gamma_sample(born_time, shape=2.0, scale=5.0):
    """
    Generates a random division time using the Gamma distribution.

    Parameters:
        born_time (float): The time the cell is born.
        shape (float): Shape parameter of the Gamma distribution (default is 2.0).
        scale (float): Scale parameter of the Gamma distribution (default is 5.0).

    Returns:
        float: The division time, sampled from a Gamma distribution.
    """
    return born_time + gamma.rvs(a=shape, scale=scale)


def sinusoidal_sample(born_time):
    """
    Generates a division time based on a sine wave pattern.
    This creates periodic variations in division times.

    Parameters:
        born_time (float): The time the cell is born.

    Returns:
        float: The division time, calculated as a function of the sine wave.
    """
    amplitude = 10.0  # Amplitude of the sine wave
    baseline = 15.0  # Baseline division time
    period = 20.0  # Period of the sine wave
    return born_time + baseline + amplitude * np.sin(2 * np.pi * born_time / period)


def fixed_lifetime(born_time, lifetime_constant=1e4):
    """
    Defines a fixed lifetime for a cell.

    Parameters:
        born_time (float): The time the cell is born (unused here).
        lifetime_constant (float): The constant lifetime value (default is 1e4).

    Returns:
        float: The fixed lifetime of the cell.
    """
    return born_time + lifetime_constant


def exponential_lifetime(born_time, mean_lifetime=50.0):
    """
    Generates a lifetime sampled from an exponential distribution.

    Parameters:
        born_time (float): The time the cell is born.
        mean_lifetime (float): The mean lifetime of the exponential distribution (default is 50.0).

    Returns:
        float: The lifetime, sampled from an exponential distribution.
    """
    return born_time + np.random.exponential(mean_lifetime)


def cos_sample(born_time):
    """
    Generates a division time based on a cosine-based function for cyclic variations.
    Note: Returns a positive value by adding an offset to ensure valid division times.

    Parameters:
        born_time (float): The time the cell is born.

    Returns:
        float: The division time, determined by a cosine function with a positive offset.
    """
    amplitude = 10.0  # Amplitude of the cosine wave
    baseline = 15.0  # Baseline division time
    return born_time + baseline + amplitude * np.cos(born_time)


# Example usage for testing purposes:
if __name__ == "__main__":
    print("Uniform sample:", uniform_sample(0))
    print("Gamma sample:", gamma_sample(0))
    print("Sinusoidal sample:", sinusoidal_sample(0))
    print("Fixed lifetime:", fixed_lifetime(0))
    print("Exponential lifetime:", exponential_lifetime(0))
    print("Cosine sample:", cos_sample(0))
