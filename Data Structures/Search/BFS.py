


def bfs(graph, start, goal):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            if node == goal:
                return
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}


bfs(graph, 'A', 'F')