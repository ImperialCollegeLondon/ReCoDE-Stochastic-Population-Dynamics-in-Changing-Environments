import numpy as np
from typing import Callable, List, Optional

def thinning_method(
    intensity_func: Callable[[float], float],
    gamma_max: float,
    start_time: float = 0,
    end_time: float = float('inf')
) -> List[float]:
    """
    Simulates event times for an inhomogeneous Poisson process using the thinning method.

    Args:
        intensity_func (Callable[[float], float]): Intensity function γ(t), defining the rate of events at time t.
        gamma_max (float): Maximum value of γ(t), used for rejection sampling.
        start_time (float): Start time of the simulation. Default is 0.
        end_time (float): End time of the simulation. Default is infinity.

    Returns:
        List[float]: A list of event times sampled from the process.
    """
    current_time = start_time
    event_times = []  # List to store accepted event times

    while current_time < end_time:
        # Generate a candidate time increment using exponential distribution
        u1 = np.random.uniform(0, 1)
        delta_time = -np.log(u1) / gamma_max
        candidate_time = current_time + delta_time

        if candidate_time >= end_time:
            break  # Stop if the candidate time exceeds the end time

        # Evaluate the intensity function at the candidate time
        intensity_value = intensity_func(candidate_time)

        # Acceptance-rejection step
        u2 = np.random.uniform(0, 1)
        if u2 <= intensity_value / gamma_max:
            event_times.append(candidate_time)  # Accept the candidate time
            current_time = candidate_time  # Update current time
        else:
            current_time = candidate_time  # Move to next candidate time

    return event_times

def create_sampling_function(
    intensity_func: Callable[[float], float],
    gamma_max: float
) -> Callable[[float], Optional[float]]:
    """
    Creates a sampling function based on the thinning method for a given intensity function.

    Args:
        intensity_func (Callable[[float], float]): Intensity function γ(t), defining the rate of events at time t.
        gamma_max (float): Maximum value of γ(t), used for rejection sampling.

    Returns:
        Callable[[float], Optional[float]]: A sampling function that takes a 'born_time' as input
            and returns a sampled event time or None if no event is generated.
    """
    def sampling_function(born_time: float) -> Optional[float]:
        """
        Samples an event time based on the intensity function, starting from the given born_time.

        Args:
            born_time (float): The starting time for the sampling.

        Returns:
            Optional[float]: A sampled event time, or None if no event is generated.
        """
        # Use thinning_method to generate a single event time
        events = thinning_method(
            intensity_func=lambda t: intensity_func(t - born_time),  # Adjust intensity for born_time
            gamma_max=gamma_max,
            start_time=born_time,
            end_time=float('inf')  # No explicit end time for single sampling
        )
        return events[0] if events else None  # Return the first sampled event or None if no event

    return sampling_function

if __name__ == "__main__":
    def constant_intensity(t):
        return 5.0

    def sinusoidal_intensity(t):
        return 5 * np.sin(2 * np.pi * t / 10) + 5

    def exponential_decay_intensity(t):
        return 10 * np.exp(-t / 10)

    # Create a sampling function for a sinusoidal intensity
    sampling_func = create_sampling_function(
        intensity_func=sinusoidal_intensity,
        gamma_max=10.0  # Maximum value of the sinusoidal intensity
    )

    # Sample event times for different born times
    for born_time in [0, 5, 10, 15]:
        sampled_time = sampling_func(born_time)
        print(f"Born time: {born_time}, Sampled event time: {sampled_time}")
