from collections import deque
# graph = [
#     [0, 1 , 1],
#     [1, 0 , 1],
#     [1, 1 , 0],
# ]

graph = [ [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


def get_nodes(node, graph):
    return [i for i in range(len(graph)) if graph[node][i] == 1]

visited = set()
parent = [-1] * len(graph)
def directed_contains_cycles(start, graph, parent):
    visited.add(start)
    for node in get_nodes(start, graph):
        if node in visited:
            return True
        elif node not in visited:
            parent[node] = start
            val = directed_contains_cycles(node, graph, list(parent))
            parent[node] = -1
            return val
    return False
print(directed_contains_cycles(0, graph, [-1] * len(graph)))


def contains_cycles(start, graph):
    to_visit = deque([start])
    visited = set([start])
    parents = [None] * len(graph)
    while to_visit:
        first = to_visit.popleft()
        for neighbor in get_nodes(first, graph):
            if neighbor in visited:
                if parents[neighbor] != first:
                    return True
            else:
                to_visit.append(neighbor)
                visited.add(neighbor)
                parents[neighbor] = first
    return False

# print(rec_contains_cycles(0, graph))