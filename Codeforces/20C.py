import sys, os 
from queue import PriorityQueue

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt")

n, m = map(int, input().split())
MAX = (10 ** 18) + 1
graph = [[] for _ in range(n)]
cost = [None] * n
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

previous = [-1] * n
def dijkstra(start_node):
    pq = PriorityQueue()
    visited = [False] * n
    for i in range(n):
        cost[i] = MAX
    cost[start_node] = 0
    pq.put((cost[start_node], start_node))
    while not pq.empty():
        cost_so_far, node = pq.get()
        if visited[node]:
            continue
        visited[node] = True
            
        for neighbor in graph[node]:
            neighbor_node, edge_cost = neighbor
            if visited[neighbor_node]:
                continue
            if cost_so_far + edge_cost < cost[neighbor_node]:
                cost[neighbor_node] = cost_so_far + edge_cost
                pq.put((cost[neighbor_node], neighbor_node))
                previous[neighbor_node] = node
dijkstra(0)
if cost[n - 1] == MAX:
    print(-1)
else:
    path = []
    node = n - 1
    while node != -1:
        path.append(node)
        node = previous[node]
    path.reverse()
    print(" ".join(map(lambda x : str(x + 1), path)))