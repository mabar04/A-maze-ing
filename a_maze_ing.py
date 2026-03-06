from Parsing_folder import Parsing, error_handeling
from Algo import DFS
from Display import hexa_display


class MazeGenerator:
    def __init__(self):
        self.algo = "DFS"

    def initial_maze(self, config):
        maze = [
            [
                {"north": True, "east": True, "south": True, "west": True,
                 "visited": False}
                for _ in range(config["width"])
            ]
            for _ in range(config["height"])
        ]
        return maze

    def generate_maze(self, filename):
        try:
            config = Parsing.read_file(filename)
            error_handeling.check_mandatory_keys(config)
            error_handeling.check_mandatory_values(config)
            error_handeling.check_added_keys(config)
            parsed_Values = Parsing.parse_config(config)
            maze = self.initial_maze(parsed_Values)
            if self.algo == "DFS":
                if parsed_Values["perfect"]:
                    DFS.generate_perfect_maze(maze, 0, 0,
                                              parsed_Values["height"],
                                              parsed_Values["width"])
                elif not parsed_Values["perfect"]:
                    DFS.generate_imperfect_maze(maze,
                                                parsed_Values["height"],
                                                parsed_Values["width"])
            elif self.algo == "Prime":
                pass
            hexa_display.print_maze_hex(maze, parsed_Values["output"])
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    maze_generated = MazeGenerator()
    maze = maze_generated.generate_maze("config.txt")
