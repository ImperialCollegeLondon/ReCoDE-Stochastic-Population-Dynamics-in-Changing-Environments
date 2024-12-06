from scipy.stats import gamma
import numpy as np

def cos_sample(born_time):
    """
    Generates a random division time using a custom distribution.
    The probability density is defined by a sine-based gamma function.
    """
    # todo
    return 1e1 * np.sin(born_time) + 1e1

def lifetime(time):
    """Defines the lifetime of a cell. Currently returns a large constant."""
    return 1e4