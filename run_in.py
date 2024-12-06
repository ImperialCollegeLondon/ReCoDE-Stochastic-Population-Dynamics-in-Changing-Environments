from cells import *
from utils import *
from src_time_independ import Game

if __name__ == "__main__":
    def division_time_func(time):
        return cos_sample(time)

    def life_time_func(time):
        return lifetime(time)

    game = Game(name="CellSimulation", s_func=division_time_func, l_func=life_time_func)

    for _ in range(100):
        game.run()

    print("Simulation completed.")
