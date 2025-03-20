# Cell Population Dynamics in Continuous Time Domain

## Description

This project explores the mathematical modeling of cell population dynamics using the McKendrick–Von Foerster equation. The focus is on understanding the time-independent case where cell division and death rates depend on the cell's age.

## Learning Outcomes

- Understand the McKendrick–Von Foerster equation for population dynamics.
- Apply separation of variables to solve partial differential equations.
- Derive and interpret the Euler-Lotka equation for population growth rates.

## Requirements

### Academic

- Basic knowledge of differential equations and mathematical modeling.
- Familiarity with population dynamics concepts.

### System

- Python 3.11 or newer
- MkDocs for documentation generation
- Miniconda (recommended for managing dependencies)

## Getting Started

1. Clone the repository and navigate to the project directory.
2. Set up a virtual environment and install the required dependencies:
   ```sh
   conda create --name cell-population-dynamics python=3.11
   conda activate cell-population-dynamics
   pip install -r requirements.txt
   ```
   
## Project Structure

```log
.
├── docs
├── notebooks
├── src
│   ├── __init__.py
|   ├── cells_manager.py   # Cell population manager
|   ├── plots.py           # Plotting functions
|   ├── run.py             # Main script to run the simulation
|   ├── simulation.py      # Core simulation logic
│   └── utils.py           # Utility functions
├── mkdocs.yml
├── requirements.txt
└── README.md
```

<!-- Change this to your License. Make sure you have added the file on GitHub -->


## MkDocs Documentation
To generate local documentation, run the following command:

```sh
mkdocs serve
```


## License

This project is licensed under the [BSD-3-Clause license](LICENSE.md)
