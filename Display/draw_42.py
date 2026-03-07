class draw_42:
    @classmethod
    def draw_42(cls, maze, height, width):
        center_row = height // 2
        center_col = width // 2
        start_row = center_row - 2
        start_col = center_col - 3

        blocked = set()
        pattern = [
            (0, 0), (0, 2), (0, 4), (0, 5),
            (1, 0), (1, 2), (1, 5),
            (2, 0), (2, 1), (2, 2), (2, 4), (2, 5),
            (3, 2), (3, 4),
            (4, 2), (4, 4), (4, 5)
        ]

        for dr, dc in pattern:
            blocked.add((start_row + dr, start_col + dc))

        for (row, col) in blocked:
            maze[row][col]["north"] = True
            maze[row][col]["south"] = True
            maze[row][col]["east"] = True
            maze[row][col]["west"] = True
            maze[row][col]["visited"] = True
