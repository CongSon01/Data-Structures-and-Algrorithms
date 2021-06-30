
def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            if node == goal:
                return
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

dfs(graph, 'A', 'F')
