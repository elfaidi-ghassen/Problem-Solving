from collections import deque
import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

direction = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1)
}

def dfs_detect_cycle(i, j, seen, call_stack):    
    seen[i][j] = True
    d = grid[i][j]
    xi = i + direction[d][0]
    xj = j + direction[d][1]
    if xi < 0 or xj < 0 or xi >= n or xj >= m:
        return False, -1, -1
    
    call_stack[i][j] = True
    
    if seen[xi][xj] and call_stack[xi][xj]:
        return True, xi, xj
    if not seen[xi][xj]:
        val, ii, jj = dfs_detect_cycle(xi, xj, seen, call_stack)
        if val:
            return True, ii, jj

    call_stack[i][j] = False
    return False, -1, -1

def bfs_count_until(grid, i, j, target_i, target_j):
    if (i, j) == (target_i, target_j):
        return 0
    to_visit = deque()
    seen = [[False] * m for _ in range(n)]
    seen[i][j] = True
    to_visit.append((i, j))
    count = 0
    while to_visit:
        nodei, nodej = to_visit.popleft()
        d = grid[nodei][nodej]
        xi = nodei + direction[d][0]
        xj = nodej + direction[d][1]
        if xi < 0 or xj < 0 or xi >= n or xj >= m or seen[xi][xj]:
            continue
        count += 1
        if (xi, xj) == (target_i, target_j):
            return count
        seen[xi][xj] = True
        to_visit.append((xi, xj))
    return -1
while True:
    n, m, c = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    
    seen = [[False] * m for _ in range(n)]
    call_stack = [[False] * m for _ in range(n)]
    has_cycle, xi, xj = dfs_detect_cycle(0, c - 1, seen, call_stack)
    
    total = 0
    for i in range(n):
        for j in range(m):
            if seen[i][j] == True:
                total += 1

    if has_cycle:
        count = bfs_count_until(grid, 0, c - 1, xi, xj)
        print(f"{count} step(s) before a loop of {total - count} step(s)")
    else:
        print(f"{total} step(s) to exit")