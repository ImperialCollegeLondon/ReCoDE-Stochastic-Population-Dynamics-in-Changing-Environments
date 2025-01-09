from utils import cos_sample, exponential_lifetime
from src_time_independ import Simulation

if __name__ == "__main__":

    division_func = cos_sample
    lifetime_func = exponential_lifetime

    game = Simulation(name=f"exp_{0}", division_func=division_func, lifetime_func=lifetime_func)

    for _ in range(100):
        game.run()

    print("Simulation completed.")
