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


# DFS, 재귀 사용
def dfs(graph, v, visited):  # 시작점 v
    visited[v] = True  # 방문처리
    print(v, end=' ')

    for i in graph[v]:  # 다음으로 방문할 노드 중
        if visited[i] == 0:  # 방문하지 않았다면
            dfs(graph, i, visited)  # 다음 점 i에서 dfs
dfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5