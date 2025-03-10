import sys, os 
from collections import deque

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt") 

di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [-1, 1, 0, 0, 1, -1, 1, -1]
def bfs(grid, i, j):
    to_visit = deque()
    to_visit.append((i, j))
    grid[i][j] = "."
    while to_visit:
        nodei, nodej = to_visit.popleft()
        for k in range(8):
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if xi < 0 or xj < 0 or xi >= n or xj >= m:
                continue
            if grid[xi][xj] != "#":
                continue
            grid[xi][xj] = "."
            to_visit.append((xi, xj))


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            bfs(grid, i, j)
            count += 1
print(count)