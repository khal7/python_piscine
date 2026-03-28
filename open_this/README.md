*This project has been created as part of the 42 curriculum by abelgarh, khabouou.*

## Description
The "A-Maze-ing" project is a Python-based maze generator and solver. The goal is to parse a configuration file to randomly generate a valid maze (perfect or imperfect), ensure specific patterns (like "42") are included, find the shortest path from an entry to an exit point, and display the result.

## Instructions
**Execution:**
Run the main program by passing the configuration file as an argument:
`python3 a_maze_ing.py config.txt`

## Configuration File Format
The config file requires one `KEY=VALUE` pair per line (comments starting with `#` are ignored):
* `WIDTH` / `HEIGHT`: Int (Maze dimensions)
* `ENTRY` / `EXIT`: x,y coordinates
* `SEED`: Int (For reproducibility)
* `OUTPUT_FILE`: String (Name of the generated file)
* `PERFECT`: True/False (Determines if the maze has only one path or multiple loops)

## Algorithm and Technical Choices
* **Generation Algorithm:** We used a randomized Depth-First Search (DFS) with a stack (Iterative Backtracking).
* **Why DFS?** It is efficient, guarantees a fully connected maze (a perfect maze), and prevents isolated cells. It is also easy to modify for the "42" pattern requirement.
* **Pathfinding:** Breadth-First Search (BFS) was implemented to guarantee finding the shortest path between the entry and exit.

## Reusable Code
The core generation logic (`Maze` and `Cell` classes) is isolated in a standalone module. It can be built into a Python package (`mazegen-*`) using `pip` and the `.whl` or `.tar.gz` files provided in the root directory. This allows the maze logic to be imported and reused in future external projects.

## Team and Project Management
* **Roles:** * abelgarh: Core generation logic, configuration parsing, pathfinding (BFS), and code packaging.
  * [Teammate Name]: Visual representation and user interaction (Terminal/MLX rendering).
* **Planning:** [Write a short sentence about how you split the time/tasks]
* **What worked well / to improve:** [Write 1-2 points about your teamwork or struggles]
* **Tools used:** Python, Git, [Add other tools like Notion, Discord, etc.]

## Resources
* Mazes for Programmers Code Your Own Twisty Little Passages (Jamis Buck).pdf
* https://medium.com/@singhatul1155/graph-traversal-demystified-mastering-dfs-and-bfs-techniques-c27cb8590e31
* https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/
* ai was used as a learning tool to trace the BFS algorithm step-by-step, debug the perfect/imperfect generation logic, and understand Python packaging requirements.
* https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/