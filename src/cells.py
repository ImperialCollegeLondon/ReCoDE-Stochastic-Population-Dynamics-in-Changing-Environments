from dataclasses import dataclass

@dataclass
class Cell:
    cell_id: int
    born_time: float
    life_time: float
    division_time: float
    is_alive: bool
    will_divide: bool


def init_cell(cell_id, born_time, life_time, division_time):
    """
    Initializes a cell with its properties.

    Parameters:
    cell_id (int): Unique identifier for the cell.
    born_time (float): Time when the cell is created.
    life_time (float): Total lifespan of the cell.
    division_time (float): Time at which the cell is expected to divide.

    Returns:
    Cell object: A dataclass object representing the cell.
    """
    return Cell(
        cell_id=cell_id,
        born_time=born_time,
        life_time=life_time,
        division_time=division_time,
        is_alive=True,
        will_divide=division_time < life_time
    )

def disactivate_cell(cell: Cell):
    """
    Disactivates a cell by marking it as inactive.

    Parameters:
    cell (Cell): The cell object to be disactivated.
    """
    cell.is_alive = False
