from queue import PriorityQueue

def ucs(graph, start, goal, weights):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            if node == goal:
                return
            for neighbour in graph[node]:
                if neighbour not in visited:
                        total_cost = int(cost) + weights.get((node, neighbour))
                        queue.put((total_cost, neighbour))


ucs_test_graph = {
        'S': ['A', 'B', 'C'],
        'A': ['S', 'G'],
        'B': ['S', 'G'],
        'C': ['S', 'G'],
        'G': ['A', 'B', 'C']
    }

ucs_test_weight = {
        ('S', 'A'): 1,
        ('S', 'B'): 5,
        ('S', 'C'): 15,
    
        ('A', 'G'): 10,
        ('A', 'S'): 1,
    
        ('B', 'S'): 5,
        ('B', 'G'): 5,
    
        ('C', 'S'): 15,
        ('C', 'G'): 5,
    
        ('G', 'A'): 10,
        ('G', 'B'): 5,
        ('G', 'C'): 5,
}
ucs(ucs_test_graph, 'S', 'G', ucs_test_weight)
