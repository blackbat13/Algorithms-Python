from typing import List


def dijkstra(graph: List[List[(int, int)]], node: int) -> List[int]:
    distances: List[int] = []
    queue: List[(int, int, int)] = []

    for i in range(len(graph)):
        distances.append(10000000)
    distances[node] = 0

    for (next_node, distance) in graph[node]:
        queue.append((node, next_node, distance))

    while len(queue) > 0:
        node = queue[0][1]
        from_node = queue[0][0]
        new_distance = distances[from_node] + queue[0][2]
        queue.pop(0)
        if new_distance < distances[node]:
            distances[node] = new_distance
            for (next_node, distance) in graph[node]:
                queue.append((node, next_node, distance))

    return distances


graph: List[List[(int, int)]] = [[], [], [], [], [], [], []]
graph[0] = [(1, 5), (6, 5)]
graph[1] = [(0, 5), (6, 5), (3, 3), (2, 3)]
graph[2] = [(1, 3), (3, 1)]
graph[3] = [(2, 1), (1, 3), (6, 3), (4, 5), (5, 4)]
graph[4] = [(3, 5), (5, 2)]
graph[5] = [(4, 2), (3, 4), (6, 5)]
graph[6] = [(0, 5), (1, 5), (3, 3), (5, 5)]

print(dijkstra(graph, 0))
