def depth_limited_dfs(graph, node, depth, visited):

    if depth < 0:
        return

    visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            depth_limited_dfs(graph, neighbour, depth-1, visited)

    return visited


graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

print("Depth Limited DFS:", depth_limited_dfs(graph,'A',2,visited))
