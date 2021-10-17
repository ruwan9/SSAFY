def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적 방문
    for i in graph[v]:
        if not visited[i]:  # if visited[i] == False:
            dfs(graph, i, visited)

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

# DFS 호출
dfs(graph, 1, visited)

"""
DFS: Depth First Search
- 깊은 부분 우선 탐색
- 스택 자료구조 사용(LIFO)
"""