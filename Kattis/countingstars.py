import sys, os 
from collections import deque

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt") 

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]

def bfs(grid, i, j):
    to_visit = deque()
    to_visit.append((i, j))
    grid[i][j] = "."
    while to_visit:
        nodei, nodej = to_visit.popleft()
        for k in range(4):
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if xi < 0 or xj < 0 or xi >= m or xj >= n:
                continue
            if grid[xi][xj] != "-":
                continue
            grid[xi][xj] = "."
            to_visit.append((xi, xj))

t = 0
while True:
    t += 1
    try:
        m, n = map(int, input().split())
        grid = []
        for _ in range(m):
            grid.append(list(input()))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "-":
                    count += 1
                    bfs(grid, i, j)
        print(f"Case {t}: {count}")
    except EOFError:
        break
