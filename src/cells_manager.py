from dataclasses import dataclass

@dataclass
class Cell:
    cell_id: int
    born_time: float
    life_time: float
    division_time: float
    is_alive: bool
    will_divide: bool

def init_immortal_cell(cell_id: int, born_time: float, division_time_func):
    """
    Initializes an immortal cell with its properties.

    Parameters:
    cell_id (int): Unique identifier for the cell.
    born_time (float): Time when the cell is created.
    division_time_func (function): Function to calculate the division time of the cell.

    Returns:
    Cell object: A dataclass object representing the cell.
    """
    division_time = born_time + division_time_func(born_time)

    return Cell(
        cell_id=cell_id,
        born_time=born_time,
        life_time=float("inf"),
        division_time=division_time,
        is_alive=True,
        will_divide=True
    )

def init_normal_cell(cell_id: int, born_time: float, life_time_func, division_time_func):
    """
    Initializes a cell with its properties.

    Parameters:
    cell_id (int): Unique identifier for the cell.
    born_time (float): Time when the cell is created.
    life_time_func (function): Function to calculate the lifetime of the cell.
    division_time_func (function): Function to calculate the division time of the cell.

    Returns:
    Cell object: A dataclass object representing the cell.
    """
    life_time = born_time + life_time_func(born_time)
    division_time = born_time + division_time_func(born_time)

    return Cell(
        cell_id=cell_id,
        born_time=born_time,
        life_time=life_time,
        division_time=division_time,
        is_alive=True,
        will_divide=division_time < life_time
    )

def deactivate_cell(cell: Cell):
    """
    Disactivates a cell by marking it as inactive.

    Parameters:
    cell (Cell): The cell object to be disactivated.
    """
    cell.is_alive = False
