from dataclasses import dataclass

@dataclass
class Cell:
    cell_id: int
    born_time: float
    life_time: float
    division_time: float
    is_alive: bool
    will_divide: bool

class CellsManager:
    def __init__(self):
        pass

    def init_immortal_cell(self, cell_id: int, born_time: float, division_time_func) -> Cell:
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

    def init_normal_cell(self, cell_id: int, born_time: float, life_time_func, division_time_func) -> Cell:
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

    def init_dividable_cell(self, cell_id: int, born_time: float, life_time_func, division_time_func):
        """
        Initializes a cell with its properties, allowing division only if lifetime is greater than division time.

        Parameters:
        cell_id (int): Unique identifier for the cell.
        born_time (float): Time when the cell is created.
        life_time_func (function): Function to calculate the lifetime of the cell.
        division_time_func (function): Function to calculate the division time of the cell.

        Returns:
        Cell object: A dataclass object representing the cell.
        """
        # try 100 times until the lifetime is greater than the division time
        for _ in range(100):
            cell = self.init_normal_cell(cell_id, born_time, life_time_func, division_time_func)
            if cell.life_time > cell.division_time:
                return cell
        raise RuntimeWarning("Failed to create cell with lifetime > division time. check the sampling functions.")
        return None


    def deactivate_cell(self, cell: Cell) -> None:
        """
        Disactivates a cell by marking it as inactive.

        Parameters:
        cell (Cell): The cell object to be disactivated.
        """
        cell.is_alive = False
