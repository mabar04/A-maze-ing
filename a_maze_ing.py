
def read_file(filename):
        config = {}
        with open(filename,"r") as file:
            for line in file:
                line = line.strip()
            
                if not line:
                    continue
                key,value = line.split("=",1)
                config[key] = value
        return config

def parse_config(config):
    width = int(config["WIDTH"])
    height = int(config["HEIGHT"])

    entry_x,entry_y = map(int,config["ENTRY"].split(","))
    exit_x,exit_y = map(int,config["EXIT"].split(","))

    output_file = config["OUTPUT_FILE"]
    perfect = config["PERFECT"]

    return {
        "width" : width,
        "height" : height,
        "entry" : (entry_x,entry_y),
        "exit" : (exit_x,exit_y),
        "output" : output_file,
        "perfect": perfect
    }

raw = read_file("config.txt")
output = parse_config(raw)

def initial_maze(input):
    maze = [
        [
            {"north" : True, "east" : True, "south": True, "west":True} for col in range(input["width"])
           
        ] for row in range(input["height"])
    ]
    return maze

maze = initial_maze(output)
def convert_maze_col(col):
    i = 0
    if col["north"]: i+= 8
    if col["east"]: i+= 4
    if col["south"]: i+= 2
    if col["west"]: i+= 1
    return hex(i)[2:]

def print_maze_hex(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            hex = convert_maze_col(maze[i][j])
            print(hex,end="") 


def generate_perfect_maze(maze, start_row, start_col,height,width):
    visited = [
        [False for _ in range(width)]
        for _ in range(height)
    ]
    visited[start_row][start_col] = True


start_row,start_col = output["entry"]
generate_perfect_maze(maze, start_row, start_col,output["height"],output["width"])
# if output["perfect"]:
#     generate_perfect_maze(maze, start_row, start_col)
# else:
#     generate_non_perfect_maze(maze, start_row, start_col)



