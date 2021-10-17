import sys
sys.stdin = open('input_files/1260.txt')
from collections import deque


def dfs(graph, v, visited):
    global d_lst
    visited[v] = True
    d_lst.append(v)
    graph[v].sort()  # 작은 수부터 탐색하도록
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    global b_lst
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        b_lst.append(v)
        graph[v].sort()  # 작은 수부터 탑색하도록
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
d_lst = []
b_lst = []

for i in range(M):
    x, y = map(int, input().split())
    # 양방향
    graph[x].append(y)
    graph[y].append(x)

dfs(graph, V, visited)
visited = [False] * (N+1)
bfs(graph, V, visited)
print(*d_lst)
print(*b_lst)