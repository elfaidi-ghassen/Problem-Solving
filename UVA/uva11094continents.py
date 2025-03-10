import sys, os 
from collections import deque

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt") 


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def bfs(grid, i, j):
    to_visit = deque()
    to_visit.append((i, j))
    grid[i][j] = ""
    count = 1
    while to_visit:
        nodei, nodej = to_visit.pop()
        for k in range(4):
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if xi < 0 or xi >= n:
                continue
            xj = xj % m
            if grid[xi][xj] != land:
                continue
            
            grid[xi][xj] = ""
            to_visit.append((xi, xj))
            count += 1
    return count



while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    pi, pj = map(int, input().split())
    land = grid[pi][pj]
    bfs(grid, pi, pj)
    mx = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == land:
                mx = max(mx, bfs(grid, i, j))
    print(mx)
    try:
        input()
    except:
        break