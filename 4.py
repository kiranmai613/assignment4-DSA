from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_trees(self):
        visited = [False] * (len(self.graph) + 1)
        count = 0
        for node in self.graph:
            if not visited[node]:
                self.dfs(node, visited)
                count += 1
        return count
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(7, 8)

num_trees = g.count_trees()
print(f"Number of trees in the forest: {num_trees}")
