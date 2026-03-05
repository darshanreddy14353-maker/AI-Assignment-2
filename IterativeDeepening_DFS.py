def dls(graph, node, depth, visited):

    if depth < 0:
        return

    visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dls(graph, neighbour, depth-1, visited)


def iddfs(graph, start, max_depth):

    for depth in range(max_depth+1):

        visited = []
        dls(graph, start, depth, visited)

        print("Depth", depth, ":", visited)


graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

iddfs(graph,'A',3)
