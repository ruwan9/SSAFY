import heapq

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(graph, start):
    # 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 첫 정점의 거리는 0
    # 우선순위 큐
    queue = []
    heapq.heappush(queue, [distances[start], start])


    while queue:
        # 현재 노드, 현재 거리
        current_distance, current_node = heapq.heappop(queue)

        # 지금까지 최소 거리가 현재 거리보다 길면 continue
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances