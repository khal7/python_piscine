from mlx import Mlx
import random
import time

animating = True
anim_step = 0


ANIM_STEPS = 30
CELL_SIZE = 60
WALL_COLORS = [0xFFFFFFFF, 0xFF0000FF, 0xFF00FF00, 0xFFFF0000]
color_index = 0
show_path = True
MARGIN = 100

mlx = Mlx()
mlx_ptr = mlx.mlx_init()
with open("maze.txt") as f:
    lines = f.readlines()


empty = lines.index("\n")
grid = lines[:empty]
entry_line = lines[empty + 1].strip()
exit_line = lines[empty + 2].strip()
path = lines[empty + 3].strip()
cols = len(grid[0].strip())
rows = len(grid)
anim_grid = [['F'] * cols for _ in range(rows)]

entry = tuple(map(int, entry_line.split(",")))
exits = tuple(map(int, exit_line.split(",")))

print(f"entry: {entry}, exit, {exits}")

win_width = cols * CELL_SIZE + MARGIN * 2
win_height = rows * CELL_SIZE + MARGIN * 2 + 60
win_ptr = mlx.mlx_new_window(mlx_ptr, win_width, win_height, "A-Maze-ing")
mlx.mlx_clear_window(mlx_ptr, win_ptr)
img = mlx.mlx_new_image(mlx_ptr, win_width, win_height)

buf, bpp, line_size, fmt = mlx.mlx_get_data_addr(img)


def redraw_grid(g) -> None:
    fill_background(buf, 0xFF000000)
    draw_marker(buf, line_size, entry[0], entry[1], 0xFF00FF00)
    draw_marker(buf, line_size, exits[0], exits[1], 0xFFFF0000)
    for r, line in enumerate(g):
        for c, char in enumerate(line):
            cell = int(char, 16)
            if cell & 1:
                draw_north_wall(buf, line_size, c, r, WALL_COLORS[color_index])
            if cell & 2:
                draw_east_wall(buf, line_size, c, r, WALL_COLORS[color_index])
            if cell & 4:
                draw_south_wall(buf, line_size, c, r, WALL_COLORS[color_index])
            if cell & 8:
                draw_west_wall(buf, line_size, c, r, WALL_COLORS[color_index])
    mlx.mlx_put_image_to_window(mlx_ptr, win_ptr, img, 0, 0)


last_time = [time.time()]


def animate(param) -> None:
    global animating, anim_step, anim_grid
    if not animating:
        return
    now = time.time()
    if now - last_time[0] < 0.05:  # 50ms between frames
        return
    last_time[0] = now
    if anim_step < ANIM_STEPS:
        for _ in range(5):
            r = random.randint(0, rows - 1)
            c = random.randint(0, cols - 1)
            anim_grid[r][c] = random.choice(['0', '5', 'A', 'F'])
        redraw_grid(anim_grid)
        anim_step += 1
    else:
        animating = False
        redraw()


def on_expose(param):
    mlx.mlx_put_image_to_window(mlx_ptr, win_ptr, img, 0, 0)


def draw_marker(buf, line_size, col, row, color) -> None:

    x = col * CELL_SIZE + MARGIN
    y = row * CELL_SIZE + MARGIN
    for dy in range(CELL_SIZE):
        for dx in range(CELL_SIZE):
            offset = (y + dy) * line_size + (x + dx) * 4
            buf[offset] = color & 0xFF
            buf[offset + 1] = (color >> 8) & 0xFF
            buf[offset + 2] = (color >> 16) & 0xFF
            buf[offset + 3] = (color >> 24) & 0xFF


def draw_north_wall(buf, line_size, col, row, color) -> None:
    x = col * CELL_SIZE + MARGIN
    y = row * CELL_SIZE + MARGIN
    for i in range(CELL_SIZE):
        offset = y * line_size + (x + i) * 4
        buf[offset] = color & 0xFF
        buf[offset + 1] = (color >> 8) & 0xFF
        buf[offset + 2] = (color >> 16) & 0xFF
        buf[offset + 3] = (color >> 24) & 0xFF


def draw_south_wall(buf, line_size, col, row, color) -> None:
    x = col * CELL_SIZE + MARGIN
    y = row * CELL_SIZE + (CELL_SIZE - 1) + MARGIN
    for i in range(CELL_SIZE):
        offset = y * line_size + (x + i) * 4
        buf[offset] = color & 0xFF
        buf[offset + 1] = (color >> 8) & 0xFF
        buf[offset + 2] = (color >> 16) & 0xFF
        buf[offset + 3] = (color >> 24) & 0xFF


def draw_east_wall(buf, line_size, col, row, color) -> None:
    x = col * CELL_SIZE + (CELL_SIZE - 1) + MARGIN
    y = row * CELL_SIZE + MARGIN
    for i in range(CELL_SIZE):
        offset = (y + i) * line_size + x * 4
        buf[offset] = color & 0xFF
        buf[offset + 1] = (color >> 8) & 0xFF
        buf[offset + 2] = (color >> 16) & 0xFF
        buf[offset + 3] = (color >> 24) & 0xFF


def draw_west_wall(buf, line_size, col, row, color) -> None:
    x = col * CELL_SIZE + MARGIN
    y = row * CELL_SIZE + MARGIN
    for i in range(CELL_SIZE):
        offset = (y + i) * line_size + x * 4
        buf[offset] = color & 0xFF
        buf[offset + 1] = (color >> 8) & 0xFF
        buf[offset + 2] = (color >> 16) & 0xFF
        buf[offset + 3] = (color >> 24) & 0xFF


def fill_background(buf, color) -> None:
    pixel = (
        (color & 0xFF).to_bytes(1, 'little') +
        ((color >> 8) & 0xFF).to_bytes(1, 'little') +
        ((color >> 16) & 0xFF).to_bytes(1, 'little') +
        ((color >> 24) & 0xFF).to_bytes(1, 'little')
    ) * (win_width * win_height)
    buf[:] = pixel


def draw_path(buf, line_size, path, start_col, start_row, color) -> None:
    col = start_col
    row = start_row
    for direction in path:
        dot_size = CELL_SIZE // 3
        x = col * CELL_SIZE + MARGIN + (CELL_SIZE - dot_size) // 2
        y = row * CELL_SIZE + MARGIN + (CELL_SIZE - dot_size) // 2

        for dy in range(dot_size):
            for dx in range(dot_size):
                offset = (y + dy) * line_size + (x + dx) * 4
                buf[offset] = color & 0xFF
                buf[offset + 1] = (color >> 8) & 0xFF
                buf[offset + 2] = (color >> 16) & 0xFF
                buf[offset + 3] = (color >> 24) & 0xFF
        if direction == 'E':
            col += 1
        elif direction == 'W':
            col -= 1
        elif direction == 'S':
            row += 1
        elif direction == 'N':
            row -= 1


def redraw() -> None:
    color = 0xFF000000
    fill_background(buf, color)

    draw_marker(buf, line_size, entry[0], entry[1], 0xFF00FF00)  # green
    draw_marker(buf, line_size, exits[0], exits[1], 0xFFFF0000)

    for row, line in enumerate(grid):
        for col, char in enumerate(line.strip()):
            cell = int(char, 16)
            if cell & 1:  # North
                draw_north_wall(buf, line_size, col, row,
                                WALL_COLORS[color_index])
            if cell & 2:  # East
                draw_east_wall(buf, line_size, col, row,
                               WALL_COLORS[color_index])
            if cell & 4:  # South
                draw_south_wall(buf, line_size, col, row,
                                WALL_COLORS[color_index])
            if cell & 8:  # West
                draw_west_wall(buf, line_size, col, row,
                               WALL_COLORS[color_index])
    if show_path:
        draw_path(buf, line_size, path, entry[0], entry[1], 0xFFFFFF00)
    mlx.mlx_put_image_to_window(mlx_ptr, win_ptr, img, 0, 0)
    mlx.mlx_string_put(mlx_ptr, win_ptr, MARGIN, rows * CELL_SIZE +
                       MARGIN + 30, 0xFFFFFFFF,
                       "1: REGEN;2: PATH; 3: COLOR; 4: QUIT; 5: ANIMATION")


mlx.mlx_expose_hook(win_ptr, on_expose, None)


def on_key(keycode, param):
    print(f"key pressed: {keycode}")
    global color_index
    global show_path
    if keycode == 65307:  # Escape
        mlx.mlx_loop_exit(mlx_ptr)
    elif keycode == 49:  # 1: to regen
        pass
    elif keycode == 50:  # 2: to show/hide path
        show_path = not show_path
        redraw()
    elif keycode == 51:  # 3: to change color
        color_index = (color_index + 1) % len(WALL_COLORS)
        redraw()
    elif keycode == 52:  # q: to quit
        mlx.mlx_loop_exit(mlx_ptr)
    elif keycode == 53:  # 5: animate
        global animating, anim_step, anim_grid
        animating = True
        anim_step = 0
        anim_grid = [['F'] * cols for _ in range(rows)]
        redraw_grid(anim_grid)


# redraw()
redraw_grid(anim_grid)
mlx.mlx_loop_hook(mlx_ptr, animate, None)
mlx.mlx_hook(win_ptr, 2, 1, on_key, None)
mlx.mlx_loop(mlx_ptr)
