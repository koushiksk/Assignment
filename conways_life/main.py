import re
from typing import Set, Tuple
from conways_life.universe import Universe, Cell

def parse_input(input_str: str) -> Set[Cell]:
    """Parse a string of coordinates into a set of cells."""
    live_cells = set()
    # Regex to find pairs of numbers, tolerant of spaces and non-digit chars
    pattern = re.compile(r"(\d+)\s*,\s*(\d+)")
    
    for match in pattern.finditer(input_str):
        x = int(match.group(1))
        y = int(match.group(2))
        live_cells.add((x, y))
        
    return live_cells

def format_output(live_cells: Set[Cell]) -> str:
    """Format a set of live cells into a sorted string for output."""
    if not live_cells:
        return "No cells are alive."
    
    # Sort cells for consistent output, primarily by x, then by y
    sorted_cells = sorted(list(live_cells))
    
    return "\n".join(f"{x}, {y}" for x, y in sorted_cells)

def main():
    """Main function to run the Game of Life console application."""
    print("Conway's Game of Life")
    print("Enter the coordinates of the initial live cells.")
    print("Example: 1, 1 | 1, 2 | 2, 1 | 2, 2")
    print("Type 'done' when you are finished.")
    print("-" * 40)

    input_lines = []
    while True:
        line = input("> ").strip()
        if line.lower() == 'done':
            break
        input_lines.append(line)
        
    initial_state_str = " | ".join(input_lines)
    
    if not initial_state_str:
        print("\nNo input provided. Exiting.")
        return

    live_cells = parse_input(initial_state_str)
    
    universe = Universe(live_cells)
    universe.tick()
    
    next_gen_cells = universe.get_live_cells()
    
    print("\nNext generation:")
    print(format_output(next_gen_cells))
    print("-" * 40)


if __name__ == "__main__":
    main() 