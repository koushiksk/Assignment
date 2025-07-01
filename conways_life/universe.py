from typing import Set, Tuple

Cell = Tuple[int, int]

class Universe:
    """Manages the state and rules of the Game of Life."""

    def __init__(self, live_cells: Set[Cell]):
        """
        Initialize the universe with a set of live cells.

        Args:
            live_cells: A set of (x, y) tuples representing live cells.
        """
        self._live_cells = live_cells

    def tick(self) -> None:
        """
        Advance the universe to the next generation by applying the rules.
        """
        next_generation = set()
        
        # Consider all live cells and their neighbors as candidates for life
        candidates = self._live_cells.union(
            neighbor
            for cell in self._live_cells
            for neighbor in self._get_neighbors(cell)
        )

        for cell in candidates:
            live_neighbors = self._count_live_neighbors(cell)
            
            is_alive = cell in self._live_cells
            
            # Rule 1 & 2: A live cell with < 2 or > 3 neighbors dies.
            # Rule 3: A live cell with 2 or 3 neighbors lives.
            if is_alive and (live_neighbors == 2 or live_neighbors == 3):
                next_generation.add(cell)
            
            # Rule 4: A dead cell with exactly 3 neighbors becomes a live cell.
            elif not is_alive and live_neighbors == 3:
                next_generation.add(cell)

        self._live_cells = next_generation

    def get_live_cells(self) -> Set[Cell]:
        """Return the current set of live cells."""
        return self._live_cells

    def _get_neighbors(self, cell: Cell) -> Set[Cell]:
        """Get all 8 neighbors of a given cell."""
        x, y = cell
        neighbors = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbors.add((x + i, y + j))
        return neighbors

    def _count_live_neighbors(self, cell: Cell) -> int:
        """Count the number of live neighbors for a given cell."""
        neighbors = self._get_neighbors(cell)
        return len(self._live_cells.intersection(neighbors)) 