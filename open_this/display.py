from mlx import Mlx  # type: ignore
import random
import time
from mazegen import MazeGenerator
# Constants stay outside the class — they never change
ANIM_STEPS = 30
CELL_SIZE = 60
WALL_COLORS = [0xFFFFFFFF, 0xFF0000FF, 0xFF00FF00, 0xFFFF0000]
MARGIN = 100


class MazeDisplay:
    """Handles all visual rendering of the maze using MLX."""

    def __init__(
            self, maze_file: str,
            maze: MazeGenerator,
            config: dict
    ) -> None:
        """Initialize the display window and load the maze file.

        Args:
            maze_file: Path to the hex maze output file.
        """
        # MLX setup
        self.mlx = Mlx()
        self.mlx_ptr = self.mlx.mlx_init()

        # State variables
        self.color_index = 0
        self.show_path = True
        self.animating = True
        self.anim_step = 0
        self.last_time = [time.time()]
        self.maze_file = maze_file
        self.maze = maze
        self.config = config

        # Load maze data from file
        self.load_maze(maze_file)

        # Create window and image buffer
        self.win_width = self.cols * CELL_SIZE + MARGIN * 2
        self.win_height = self.rows * CELL_SIZE + MARGIN * 2 + 60
        self.win_ptr = self.mlx.mlx_new_window(
            self.mlx_ptr, self.win_width, self.win_height, "A-Maze-ing"
        )
        self.mlx.mlx_clear_window(self.mlx_ptr, self.win_ptr)
        self.img = self.mlx.mlx_new_image(
            self.mlx_ptr, self.win_width, self.win_height
        )
        self.buf, self.bpp, self.line_size, self.fmt = (
            self.mlx.mlx_get_data_addr(self.img)
        )
        # Register hooks
        self.mlx.mlx_expose_hook(self.win_ptr, self.on_expose, None)
        self.mlx.mlx_hook(self.win_ptr, 2, 1, self.on_key, None)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.animate, None)

    def load_maze(self, maze_file: str) -> None:
        """Read and parse the hex maze file.

        Args:
            maze_file: Path to the maze file to load.
        """
        with open(maze_file) as f:
            lines = f.readlines()

        empty = lines.index("\n")
        self.grid = lines[:empty]
        self.entry = tuple(map(int, lines[empty + 1].strip().split(",")))
        self.exits = tuple(map(int, lines[empty + 2].strip().split(",")))
        self.path = lines[empty + 3].strip()
        self.cols = len(self.grid[0].strip())
        self.rows = len(self.grid)
        self.anim_grid = [['F'] * self.cols for _ in range(self.rows)]

        # print(f"entry: {self.entry}, exit: {self.exits}")

    def run(self) -> None:
        """Start the animation and enter the MLX event loop."""
        self.redraw_grid(self.anim_grid)
        self.mlx.mlx_loop(self.mlx_ptr)

    # -------------------------------------------------------------------------
    # Drawing methods
    # -------------------------------------------------------------------------

    def fill_background(self, color: int) -> None:
        """Fill the entire image buffer with a single color.

        Args:
            color: ARGB color value.
        """
        pixel = (
            (color & 0xFF).to_bytes(1, 'little') +
            ((color >> 8) & 0xFF).to_bytes(1, 'little') +
            ((color >> 16) & 0xFF).to_bytes(1, 'little') +
            ((color >> 24) & 0xFF).to_bytes(1, 'little')
        ) * (self.win_width * self.win_height)
        self.buf[:] = pixel

    def draw_marker(self, col: int, row: int, color: int) -> None:
        """Fill an entire cell with a color (used for entry/exit markers).

        Args:
            col: Cell column.
            row: Cell row.
            color: ARGB color value.
        """
        x = col * CELL_SIZE + MARGIN
        y = row * CELL_SIZE + MARGIN
        for dy in range(CELL_SIZE):
            for dx in range(CELL_SIZE):
                offset = (y + dy) * self.line_size + (x + dx) * 4
                self.buf[offset] = color & 0xFF
                self.buf[offset + 1] = (color >> 8) & 0xFF
                self.buf[offset + 2] = (color >> 16) & 0xFF
                self.buf[offset + 3] = (color >> 24) & 0xFF

    def draw_north_wall(self, col: int, row: int, color: int) -> None:
        """Draw the north wall of a cell.

        Args:
            col: Cell column.
            row: Cell row.
            color: ARGB color value.
        """
        x = col * CELL_SIZE + MARGIN
        y = row * CELL_SIZE + MARGIN
        for i in range(CELL_SIZE):
            offset = y * self.line_size + (x + i) * 4
            self.buf[offset] = color & 0xFF
            self.buf[offset + 1] = (color >> 8) & 0xFF
            self.buf[offset + 2] = (color >> 16) & 0xFF
            self.buf[offset + 3] = (color >> 24) & 0xFF

    def draw_south_wall(self, col: int, row: int, color: int) -> None:
        """Draw the south wall of a cell.

        Args:
            col: Cell column.
            row: Cell row.
            color: ARGB color value.
        """
        x = col * CELL_SIZE + MARGIN
        y = row * CELL_SIZE + (CELL_SIZE - 1) + MARGIN
        for i in range(CELL_SIZE):
            offset = y * self.line_size + (x + i) * 4
            self.buf[offset] = color & 0xFF
            self.buf[offset + 1] = (color >> 8) & 0xFF
            self.buf[offset + 2] = (color >> 16) & 0xFF
            self.buf[offset + 3] = (color >> 24) & 0xFF

    def draw_east_wall(self, col: int, row: int, color: int) -> None:
        """Draw the east wall of a cell.

        Args:
            col: Cell column.
            row: Cell row.
            color: ARGB color value.
        """
        x = col * CELL_SIZE + (CELL_SIZE - 1) + MARGIN
        y = row * CELL_SIZE + MARGIN
        for i in range(CELL_SIZE):
            offset = (y + i) * self.line_size + x * 4
            self.buf[offset] = color & 0xFF
            self.buf[offset + 1] = (color >> 8) & 0xFF
            self.buf[offset + 2] = (color >> 16) & 0xFF
            self.buf[offset + 3] = (color >> 24) & 0xFF

    def draw_west_wall(self, col: int, row: int, color: int) -> None:
        """Draw the west wall of a cell.

        Args:
            col: Cell column.
            row: Cell row.
            color: ARGB color value.
        """
        x = col * CELL_SIZE + MARGIN
        y = row * CELL_SIZE + MARGIN
        for i in range(CELL_SIZE):
            offset = (y + i) * self.line_size + x * 4
            self.buf[offset] = color & 0xFF
            self.buf[offset + 1] = (color >> 8) & 0xFF
            self.buf[offset + 2] = (color >> 16) & 0xFF
            self.buf[offset + 3] = (color >> 24) & 0xFF

    def draw_path(self, path: str, start_col: int, start_row: int,
                  color: int) -> None:
        """Draw the solution path as dots through the maze.

        Args:
            path: String of directions e.g. 'SSEENWW'.
            start_col: Starting column (entry x).
            start_row: Starting row (entry y).
            color: ARGB color value.
        """
        col = start_col
        row = start_row
        for direction in path:
            dot_size = CELL_SIZE // 3
            x = col * CELL_SIZE + MARGIN + (CELL_SIZE - dot_size) // 2
            y = row * CELL_SIZE + MARGIN + (CELL_SIZE - dot_size) // 2
            for dy in range(dot_size):
                for dx in range(dot_size):
                    offset = (y + dy) * self.line_size + (x + dx) * 4
                    self.buf[offset] = color & 0xFF
                    self.buf[offset + 1] = (color >> 8) & 0xFF
                    self.buf[offset + 2] = (color >> 16) & 0xFF
                    self.buf[offset + 3] = (color >> 24) & 0xFF
            if direction == 'E':
                col += 1
            elif direction == 'W':
                col -= 1
            elif direction == 'S':
                row += 1
            elif direction == 'N':
                row -= 1

    def redraw_grid(self, g: list) -> None:
        """Redraw the maze from a given grid (used during animation).

        Args:
            g: 2D list of hex characters representing the maze.
        """
        self.fill_background(0xFF000000)
        self.draw_marker(self.entry[0], self.entry[1], 0xFF00FF00)
        self.draw_marker(self.exits[0], self.exits[1], 0xFFFF0000)
        for r, line in enumerate(g):
            for c, char in enumerate(line):
                cell = int(char, 16)
                color = WALL_COLORS[self.color_index]
                if cell & 1:
                    self.draw_north_wall(c, r, color)
                if cell & 2:
                    self.draw_east_wall(c, r, color)
                if cell & 4:
                    self.draw_south_wall(c, r, color)
                if cell & 8:
                    self.draw_west_wall(c, r, color)
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.win_ptr, self.img, 0, 0
        )

    def redraw(self) -> None:
        """Redraw the full maze with current state (path, colors, markers)."""
        self.fill_background(0xFF000000)
        self.draw_marker(self.entry[0], self.entry[1], 0xFF00FF00)
        self.draw_marker(self.exits[0], self.exits[1], 0xFFFF0000)
        for row, line in enumerate(self.grid):
            for col, char in enumerate(line.strip()):
                cell = int(char, 16)
                color = WALL_COLORS[self.color_index]
                if cell & 1:
                    self.draw_north_wall(col, row, color)
                if cell & 2:
                    self.draw_east_wall(col, row, color)
                if cell & 4:
                    self.draw_south_wall(col, row, color)
                if cell & 8:
                    self.draw_west_wall(col, row, color)
        if self.show_path:
            self.draw_path(
                self.path, self.entry[0], self.entry[1], 0xFFFFFF00
            )
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.win_ptr, self.img, 0, 0
        )
        self.mlx.mlx_string_put(
            self.mlx_ptr, self.win_ptr,
            MARGIN, self.rows * CELL_SIZE + MARGIN + 30,
            0xFFFFFFFF,
            "1: REGEN; 2: PATH; 3: COLOR; 4: QUIT; 5: ANIMATION"
        )

    # -------------------------------------------------------------------------
    # Event hooks
    # -------------------------------------------------------------------------

    def on_expose(self, param: object) -> None:
        """Redraw the image when the window is exposed.

        Args:
            param: Unused MLX parameter.
        """
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.win_ptr, self.img, 0, 0
        )

    def animate(self, param: object) -> None:
        """Loop hook that handles the reveal animation frame by frame.

        Args:
            param: Unused MLX parameter.
        """
        if not self.animating:
            return
        now = time.time()
        if now - self.last_time[0] < 0.05:
            return
        self.last_time[0] = now
        if self.anim_step < ANIM_STEPS:
            for _ in range(5):
                r = random.randint(0, self.rows - 1)
                c = random.randint(0, self.cols - 1)
                self.anim_grid[r][c] = random.choice(['0', '5', 'A', 'F'])
            self.redraw_grid(self.anim_grid)
            self.anim_step += 1
        else:
            self.animating = False
            self.redraw()

    def on_key(self, keycode: int, param: object) -> None:
        """Handle keyboard input for all user interactions.

        Args:
            keycode: The key code of the pressed key.
            param: Unused MLX parameter.
        """
        print(f"key pressed: {keycode}")
        if keycode == 65307:  # Escape
            self.mlx.mlx_loop_exit(self.mlx_ptr)
        elif keycode == 49:   # 1: regen
            self.maze = MazeGenerator(
                self.config["width"],
                self.config["height"],
                self.config["entry"],
                self.config["exit"],
            )
            self.maze.pattern_42()
            seed = self.config.get("seed")
            self.maze.generate(seed)
            if not self.config["perfect"]:
                self.maze.not_perfect()
            self.maze.write_output(self.config["output_file"])
            self.load_maze(self.config["output_file"])
            self.animating = True
            self.anim_step = 0
            self.anim_grid = [['F'] * self.cols for _ in range(self.rows)]

        elif keycode == 50:   # 2: show/hide path
            self.show_path = not self.show_path
            self.redraw()
        elif keycode == 51:   # 3: change wall color
            self.color_index = (self.color_index + 1) % len(WALL_COLORS)
            self.redraw()
        elif keycode == 52:   # 4: quit
            self.mlx.mlx_loop_exit(self.mlx_ptr)
        elif keycode == 53:   # 5: trigger animation
            self.animating = True
            self.anim_step = 0
            self.anim_grid = [['F'] * self.cols for _ in range(self.rows)]
            self.redraw_grid(self.anim_grid)
