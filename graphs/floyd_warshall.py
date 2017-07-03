def floyd_warshall(graph):
    for i in range(0, len(graph)):
        for j in range(0, len(graph)):
            for k in range(0, len(graph)):
                if i == j or k == i or k == j:
                    continue

                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


f = 1000000000
graph = [[], [], [], [], [], [], []]
graph[0] = [0, 5, f, f, f, f, 5]
graph[1] = [5, 0, 3, 3, f, f, 5]
graph[2] = [f, 3, 0, 1, f, f, f]
graph[3] = [f, 3, 1, 0, 5, 4, 3]
graph[4] = [f, f, f, 5, 0, 2, f]
graph[5] = [f, f, f, 4, 2, 0, 5]
graph[6] = [5, 5, f, 3, f, 5, 0]

floyd_warshall(graph)

for row in graph:
    print(row)
