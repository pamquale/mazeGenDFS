# Procedural Maze Game

## Overview

This project is a maze game developed in Python using the Pygame library. Each time the game is run, it generates a new unique maze using a Depth-First Search (DFS) algorithm with recursive backtracking. The player can navigate through the maze, starting from the top-left corner and aiming to reach the bottom-right corner, which is marked as the exit.

## Features

- **Procedural Maze Generation**: Generates a unique maze on each run using the DFS algorithm.
- **Player Movement**: Move the player using arrow keys (up, down, left, right).
- **Collision Detection**: Ensures the player cannot move through walls.
- **Exit Point**: The goal is to reach the exit point, marked in green.
- **Win Condition**: Displays a win message and provides an option to restart the game with a new maze upon reaching the exit.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pamquale/mazeGenDFS.git
    cd mazeGenDFS
    ```

2. **Install the required packages**:
    Ensure you have Python installed. Then install Pygame using pip:
    ```bash
    pip install pygame
    ```

3. **Run the game**:
    ```bash
    python main.py
    ```

## How to Play

- Use the arrow keys to move the red player dot through the maze.
- The goal is to reach the green exit square at the bottom-right corner.
- Upon reaching the exit, a win message will be displayed.
- Press 'R' to restart the game with a new maze.

## Code Explanation

### Maze Generation

The maze is generated using the Depth-First Search (DFS) algorithm with recursive backtracking. The algorithm starts at the top-left corner and carves out a path through the grid by visiting unvisited neighbors and removing walls between cells.

### Ensuring Path to Exit

After generating the maze, the game ensures there is a path from the start to the exit by using a Breadth-First Search (BFS) algorithm to check connectivity. If no path is found, a direct path is created from the start to the exit.

### Key Methods

- `generate_maze()`: Generates the maze using DFS.
- `ensure_path_to_exit()`: Ensures there is a valid path from the start to the exit using BFS.
- `create_direct_path()`: Creates a direct path from the start to the exit if necessary.
- `move_player(direction)`: Moves the player in the specified direction, checking for collisions.
- `check_win()`: Checks if the player has reached the exit.
- `display_win_screen()`: Displays the win message and waits for the player to press 'R' to restart.

## Dependencies

- Python 3.x
- Pygame

## License

This project is licensed under the MIT License.
