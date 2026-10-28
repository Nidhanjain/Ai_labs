# Experiment 3: Goal-Based Agent - Grid Navigation using BFS
from collections import deque

grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]  # 0=free, 1=obstacle

def find_path(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        (r, c), path = q.popleft()
        if (r, c) == goal:
            return path
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                and grid[nr][nc] == 0 and (nr, nc) not in seen):
                seen.add((nr, nc))
                q.append(((nr, nc), path + [(nr, nc)]))
    return None

print("Path:", find_path((0, 0), (2, 2)))
