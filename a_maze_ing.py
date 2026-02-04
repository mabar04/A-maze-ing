import random
from maze_curses import run_curses

# Parsing Part
def read_file(filename):
    config = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            key, value = line.split("=", 1)
            config[key] = value
    return config

def parse_config(config):
    width = int(config["WIDTH"])
    height = int(config["HEIGHT"])

    entry_col, entry_row = map(int, config["ENTRY"].split(","))
    exit_col, exit_row = map(int, config["EXIT"].split(","))

    output_file = config["OUTPUT_FILE"]
    perfect = config["PERFECT"]

    return {
        "width": width,
        "height": height,
        "entry": (entry_row, entry_col),
        "exit": (exit_row, exit_col),     
        "output": output_file,
        "perfect": perfect
    }
# first full maze
def initial_maze(config):
    maze = [
        [
            {"north": True, "east": True, "south": True, "west": True} 
            for _ in range(config["width"])
        ] 
        for _ in range(config["height"])
    ]
    return maze


# Hex reading part
def convert_maze_col(col):
    i = 0
    if col["north"]: i += 8
    if col["east"]: i += 4
    if col["south"]: i += 2
    if col["west"]: i += 1
    return hex(i)[2:]


def print_maze_hex(maze):
    for row in maze:
        for col in row:
            a = convert_maze_col(col)
            if a == 'a':
                print("A",end="")
            elif a == 'b':
                print("B",end="")
            elif a == 'c':
                print("C",end="")
            elif a == 'd':
                print("D",end="")
            elif a == 'e':
                print("E",end="")
            elif a == "f":
                print("F",end="")
            else:
                print(a, end="")
        print()

def check_neighbors(visited, row, col, height, width):
    neighbors = []
    if row - 1 >= 0 and not visited[row - 1][col]:
        neighbors.append(("north", row - 1, col))
    if row + 1 <= height - 1 and not visited[row + 1][col]:
        neighbors.append(("south", row + 1, col))
    if col - 1 >= 0 and not visited[row][col - 1]:
        neighbors.append(("west", row, col - 1))
    if col + 1 <= width - 1 and not visited[row][col + 1]:
        neighbors.append(("east", row, col + 1))
    return neighbors


def generate_perfect_maze(maze, visited, row, col, height, width):
    visited[row][col] = True
    neighbors = check_neighbors(visited, row, col, height, width)
    random.shuffle(neighbors)
    for direction, n_row, n_col in neighbors:
        if not visited[n_row][n_col]:
            maze[row][col][direction] = False
            if direction == "north":
                maze[n_row][n_col]["south"] = False
            elif direction == "south":
                maze[n_row][n_col]["north"] = False
            elif direction == "east":
                maze[n_row][n_col]["west"] = False
            elif direction == "west":
                maze[n_row][n_col]["east"] = False
            generate_perfect_maze(maze, visited, n_row, n_col, height, width)


def generate_imperfect_maze(maze, height, width, chance=0.1):
    directions = [
        ("north", -1, 0, "south"),
        ("south", 1, 0, "north"),
        ("west", 0, -1, "east"),
        ("east", 0, 1, "west")
    ]

    for row in range(height):
        for col in range(width):

            # random chance to break a wall
            if random.random() < chance:
                direction, dr, dc, opposite = random.choice(directions)

                new_row = row + dr
                new_col = col + dc

                # check bounds
                if 0 <= new_row < height and 0 <= new_col < width:
                    # remove wall both sides
                    maze[row][col][direction] = False
                    maze[new_row][new_col][opposite] = False


raw = read_file("config.txt")
output = parse_config(raw)


maze = initial_maze(output)

# Perfect Maze
visited = [
    [False for _ in range(output["width"])]
    for _ in range(output["height"])
]

start_row, start_col = output["entry"]
end_row, end_col = output["exit"]
if output["perfect"] == True:
    generate_perfect_maze(maze, visited, start_row, start_col, output["height"], output["width"])
else:
    generate_perfect_maze(maze, visited, start_row, start_col, output["height"], output["width"])
    generate_imperfect_maze(maze, output["height"], output["width"])

maze[start_row][start_col]["west"] = False
maze[end_row][end_col]["east"] = False

# ---------------- Print Maze ----------------
print_maze_hex(maze)
