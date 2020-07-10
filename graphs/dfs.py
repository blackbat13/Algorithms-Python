from typing import List


def dfs(graph: List[List[int]], visited: List[bool], node: int) -> None:
    if visited[node]:
        return

    visited[node] = True
    print(f'Visited node: {node}')

    for new_node in graph[node]:
        if not visited[new_node]:
            dfs(graph, visited, new_node)


visited: List[bool] = []
graph: List[List[int]] = [[], [], [], [], [], [], []]
graph[0] = [1, 6]
graph[1] = [0, 6, 3, 2]
graph[2] = [1, 3]
graph[3] = [2, 1, 6, 4, 5]
graph[4] = [3, 5]
graph[5] = [4, 3, 6]
graph[6] = [0, 1, 3, 5]

for i in range(0, len(graph)):
    visited.append(False)

dfs(graph, visited, 0)
