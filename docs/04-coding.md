# Coding techniques and design patterns

## Design Patterns Used in the Simulation

The simulation code for cell population dynamics employs several design patterns to enhance modularity, extensibility, and maintainability. Here are the key design patterns used in the implementation:

### 1. Factory Method Pattern (Cell Initialization)
- The Cell_Manager act as factory methods to create/disactive different types of cell objects.
- Instead of directly instantiating Cell objects in multiple places, these factory functions ensure consistent initialization logic.
### 2. Strategy Pattern (Customizable Functions for Lifetime and Division)
- The simulation class takes `division_func` and `lifetime_func` as parameters.
- This allows the user to plug in different strategies for computing division and lifetime, making the simulation flexible without modifying core logic.
- Implemented using lambda functions of the distribution which do not depend on discretization.
### 3. Simulation Loop (Event-Driven Design)
- The run method repeatedly processes the next event based on `find_next_event()`.
- Events are dynamically determined rather than using fixed time steps, making the simulation in the continuous time domain without any discretization.
- The simulation is free of any time discretization issues that arise in epoch-based simulations.
### 4. State Pattern (Cell Lifecycle)
- The Cell class has attributes like `is_alive` and `will_divide`, which dictate its behavior.
- The `deactivate_cell` function transitions a cell's state from alive to inactive.
### 5. Observer Pattern (Logging Events)
- The `log_event` method records key events (division and death) during the simulation.
- This allows external components to observe and analyze the simulation history.

## Coding Techniques for Efficiency and Readability

### Lambda Functions
The use of lambda functions allows for concise and readable definitions of functions, especially when defining custom probability distributions for division and lifetime.
This is particularly useful since no discrete of probability distributions are used in the simulation.

```python
division_func = lambda x: np.random.gamma(5, 1, x)
lifetime_func = lambda x: np.random.exponential(1, x)
```

This approach simplifies the code and makes it easier to understand the logic behind the simulation.