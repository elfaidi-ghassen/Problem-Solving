from collections import deque
import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def bfs(i, j, grid, nb_points, nb):
    to_visit = deque()
    to_visit.appendleft((i, j))
    grid[i][j] = "~"
    while to_visit:
        nodei, nodej = to_visit.pop()
        
        for k in range(4):
            if nb_points == nb + 1: 
                break
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if (xi < 0 or xj < 0 or xi >= n or xj >= m):
                continue
            if (grid[xi][xj] in ["#", "~"]):
                continue
            
            grid[xi][xj] = "~"
            to_visit.append((xi, xj))
            nb_points -= 1


n, m, k = map(int, input().split())

grid = []
for _ in range(n):
    line = input()
    grid.append(list(line))

nb_points = 0
starti, startj = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            nb_points += 1
            starti = i
            startj = j

bfs(starti, startj, grid, nb_points, k)

for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            grid[i][j] = "X"
        elif grid[i][j] == "~":
            grid[i][j] = "."

for line in grid:
    print("".join(line))
