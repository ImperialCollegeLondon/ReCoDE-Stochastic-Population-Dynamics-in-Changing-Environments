from cells import *
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

class Game:
    """
    Simulates the lifecycle of cells, including division and death, and tracks population dynamics.
    """

    def __init__(self, name, s_func, l_func):
        """
        Initializes the simulation with a single cell and the specified functions for division time and lifetime.

        Parameters:
            name (str): Name of the simulation.
            s_func (function): Function to calculate the division time of a cell.
            l_func (function): Function to calculate the lifetime of a cell.
        """
        first_cell = init_cell(0, 0, l_func(0), s_func(0))
        self.name = name
        self.cells = [first_cell]  # List of all cells
        self.log = []  # Event log
        self.s_func = s_func  # Function for division time
        self.l_func = l_func  # Function for lifetime
        self.epoch = 0  # Simulation step counter

    def sget(self, time):
        """Calculates the absolute division time given a starting time."""
        return time + self.s_func(time)

    def lget(self, time):
        """Calculates the absolute lifetime given a starting time."""
        return time + self.l_func(time)

    def divide(self, cell):
        """
        Handles the division of a cell by deactivating it and creating two new daughter cells.

        Parameters:
            cell (Cell): The cell that is dividing.
        """
        disactivate_cell(cell)

        division_time = cell.division_time
        new_cell1 = init_cell(
            cell_id=len(self.cells),
            born_time=division_time,
            life_time=self.lget(division_time),
            division_time=self.sget(division_time)
        )
        new_cell2 = init_cell(
            cell_id=len(self.cells) + 1,
            born_time=division_time,
            life_time=self.lget(division_time),
            division_time=self.sget(division_time)
        )
        self.cells.extend([new_cell1, new_cell2])

    def log_event(self, time, cell_id, operation):
        """
        Logs an event (division or death) in the simulation.

        Parameters:
            time (float): The time at which the event occurred.
            cell_id (int): The ID of the cell involved in the event.
            operation (str): The type of event ('division' or 'death').
        """
        # todo
        self.log.append({
            "time": time,
            "cell_id": cell_id,
            "operation": operation
        })

    def find_next_event(self):
        """
        Finds the next event (division or death) and the cell associated with it.

        Returns:
            tuple: (time of the event, cell involved, type of event).
        """
        next_time = float("inf")
        next_cell = None
        operation = "pass"

        for cell in self.cells:
            if not cell.is_alive:
                continue

            # Check death time
            if cell.life_time < next_time:
                next_time = cell.life_time
                next_cell = cell
                operation = "death"

            # Check division time
            if cell.will_divide and cell.division_time < next_time:
                next_time = cell.division_time
                next_cell = cell
                operation = "division"

        return next_time, next_cell, operation

    def run(self):
        """Executes one step of the simulation by processing the next event."""
        self.epoch += 1
        next_time, next_cell, operation = self.find_next_event()
        if operation == "pass":
            return  # No events left to process
        if operation == "death":
            disactivate_cell(next_cell)
            self.log_event(next_time, next_cell.cell_id, "death")
        elif operation == "division":
            self.divide(next_cell)
            self.log_event(next_time, next_cell.cell_id, "division")

