from collections import defaultdict

# Define a Graph class
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited.add(start)
        print(start, end=' ')

        for i in self.graph[start]:
            if i not in visited:
                self.dfs(i, visited)

# Create a graph and add edges to it
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)

# Perform DFS starting from vertex 0
print("DFS Traversal:")
visited = set()
g.dfs(0, visited)
