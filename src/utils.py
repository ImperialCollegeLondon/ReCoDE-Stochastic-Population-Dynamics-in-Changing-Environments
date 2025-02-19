import numpy as np
from scipy.stats import gamma
import numpy as np
from scipy.stats import gamma

def uniform_sample(born_time: float) -> float:
    """
    Generates a random division time sampled uniformly within a range.

    Args:
        born_time (float): The time the cell is born.

    Returns:
        float: The division time, sampled uniformly.
    """
    low = 5.0  # Minimum division time
    high = 15.0  # Maximum division time
    return np.random.uniform(low, high)

def gamma_sample(born_time: float, shape: float = 2.0, scale: float = 5.0) -> float:
    """
    Generates a random division time using the Gamma distribution.

    Args:
        born_time (float): The time the cell is born.
        shape (float): Shape parameter of the Gamma distribution. Default is 2.0.
        scale (float): Scale parameter of the Gamma distribution. Default is 5.0.

    Returns:
        float: The division time, sampled from a Gamma distribution.
    """
    return gamma.rvs(a=shape, scale=scale)

def sinusoidal_sample(born_time: float) -> float:
    """
    Generates a division time based on a sine wave pattern. This creates periodic
    variations in division times.

    Args:
        born_time (float): The time the cell is born.

    Returns:
        float: The division time, calculated as a function of the sine wave.
    """
    amplitude = 10.0  # Amplitude of the sine wave
    baseline = 15.0  # Baseline division time
    period = 20.0  # Period of the sine wave
    return born_time + baseline + amplitude * np.sin(2 * np.pi * born_time / period)

def fixed_lifetime(born_time: float, lifetime_constant: float = 1e4) -> float:
    """
    Defines a fixed lifetime for a cell.

    Args:
        born_time (float): The time the cell is born (unused).
        lifetime_constant (float): The constant lifetime value. Default is 1e4.

    Returns:
        float: The fixed lifetime of the cell.
    """
    return lifetime_constant

def exponential_lifetime(born_time: float, mean_lifetime: float = 10.0) -> float:
    """
    Generates a lifetime sampled from an exponential distribution.

    Args:
        born_time (float): The time the cell is born.
        mean_lifetime (float): The mean lifetime of the exponential distribution. Default is 10.0.

    Returns:
        float: The lifetime, sampled from an exponential distribution.
    """
    return np.random.exponential(mean_lifetime)

def cos_sample(born_time: float) -> float:
    """
    Generates a division time based on a cosine-based function for cyclic variations.
    Adds an offset to ensure positive division times.

    Args:
        born_time (float): The time the cell is born.

    Returns:
        float: The division time, determined by a cosine function with a positive offset.
    """
    amplitude = 10.0  # Amplitude of the cosine wave
    baseline = 15.0  # Baseline division time
    return baseline + amplitude * np.cos(born_time)


# Example usage for testing purposes:
if __name__ == "__main__":
    print("Uniform sample:", uniform_sample(0))
    print("Gamma sample:", gamma_sample(0))
    print("Sinusoidal sample:", sinusoidal_sample(0))
    print("Fixed lifetime:", fixed_lifetime(0))
    print("Exponential lifetime:", exponential_lifetime(0))
    print("Cosine sample:", cos_sample(0))
