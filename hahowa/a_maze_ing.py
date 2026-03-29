import sys
from mazegen import MazeGenerator, read_config, process_config, validate_config
from display import MazeDisplay


def main() -> None:
    """
    Run the full maze generation workflow.

    This function:
    - reads the config file path from command-line arguments
    - loads and processes the configuration file
    - validates the configuration values
    - creates the maze object
    - generates the maze using the given seed
    - writes the hexadecimal maze output to the output file

    If an error occurs, it prints the error message.
    """
    try:
        if len(sys.argv) != 2:
            print("Please provide the config file path.")
            return

        path = sys.argv[1]
        readed_config = read_config(path)
        parsed_config = process_config(readed_config)
        validate_config(parsed_config)

        maze = MazeGenerator(
            parsed_config["width"],
            parsed_config["height"],
            parsed_config["entry"],
            parsed_config["exit"],
        )
        maze.pattern_42()
        maze.generate(parsed_config.get("seed"))
        if not parsed_config["perfect"]:
            maze.not_perfect()
        maze.write_output(parsed_config["output_file"])
        display = MazeDisplay(
            parsed_config["output_file"], maze, parsed_config)
        display.run()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
