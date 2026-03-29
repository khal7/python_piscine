*This project has been created as part of the 42 curriculum by abelgarh, khabouou.*

# A-Maze-ing

## Description
A-Maze-ing is a Python project that generates, solves, stores, and displays mazes from a configuration file.

The program reads a text configuration file, validates its content, generates a random maze, writes that maze to an output file using a hexadecimal wall encoding, computes the shortest path from the entry to the exit, and provides a visual representation of the result.

The project also separates the maze generation logic into a reusable Python package named `mazegen-*`, so the core generator can be rebuilt and reused in another project.

## Instructions

### Requirements
- Python 3.10 or later
- A virtual environment is recommended
- Any dependencies required by your visual display mode

### Standard execution
Run the project with a configuration file:

```bash
python3 a_maze_ing.py config.txt
```

`a_maze_ing.py` is the main file.
`config.txt` is the configuration file passed as the only argument.

### Build and reinstall the reusable package
The evaluation may require rebuilding the package inside a virtual environment, then installing it again in another environment.

Example workflow:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip build
python3 -m build
```

This should recreate a file named like:

```text
mazegen-1.0.0-py3-none-any.whl
```

or:

```text
mazegen-1.0.0.tar.gz
```

Then, in another virtual environment, install the package and run the project again:

```bash
python3 -m venv testenv
source testenv/bin/activate
python3 -m pip install dist/mazegen-1.0.0-py3-none-any.whl
python3 a_maze_ing.py config.txt
```

### Linting and type checking
The project is expected to pass `flake8` and `mypy`.

Example:

```bash
flake8 .
mypy .
```

## Configuration File Format
The configuration file contains one `KEY=VALUE` pair per line.
Lines starting with `#` are comments and must be ignored.

### Mandatory keys
| Key | Description | Example |
|---|---|---|
| `WIDTH` | Maze width in number of cells | `WIDTH=20` |
| `HEIGHT` | Maze height in number of cells | `HEIGHT=15` |
| `ENTRY` | Entry coordinates `(x,y)` | `ENTRY=0,0` |
| `EXIT` | Exit coordinates `(x,y)` | `EXIT=19,14` |
| `OUTPUT_FILE` | Output file name | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Defines whether the maze must be perfect | `PERFECT=True` |

### Example configuration
```text
# Default maze configuration
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

### Validation rules
The program must reject invalid configurations gracefully and print a clear error message instead of crashing.

Typical invalid cases include:
- a missing mandatory key
- a line that does not respect the `KEY=VALUE` format
- letters instead of numbers for integer fields
- an invalid boolean value for `PERFECT`
- a wrong tuple format for `ENTRY` or `EXIT`
- entry or exit outside maze bounds
- identical entry and exit
- impossible maze dimensions

## Maze Generation Algorithm
The chosen maze generation algorithm is a randomized Depth-First Search using iterative backtracking with a stack.

### Why this algorithm was chosen
This algorithm was chosen because:
- it is simple to implement and explain
- it guarantees full connectivity in the perfect maze case
- it naturally creates a valid maze structure without isolated cells
- it works well with reproducibility when a seed is provided
- it is easy to extend with project-specific constraints such as the visible `42` pattern

## Maze Rules Followed by the Project
The generated maze is designed to respect the project requirements:
- the maze is randomly generated
- reproducibility is possible through a seed
- each cell has up to four walls: north, east, south, west
- entry and exit are inside the maze and are different
- neighbouring cells always agree on shared walls
- the maze keeps walls on the external borders
- the structure avoids isolated cells, except for the fully closed cells used to draw `42`
- the maze must not contain a `3x3` or larger fully open zone
- when the maze is large enough, a visible `42` pattern is included
- if `PERFECT=True`, the maze contains exactly one valid path between entry and exit

If the maze is too small to contain the `42` pattern, the program prints an error message on the console.

## Shortest Path
The shortest path from entry to exit is computed with Breadth-First Search (`BFS`).

BFS was chosen for pathfinding because it guarantees the shortest path in an unweighted grid/graph, which matches the maze structure used in this project.

## Output File Format
The generated maze is written to the output file using one hexadecimal digit per cell.
Each digit represents which walls are closed.

### Output structure
The output file contains:
1. `HEIGHT` lines
2. each line contains `WIDTH` hexadecimal characters
3. one empty line
4. the entry coordinates
5. the exit coordinates
6. the shortest valid path using only `N`, `E`, `S`, `W`

All lines end with a newline.

## Visual Representation and Interaction
The project provides a visual display of the maze, either in the terminal or in a graphical window depending on the chosen implementation.

The display shows at least:
- walls
- entry
- exit
- shortest path

The interactive part of the program includes the mandatory actions required during evaluation:
- regenerate a new maze
- show or hide the shortest path
- change the wall colours

Additional interactions may also be supported.

## Reusable Module Documentation
The reusable part of the project is the maze generation package `mazegen-*`.
It contains the core classes and logic responsible for:
- maze creation
- wall management
- generation using the selected algorithm
- shortest-path computation
- exporting or accessing the generated maze structure

### What is reusable
The reusable module exposes the maze generator independently from the main visual application.
This means the generation logic can be imported and reused in another Python project without copying the whole repository.


## Team and Project Management

### Roles of each team member
- `abelgarh`: configuration parsing, validation, maze generation logic, pathfinding, debugging, and documentation updates
- `khabouou`: visual representation, interaction flow, display integration, packaging

### Anticipated planning and how it evolved
At the beginning, the plan was to split the project into three large parts: parsing, generation, and display.
Later, the planning evolved because more time than expected was needed for validation, wall coherence, shortest-path correctness, and packaging the reusable module for evaluation.
As a result, the project was finished in smaller iterations: first parsing and generation, then pathfinding and output format, then display and packaging.

### What worked well
- Splitting the project into separate responsibilities made debugging easier.
- Keeping the generator logic separate from the display helped code reuse and testing.

### What could be improved
- More shared testing earlier in the project would have reduced integration issues.
- The README and packaging steps should have been finalized earlier to better prepare for peer-evaluation.

## Resources
- *Mazes for Programmers: Code Your Own Twisty Little Passages* — Jamis Buck
- Python official documentation
- Graph traversal references for DFS and BFS
- Packaging references for Python wheels and source distributions
- The project subject and the provided correction scale

### AI usage
AI was used as a learning and support tool, not as a blind code generator.
More precisely, AI was used for:
- understanding DFS, BFS, backtracking, and graph traversal concepts
- improving docstrings and README structure

