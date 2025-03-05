from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

@dataclass
class Cell:
    born_time: float
    life_time: float
    division_time: float
    is_alive: bool
    will_divide: bool

    @classmethod
    def init_immortal_cell(cls, born_time: float, division_time_func) -> Cell:
        """Initializes an immortal cell with its properties.

        Args:
            born_time: Time when the cell is created.
            division_time_func: Function to calculate the division time of the cell.

        Returns:
            A dataclass object representing the cell.
        """
        division_time = born_time + division_time_func(born_time)

        return cls(
            born_time=born_time,
            life_time=float("inf"),
            division_time=division_time,
            is_alive=True,
            will_divide=True
        )

    @classmethod
    def init_normal_cell(cls, born_time: float, life_time_func, division_time_func) -> Cell:
        """
        Initializes a cell with its properties.

        Parameters:
        born_time (float): Time when the cell is created.
        life_time_func (function): Function to calculate the lifetime of the cell.
        division_time_func (function): Function to calculate the division time of the cell.

        Returns:
        Cell object: A dataclass object representing the cell.
        """
        life_time = born_time + life_time_func(born_time)
        division_time = born_time + division_time_func(born_time)

        return cls(
            born_time=born_time,
            life_time=life_time,
            division_time=division_time,
            is_alive=True,
            will_divide=division_time < life_time
        )

    @classmethod
    def init_dividable_cell(cls, born_time: float, life_time_func, division_time_func) -> Cell:
        """
        Initializes a cell with its properties, allowing division only if lifetime is greater than division time.

        Parameters:
        born_time (float): Time when the cell is created.
        life_time_func (function): Function to calculate the lifetime of the cell.
        division_time_func (function): Function to calculate the division time of the cell.

        Returns:
        Cell object: A dataclass object representing the cell.
        """
        # try 100 times until the lifetime is greater than the division time
        for _ in range(100):
            cell = Cell.init_normal_cell(born_time, life_time_func, division_time_func)
            if cell.life_time > cell.division_time:
                return cell
        raise RuntimeWarning("Failed to create cell with lifetime > division time. check the sampling functions.")
        return None


def deactivate_cell(cell: Cell) -> None:
    """
    Disactivates a cell by marking it as inactive.

    Parameters:
    cell (Cell): The cell object to be disactivated.
    """
    cell.is_alive = False
