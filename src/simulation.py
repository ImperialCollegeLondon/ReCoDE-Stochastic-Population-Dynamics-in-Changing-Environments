from cell import deactivate_cell, Cell
from typing import Callable, List, Tuple, Dict

class Simulation:
    """
    Simulates the lifecycle of cells, including division and death, and tracks population dynamics.
    """

    def __init__(self, name: str, division_func: Callable[[float], float], lifetime_func: Callable[[float], float]):
        """
        Initializes the simulation with a single cell and the specified functions for division time and lifetime.

        Args:
            name (str): Name of the simulation.
            division_func (Callable[[float], float]): Function to calculate the division time of a cell.
            lifetime_func (Callable[[float], float]): Function to calculate the lifetime of a cell.
        """
        first_cell = Cell.init_normal_cell(0, lifetime_func, division_func)
        self.name: str = name
        self.live_cells: List[Cell] = [first_cell]  # List of living cells
        self.dead_cells: List[Cell] = [] # List of dead cells
        self.log: List[Dict[str, object]] = []  # Event log
        self.division_func: Callable[[float], float] = division_func
        self.lifetime_func: Callable[[float], float] = lifetime_func
        self.epoch: int = 0  # Simulation step counter

    def sget(self, time: float) -> float:
        """
        Calculates the absolute division time given a starting time.

        Args:
            time (float): The starting time.

        Returns:
            float: The absolute division time.
        """
        return time + self.division_func(time)

    def lget(self, time: float) -> float:
        """
        Calculates the absolute lifetime given a starting time.

        Args:
            time (float): The starting time.

        Returns:
            float: The absolute lifetime.
        """
        return time + self.lifetime_func(time)

    def divide(self, i_next_cell: int, cell: Cell) -> None:
        """
        Handles the division of a cell by deactivating it and creating two new daughter cells.

        Args:
            i_next_cell (int): Index of the cell in the list of live cells.
            cell (object): The cell that is dividing.
        """
        deactivate_cell(cell)
        self.dead_cells.append(self.live_cells.pop(i_next_cell))
        division_time = cell.division_time

        new_cell1 = Cell.init_normal_cell(
            born_time=division_time,
            life_time_func=self.lifetime_func,
            division_time_func=self.division_func
        )

        new_cell2 = Cell.init_normal_cell(
            born_time=division_time,
            life_time_func=self.lifetime_func,
            division_time_func=self.division_func
        )

        self.live_cells.extend([new_cell1, new_cell2])

    def log_event(self, time: float, operation: str) -> None:
        """
        Logs an event (division or death) in the simulation.

        Args:
            time (float): The time at which the event occurred.
            operation (str): The type of event ('division' or 'death').
        """
        self.log.append({
            "time": time,
            "operation": operation
        })

    def find_next_event(self) -> Tuple[float, Cell, str]:
        """
        Finds the next event (division or death) and the cell associated with it.

        Returns:
            Tuple[float, int, Cell, str]: The time of the event, the index of the cell involved,
            the cell involved, and the type of event.
        """
        next_time = float("inf")
        i_next_cell = None
        next_cell = None
        operation = "pass"

        for i_cell_live, cell in enumerate(self.live_cells):
            # Check death time
            if cell.life_time < next_time:
                next_time = cell.life_time
                i_next_cell = i_cell_live
                next_cell = cell
                operation = "death"

            # Check division time
            if cell.will_divide and cell.division_time < next_time:
                next_time = cell.division_time
                i_next_cell = i_cell_live
                next_cell = cell
                operation = "division"

        return next_time, i_next_cell, next_cell, operation

    def run(self) -> None:
        """
        Executes one step of the simulation by processing the next event.
        """
        self.epoch += 1
        next_time, i_next_cell, next_cell, operation = self.find_next_event()
        if operation == "pass":
            return  # No events left to process
        if operation == "death":
            deactivate_cell(next_cell)
            self.dead_cells.append(self.live_cells.pop(i_next_cell))
            self.log_event(next_time, "death")
        elif operation == "division":
            self.divide(i_next_cell, next_cell)
            self.log_event(next_time, "division")

    def get_time_population_curve(self) -> List[List[float]]:
        """
        Generates the time-population curve from the simulation log.

        Returns:
            List[List[float]]: A list of [time, population] pairs.
        """
        curve = [[0, 1]]  # Initial population
        population = 1
        for event in self.log:
            if event['operation'] == 'division':
                population += 1
                curve.append([event['time'], population])
            elif event['operation'] == 'death':
                population -= 1
                curve.append([event['time'], population])
        return curve
