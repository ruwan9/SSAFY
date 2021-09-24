from collections import deque

# BFS
def bfs(graph, start, visited):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드 방문처리
    visited[start] = True

    # queue가 빌 때까지 반복
    while queue:
        #queue에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        #해당 원소와 연결된, 아직 방문하지 않은 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# BFS 호출
bfs(graph, 1, visited)

"""
BFS: Breadth First Search
- 가까운 노드부터 탐색
- 큐 자료구조 사용(FIFO)
"""