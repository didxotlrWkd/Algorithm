from collections import deque

#그래프가 딕셔너리 형태일때
def bfs_dict(start_node, graph):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        curr_node = queue.popleft()
        if curr_node == 'C':
            return curr_node

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return -1

graph_dict = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G'],
        'E': ['F'],
        'F': [],
        'G': []
}

bfs_dict('A',graph_dict)

#그래프가 2차원 배열일때
def bfs_2dArray(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()
        print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return -1

graph_2dArray = [
        ['O', 'O', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O', 'O', 'O'],
]

bfs_2dArray(0,0,graph_2dArray)