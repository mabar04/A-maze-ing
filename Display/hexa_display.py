

class hexa_display:
    @classmethod
    def convert_maze_col(cls, col):
        i = 0
        if col["north"]:
            i += 8
        if col["east"]:
            i += 4
        if col["south"]:
            i += 2
        if col["west"]:
            i += 1
        return hex(i)[2]

    @classmethod
    def print_maze_hex(cls, maze, parsed_values):
        with open(parsed_values["output"], "w") as maze_file:
            for row in maze:
                for col in row:
                    a = cls.convert_maze_col(col)
                    if a == 'a':
                        maze_file.write("A")
                    elif a == 'b':
                        maze_file.write("B")
                    elif a == 'c':
                        maze_file.write("C")
                    elif a == 'd':
                        maze_file.write("D")
                    elif a == 'e':
                        maze_file.write("E")
                    elif a == "f":
                        maze_file.write("F")
                    else:
                        maze_file.write(a)
                maze_file.write("\n")
            # maze_file.write("\n")
            # maze_file.write(str(parsed_values["entry"]))
            # maze_file.write("\n")
            # maze_file.write(str(parsed_values["exit"]))
