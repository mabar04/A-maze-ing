from collections import deque


class BFS:

    @classmethod
    def find_path(cls, maze, entry, exit, height, width):
        queue = deque()
        queue.append(entry)
        visited = {entry}
        parent = {(entry, "None"): None}
        while queue:
            row, col = queue.popleft()
            if (row, col) == exit:
                break
            for direction, n_row, n_col in cls.get_neighbors(maze, row, col,
                                                             height, width):
                if (n_row, n_col) not in visited:
                    visited.add((n_row, n_col))
                    parent[(n_row, n_col, direction)] = (row, col, direction)
                    queue.append((n_row, n_col))

