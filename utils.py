from scipy.stats import gamma
import numpy as np

def cos_sample(born_time):
    """
    Generates a random division time using a custom distribution.
    The probability density is defined by a sine-based gamma function.
    """

    def gamma(a, b):
        return 5 * np.sin(a + b) + 5

    gamma_max = 10  # Maximum value of gamma for rejection sampling
    tau_star = 0

    while True:
        u1 = np.random.uniform(0, 1)  # Uniform random variable
        tau_star -= np.log(u1) / gamma_max
        u2 = np.random.uniform(0, 1)
        if u2 <= gamma(tau_star, born_time + tau_star) / gamma_max:
            break

    return tau_star

def lifetime(time):
    """Defines the lifetime of a cell. Currently returns a large constant."""
    return 1e4