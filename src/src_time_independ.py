import numpy as np
import matplotlib.pyplot as plt

def init_cell(cell_id, born_time, expected_division_time, is_alive):
    """
    Initializes a cell with its properties.

    Parameters:
    cell_id (int): Unique identifier for the cell.
    born_time (float): Time when the cell is created.
    expected_division_time (float): Time at which the cell is expected to divide.
    is_alive (bool): Status indicating if the cell is active/alive.

    Returns:
    list: A list representing the cell [id, born_time, division_time, is_alive].
    """
    return [cell_id, born_time, expected_division_time, is_alive]


def time_independent_sample():
    """
    Generates a random sample for the division time of a cell using a gamma distribution.

    Returns:
    float: A random sample representing the division time.
    """
    x = np.random.gamma(5, 1)  # Shape=5, Scale=1
    return x


def time_independent_divise(cell_list, cell_id):
    """
    Handles the division of a specific cell, creating two new cells.

    Parameters:
    cell_list (list): List of all cells.
    cell_id (int): ID of the cell to be divided.

    Behavior:
    - Marks the parent cell as inactive (`is_alive = False`).
    - Creates two new daughter cells with updated IDs and division times.
    """
    # Find the target cell to divide
    target_cell = cell_list[cell_id]

    # Deactivate the parent cell
    target_cell[3] = False

    # Generate two new cells
    N = len(cell_list)
    new_cell1 = init_cell(N, target_cell[2], target_cell[2] + time_independent_sample(), True)
    new_cell2 = init_cell(N + 1, target_cell[2], target_cell[2] + time_independent_sample(), True)

    # Append the new cells to the cell list
    cell_list.append(new_cell1)
    cell_list.append(new_cell2)


def find_next_divise_cell(cell_list):
    """
    Identifies the next cell to divide based on the earliest division time.

    Parameters:
    cell_list (list): List of all cells.

    Returns:
    int: The ID of the cell with the earliest division time.
    """
    minimal = np.inf  # Initialize with infinity for comparison
    cell_id = -1      # Default cell ID if no cell is found

    # Iterate over cells to find the one with the earliest division time
    for cell in cell_list:
        if cell[3]:  # Only consider active cells
            if cell[2] <= minimal:
                minimal = cell[2]
                cell_id = cell[0]

    return cell_id


def time_independent_run(cell_list):
    """
    Executes one step of the simulation: finds the next cell to divide and performs division.

    Parameters:
    cell_list (list): List of all cells.

    Returns:
    list: Updated list of cells after the division.
    """
    # Find the next cell to divide
    next_divise_cell_id = find_next_divise_cell(cell_list)

    # Perform division for the identified cell
    time_independent_divise(cell_list, next_divise_cell_id)

    return cell_list


def time_independent_main():
    """
    Main simulation function to model cell division.

    Behavior:
    - Initializes the simulation with a single cell.
    - Runs the division process for a fixed number of iterations (600).
    - Prints the state of the cell list for the first 5 iterations for debugging.

    Returns:
    list: The final list of cells after all iterations.
    """
    # Initialize the cell list with the first cell
    cell_list = []
    first_cell = init_cell(0, 0, time_independent_sample(), True)
    cell_list.append(first_cell)

    # Run the simulation for 600 iterations
    for _ in range(600):
        if _ < 5:  # Print the cell list for the first 5 iterations
            print(cell_list)

        # Execute one step of the simulation
        time_independent_run(cell_list)

    return cell_list


# Example usage:
# Run the simulation and observe the results
if __name__ == "__main__":
    final_cell_list = time_independent_main()

    # Print the total number of cells and a sample cell for analysis
    print("Total cells:", len(final_cell_list))
    print("Sample cell:", final_cell_list[0])  # Details of the first cell
