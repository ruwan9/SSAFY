import sys
sys.stdin = open('input13-1.txt')
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

# BFS
queue = deque()
queue.append(X)

while queue:
  now = queue.popleft()

  for next_node in graph[now]:
    if distance[next_node] == -1:  # 방문하지 않았다면
      distance[next_node] = distance[now] + 1  # 최단 거리 갱신
      queue.append(next_node)
  
check = False
for i in range(1, N+1):
  if distance[i] == K:
    print(i)
    check = True

if check == False:
  print(-1)

"""
'모든 도로의 거리는 1' -> BFS 이용
1. 그래프 만들기
2. BFS 구현
- 방문하지 않았다면 최단 거리 갱신
3. 최단 거리가 K인 경우 check = True / 없는 경우 -1
"""