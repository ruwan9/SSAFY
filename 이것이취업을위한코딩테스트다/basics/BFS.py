graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
N = len(graph)
visited = [False] * N

# BFS, queue 사용
from collections import deque


def bfs(graph, start, visited):  # 시작점 start
    queue = deque([start])  # 사용할 Queue
    visited[start] = True  # 방문처리

    while queue:
        v = queue.popleft()  # 시작점 v
        print(v, end=' ')

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = True
bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6