from cells_manage import init_normal_cell, deactivate_cell

class Simulation:
    """
    Simulates the lifecycle of cells, including division and death, and tracks population dynamics.
    """

    def __init__(self, name, division_func, lifetime_func):
        """
        Initializes the simulation with a single cell and the specified functions for division time and lifetime.

        Parameters:
            name (str): Name of the simulation.
            division_func (function): Function to calculate the division time of a cell.
            lifetime_func (function): Function to calculate the lifetime of a cell.
        """
        first_cell = init_normal_cell(0, 0, lifetime_func, division_func)
        self.name = name
        self.cells = [first_cell]  # List of all cells
        self.log = []  # Event log
        self.division_func = division_func  # Function for division time
        self.lifetime_func = lifetime_func  # Function for lifetime
        self.epoch = 0  # Simulation step counter

    def sget(self, time):
        """Calculates the absolute division time given a starting time."""
        return time + self.division_func(time)

    def lget(self, time):
        """Calculates the absolute lifetime given a starting time."""
        return time + self.lifetime_func(time)

    def divide(self, cell):
        """
        Handles the division of a cell by deactivating it and creating two new daughter cells.

        Parameters:
            cell (Cell): The cell that is dividing.
        """
        deactivate_cell(cell)
        division_time = cell.division_time

        new_cell1 = init_normal_cell(
            cell_id=len(self.cells),
            born_time=division_time,
            life_time_func=self.lifetime_func,
            division_time_func=self.division_func
        )

        new_cell2 = init_normal_cell(
            cell_id=len(self.cells) + 1,
            born_time=division_time,
            life_time_func=self.lifetime_func,
            division_time_func=self.division_func
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
            deactivate_cell(next_cell)
            self.log_event(next_time, next_cell.cell_id, "death")
        elif operation == "division":
            self.divide(next_cell)
            self.log_event(next_time, next_cell.cell_id, "division")

