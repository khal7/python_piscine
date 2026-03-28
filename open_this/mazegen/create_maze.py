import random
from collections import deque


class Cell:
    """
    Represents a single cell in the maze grid.

    Each cell knows its position (row and column),
    the state of its four walls, and whether it has
    been visited during maze generation.
    """

    def __init__(self, row: int, col: int) -> None:
        """
        Initialize a cell with its position and default walls.

        Args:
            row: The row index of the cell.
            col: The column index of the cell.
        """
        self.row = row
        self.col = col
        self.north: bool = True
        self.east: bool = True
        self.south: bool = True
        self.west: bool = True
        self.visited: bool = False
        self.is_pattern = False


class MazeGenerator:
    """
    Represents the full maze as a grid of cells.

    The maze stores its width, height, and a 2D grid
    containing all Cell objects.
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry_pos: tuple[int, int],
        exit_pos: tuple[int, int]
    ) -> None:
        """
        Initialize the maze with its dimensions, entry, exit,
        and build the grid.

        Args:
            width: Number of columns in the maze.
            height: Number of rows in the maze.
            entry_pos: Entry position in the maze.
            exit_pos: Exit position in the maze.
        """
        self.width = width
        self.height = height
        self.entry_pos = entry_pos
        self.exit_pos = exit_pos
        self.grid: list[list[Cell]] = self.build_grid()

    def build_grid(self) -> list[list[Cell]]:
        """
        Create and return the 2D grid of cells.

        Returns:
            A list of rows, where each row contains Cell objects.
        """
        grid: list[list[Cell]] = []

        for row in range(self.height):
            current_row: list[Cell] = []
            for col in range(self.width):
                current_row.append(Cell(row, col))
            grid.append(current_row)
        return grid

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Return the cell at the given row and column.

        Args:
            row: The row index of the cell.
            col: The column index of the cell.

        Returns:
            The Cell object at the given position.
        """
        return self.grid[row][col]

    def is_in_bounds(self, row: int, col: int) -> bool:
        """
        Check whether a position is inside the maze boundaries.

        Args:
            row: The row index to check.
            col: The column index to check.

        Returns:
            True if the position is inside the maze, otherwise False.
        """
        return 0 <= row < self.height and 0 <= col < self.width

    def get_neighbors(self, cell: Cell) -> list[tuple[str, Cell]]:
        """
        Return all valid neighboring cells of the given cell.

        This method checks the four possible directions around the cell:
        north, east, south, and west. For each direction, it verifies
        that the position is still inside the maze boundaries. If it is,
        the neighbor is added to the result.

        Args:
            cell: The current cell whose neighbors should be found.

        Returns:
            A list of tuples. Each tuple contains:
            - the direction name as a string
            - the neighboring Cell object

            Example:
                [("north", some_cell), ("east", another_cell)]
        """
        neighbors: list[tuple[str, Cell]] = []

        directions = [
            ("north", cell.row - 1, cell.col),
            ("east", cell.row, cell.col + 1),
            ("south", cell.row + 1, cell.col),
            ("west", cell.row, cell.col - 1),
        ]

        for direction, row, col in directions:
            if self.is_in_bounds(row, col):
                neighbors.append((direction, self.get_cell(row, col)))

        return neighbors

    def remove_wall_between(self, cell1: Cell, cell2: Cell) -> None:
        """
        Remove the shared wall between two adjacent cells.

        This method compares the positions of the two cells to determine
        whether cell2 is north, east, south, or west of cell1. Once their
        relative position is known, it removes the correct wall from both
        cells so the passage stays consistent.

        Args:
            cell1: The first cell.
            cell2: The second cell adjacent to the first one.

        Returns:
            None
        """
        if cell1.row == cell2.row:
            if cell1.col + 1 == cell2.col:
                cell1.east = False
                cell2.west = False
            elif cell1.col - 1 == cell2.col:
                cell1.west = False
                cell2.east = False

        elif cell1.col == cell2.col:
            if cell1.row + 1 == cell2.row:
                cell1.south = False
                cell2.north = False
            elif cell1.row - 1 == cell2.row:
                cell1.north = False
                cell2.south = False

    def not_visited_neighbors(self, cell: Cell) -> list[tuple[str, Cell]]:
        """
        Return only the neighboring cells that have not been visited yet.

        This method first gets all valid neighbors of the given cell,
        then filters them and keeps only those whose visited flag is False.

        Args:
            cell: The current cell whose unvisited neighbors should be found.

        Returns:
            A list of tuples. Each tuple contains:
            - the direction name as a string
            - the neighboring unvisited Cell object
        """
        not_visited_neighbors: list[tuple[str, Cell]] = []

        for direc, neigh in self.get_neighbors(cell):
            if not neigh.visited:
                not_visited_neighbors.append((direc, neigh))

        return not_visited_neighbors

    def generate(self, seed: int) -> None:
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()

        start_cel = self.get_cell(self.entry_pos[1], self.entry_pos[0])
        start_cel.visited = True
        stack = [start_cel]

        while stack:
            curr_cel = stack[-1]
            neighbr = self.not_visited_neighbors(curr_cel)
            if neighbr:
                _, next_cel = random.choice(neighbr)
                self.remove_wall_between(curr_cel, next_cel)
                next_cel.visited = True
                stack.append(next_cel)
            else:
                stack.pop()

    # def generate(self, seed: int) -> None:
    #     # reset all cells first
    #     for row in self.grid:
    #         for cell in row:
    #             cell.visited = False
    #             cell.north = True
    #             cell.east = True
    #             cell.south = True
    #             cell.west = True
    #             cell.is_pattern = False

    #     # re-apply 42 pattern
    #     self.pattern_42()
    #     if seed is not None:
    #         random.seed(seed)
    #     else:
    #         random.seed()
    #     start_cel = self.get_cell(self.entry_pos[1], self.entry_pos[0])
    #     start_cel.visited = True
    #     stack = [start_cel]
    #     while stack:
    #         curr_cel = stack[-1]
    #         neighbr = self.not_visited_neighbors(curr_cel)
    #         if neighbr:
    #             _, next_cel = random.choice(neighbr)
    #             self.remove_wall_between(curr_cel, next_cel)
    #             next_cel.visited = True
    #             stack.append(next_cel)
    #         else:
    #             stack.pop()

    def cell_to_hex(self, cell: Cell) -> str:
        """
        Convert one cell's walls into a hexadecimal digit.

        Wall values:
            north = 1
            east = 2
            south = 4
            west = 8

        Args:
            cell: The cell to convert.

        Returns:
            A hexadecimal string representing the cell walls.
        """
        value = 0

        if cell.north:
            value += 1
        if cell.east:
            value += 2
        if cell.south:
            value += 4
        if cell.west:
            value += 8

        return format(value, "x")

    def row_to_hex(self, row: list[Cell]) -> str:
        """
        Convert one row of cells into a hexadecimal string.

        Each cell in the row is converted to one hex digit,
        then all digits are joined into a single string.

        Args:
            row: A list of Cell objects.

        Returns:
            A string representing the full row in hexadecimal.
        """
        line = ""

        for cell in row:
            line += self.cell_to_hex(cell)

        return line

    def maze_to_hex(self) -> list[str]:
        """
        Convert the full maze into hexadecimal lines.

        Each row in the maze is converted into one hexadecimal string.

        Returns:
            A list of strings, where each string represents one row
            of the maze in hexadecimal format.
        """
        maze_in_hexa = []

        for row in self.grid:
            maze_in_hexa.append(self.row_to_hex(row))

        return maze_in_hexa

    def write_output(self, path: str) -> None:
        """
        Write the maze hexadecimal representation to a file.

        Each row of the maze is written as one line in the output file.

        Args:
            path: Path of the output file.

        Returns:
            None
        """
        lines = self.maze_to_hex()

        with open(path, "w") as file:
            for line in lines:
                file.write(line + "\n")
            file.write("\n")
            file.write(f"{self.entry_pos[0]},{self.entry_pos[1]}\n")
            file.write(f"{self.exit_pos[0]},{self.exit_pos[1]}\n")
            short_path = self.get_directions(self.shortest_path())
            file.write(short_path + "\n")

    # def pattern_42(self) -> None:
    #     """
    #     Check if the maze is large enough to fit the '42' pattern.
    #     If yes, mark the pattern cells as visited so walls remain closed.
    #     If not, print an error message on the console.
    #     """
    #     if self.width < 9 or self.height < 7:
    #         print("Error: Maze too small to generate the '42' pattern.")
    #         return

    #     start_row = (self.height - 5) // 2
    #     start_col = (self.width - 7) // 2

    #     pattern = [
    #         [1, 0, 1, 0, 1, 1, 1],
    #         [1, 0, 1, 0, 0, 0, 1],
    #         [1, 1, 1, 0, 1, 1, 1],
    #         [0, 0, 1, 0, 1, 0, 0],
    #         [0, 0, 1, 0, 1, 1, 1],
    #     ]

    #     for r in range(5):
    #         for c in range(7):
    #             if pattern[r][c] == 1:
    #                 cell = self.get_cell(start_row + r, start_col + c)
    #                 cell.visited = True
    #                 cell.is_pattern = True
    def pattern_42(self) -> None:
        if self.width < 9 or self.height < 7:
            print("Error: Maze too small to generate the '42' pattern.")
            return

        start_row = (self.height - 5) // 2
        start_col = (self.width - 7) // 2

        pattern = [
            [1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 1],
        ]

        entry_cell = (self.entry_pos[1], self.entry_pos[0])  # row, col
        exit_cell = (self.exit_pos[1], self.exit_pos[0])     # row, col

        for r in range(5):
            for c in range(7):
                row = start_row + r
                col = start_col + c

                if pattern[r][c] == 1:
                    if (row, col) == entry_cell or (row, col) == exit_cell:
                        continue

                    cell = self.get_cell(row, col)
                    cell.visited = True
                    cell.is_pattern = True

    def get_directions(self, path: list) -> str:
        if not path:
            return ""

        directions = ""
        for i in range(len(path) - 1):
            curr_r, curr_c = path[i]
            next_r, next_c = path[i + 1]

            if next_r < curr_r:
                directions += "N"
            elif next_r > curr_r:
                directions += "S"
            elif next_c > curr_c:
                directions += "E"
            elif next_c < curr_c:
                directions += "W"

        return directions

    # def shortest_path(self) -> list[tuple]:
    #     """
    #     Find the shortest path from entry to exit using BFS.
    #     Returns a string of directions (N, E, S, W).
    #     """
    #     start = self.entry_pos
    #     exit_ = self.exit_pos
    #     queue = deque([start])
    #     visited = set([start])
    #     parent: dict = {}

    #     while queue:
    #         curr_row, curr_col = queue.popleft()
    #         curr_cell = self.get_cell(curr_row, curr_col)

    #         if (curr_row, curr_col) == exit_:
    #             path = []
    #             current = exit_

    #             while current != start:
    #                 path.append(current)
    #                 current = parent[current]

    #             path.append(start)
    #             path.reverse()
    #             return path

    #         if not curr_cell.north:
    #             nr, nc = curr_row - 1, curr_col
    #             if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
    #                 queue.append((nr, nc))
    #                 visited.add((nr, nc))
    #                 parent[(nr, nc)] = (curr_row, curr_col)

    #         if not curr_cell.south:
    #             nr, nc = curr_row + 1, curr_col
    #             if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
    #                 queue.append((nr, nc))
    #                 visited.add((nr, nc))
    #                 parent[(nr, nc)] = (curr_row, curr_col)

    #         if not curr_cell.east:
    #             nr, nc = curr_row, curr_col + 1
    #             if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
    #                 queue.append((nr, nc))
    #                 visited.add((nr, nc))
    #                 parent[(nr, nc)] = (curr_row, curr_col)

    #         if not curr_cell.west:
    #             nr, nc = curr_row, curr_col - 1
    #             if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
    #                 queue.append((nr, nc))
    #                 visited.add((nr, nc))
    #                 parent[(nr, nc)] = (curr_row, curr_col)

    #     return []
    def shortest_path(self) -> list[tuple[int, int]]:
        start_x, start_y = self.entry_pos
        exit_x, exit_y = self.exit_pos

        start = (start_y, start_x)   # row, col
        exit_ = (exit_y, exit_x)     # row, col

        queue = deque([start])
        visited = {start}
        parent: dict[tuple[int, int], tuple[int, int]] = {}

        while queue:
            curr_row, curr_col = queue.popleft()
            curr_cell = self.get_cell(curr_row, curr_col)

            if (curr_row, curr_col) == exit_:
                path = []
                current = exit_

                while current != start:
                    path.append(current)
                    current = parent[current]

                path.append(start)
                path.reverse()
                return path

            if not curr_cell.north:
                nr, nc = curr_row - 1, curr_col
                if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (curr_row, curr_col)

            if not curr_cell.south:
                nr, nc = curr_row + 1, curr_col
                if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (curr_row, curr_col)

            if not curr_cell.east:
                nr, nc = curr_row, curr_col + 1
                if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (curr_row, curr_col)

            if not curr_cell.west:
                nr, nc = curr_row, curr_col - 1
                if self.is_in_bounds(nr, nc) and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (curr_row, curr_col)

        return []

    def not_perfect(self) -> None:
        """
        Break random internal walls to create loops,
        making the maze imperfect.
        """
        numb_of_wal_break = (self.width * self.height) // 10
        broke_wal = 0

        while broke_wal < numb_of_wal_break:
            r = random.randint(1, self.height - 2)
            c = random.randint(1, self.width - 2)
            cell = self.get_cell(r, c)

            if cell.is_pattern:
                continue

            direction = random.choice(["north", "east", "south", "west"])

            if direction == "north" and cell.north:
                neighbor = self.get_cell(r - 1, c)
                if not neighbor.is_pattern:
                    self.remove_wall_between(cell, neighbor)
                    broke_wal += 1

            elif direction == "east" and cell.east:
                neighbor = self.get_cell(r, c + 1)
                if not neighbor.is_pattern:
                    self.remove_wall_between(cell, neighbor)
                    broke_wal += 1

            elif direction == "south" and cell.south:
                neighbor = self.get_cell(r + 1, c)
                if not neighbor.is_pattern:
                    self.remove_wall_between(cell, neighbor)
                    broke_wal += 1

            elif direction == "west" and cell.west:
                neighbor = self.get_cell(r, c - 1)
                if not neighbor.is_pattern:
                    self.remove_wall_between(cell, neighbor)
                    broke_wal += 1
