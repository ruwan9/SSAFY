import sys
sys.stdin = open('input2.txt')
from collections import deque

N, M = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(N))
print(graph)

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if graph[nr][nc] == 0:
                continue

            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                print(graph)
                queue.append((nr, nc))

    return graph[N-1][M-1]

print(bfs(0, 0))
