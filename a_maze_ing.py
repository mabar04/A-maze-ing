import random

# ---------------- Config Parsing ----------------
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

    entry_col, entry_row = map(int, config["ENTRY"].split(","))  # x = col, y = row
    exit_col, exit_row = map(int, config["EXIT"].split(","))

    output_file = config["OUTPUT_FILE"]
    perfect = config["PERFECT"]

    return {
        "width": width,
        "height": height,
        "entry": (entry_row, entry_col),  # row, col
        "exit": (exit_row, exit_col),     # row, col  <-- FIXED
        "output": output_file,
        "perfect": perfect
    }

raw = read_file("config.txt")
output = parse_config(raw)

# ---------------- Maze Initialization ----------------
def initial_maze(config):
    maze = [
        [
            {"north": True, "east": True, "south": True, "west": True} 
            for _ in range(config["width"])
        ] 
        for _ in range(config["height"])
    ]
    return maze

maze = initial_maze(output)

# ---------------- Convert to Hex ----------------
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
            print(convert_maze_col(col), end="")
        print()

# ---------------- DFS Perfect Maze ----------------
visited = [
    [False for _ in range(output["width"])]
    for _ in range(output["height"])
]

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
            # Remove walls between current cell and neighbor
            maze[row][col][direction] = False
            if direction == "north":
                maze[n_row][n_col]["south"] = False
            elif direction == "south":
                maze[n_row][n_col]["north"] = False
            elif direction == "east":
                maze[n_row][n_col]["west"] = False
            elif direction == "west":
                maze[n_row][n_col]["east"] = False
            
            visited[n_row][n_col] = True  # mark visited before recursion
            generate_perfect_maze(maze, visited, n_row, n_col, height, width)

# ---------------- Run Maze Generation ----------------
start_row, start_col = output["entry"]
end_row, end_col = output["exit"]

generate_perfect_maze(maze, visited, start_row, start_col, output["height"], output["width"])

# Open entry/exit walls
maze[start_row][start_col]["west"] = False
maze[end_row][end_col]["east"] = False

# ---------------- Print Maze ----------------
print_maze_hex(maze)
