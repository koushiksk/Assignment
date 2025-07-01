# Conway's Game of Life

## Overview

This project is a Python implementation of Conway's Game of Life, a classic zero-player game that demonstrates how complex patterns can emerge from a small set of simple rules.

The application allows a user to provide an initial "seed" of live cells, and it will calculate and display the state of the universe after one "tick," or generation.

## Architecture

The solution is divided into three key files to ensure a clear separation of concerns, following production-quality coding practices.

-   **`universe.py`**: Contains the core logic for the Game of Life. The `Universe` class manages the state of all cells and implements the rules for transitioning from one generation to the next.
-   **`main.py`**: Provides the console user interface. It is responsible for parsing user input, initializing the universe with a starting pattern, triggering the simulation, and displaying the results.
-   **`test_game_of_life.py`**: Contains unit tests for the core logic. It uses the examples provided in the problem description (Block, Boat, Blinker, Toad) to verify that the `Universe` class behaves correctly.

## Design Choices

-   **Data Structure for the Grid**: The infinite two-dimensional grid is represented by a `set` of `(x, y)` tuples. Each tuple in the set corresponds to the coordinate of a live cell. This approach is highly memory-efficient compared to a traditional 2D array, as it only stores the live cells and does not need to define fixed boundaries for the "infinite" grid.

-   **Simulation Algorithm (`tick` method)**: To calculate the next generation, the algorithm avoids iterating over an infinite space. Instead, it identifies a finite set of "candidate" cells that could potentially be alive in the next generation. A candidate is any cell that is currently alive or is a direct neighbor of a live cell. For each candidate, the algorithm counts its live neighbors and applies the four rules of the game to determine if it should be included in the next generation's set of live cells.

## How to Run

### Running the Application

To run the interactive console application, execute the following command from the project's root directory:

```bash
python conways_life/main.py
```

You will be prompted to enter the coordinates of the initial live cells. You can enter them one per line or multiple per line, separated by characters like `|` or `,`. When you are finished, type `done`.

### Running the Unit Tests

To verify that the core logic is working correctly, run the unit tests:

```bash
python conways_life/test_game_of_life.py
```

All tests should pass, confirming that the implementation correctly handles the example patterns from the problem description. 