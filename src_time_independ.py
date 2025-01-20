import numpy as np
import matplotlib.pyplot as plt

def init_cell(cell_id, born_time, expected_division_time, is_alive):
    """
    id: index
    t: born time
    division time: time take to divise
    is_alive: bool
    """
    return [cell_id, born_time, expected_division_time, is_alive]


def time_independent_sample():
    x = np.random.gamma(5,1)
    # x = np.random.exponential(0.2)
    return x


def time_independent_divise(cell_list, cell_id):
    target_cell = cell_list[cell_id]
    # 1. disactive cell with cell id
    target_cell[3] = False
    # 2. add two new cells
    N = len(cell_list)
    new_cell1 = init_cell(N, target_cell[2], target_cell[2]+time_independent_sample(), True)
    new_cell2 = init_cell(N+1, target_cell[2], target_cell[2]+time_independent_sample(), True)
    cell_list.append(new_cell1)
    cell_list.append(new_cell2)


def find_next_divise_cell(cell_list):
    minimal = np.inf
    cell_id = -1
    for cell in cell_list:
        if cell[3] == True:
            if cell[2]<=minimal:
                minimal = cell[2]
                cell_id = cell[0]
    return cell_id


def time_independent_run(cell_list):
    next_divise_cell_id = find_next_divise_cell(cell_list)
    time_independent_divise(cell_list, next_divise_cell_id)
    return cell_list


def time_independent_main():
    cell_list = []
    first_cell = init_cell(0, 0, time_independent_sample(), True)
    cell_list.append(first_cell)

    for _ in range(600):
        if _ < 5:
            print(cell_list)
        time_independent_run(cell_list)

    return cell_list


