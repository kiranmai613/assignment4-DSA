from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * (len(self.graph)+1)
        queue = deque()

        visited[start] = True
        queue.append(start)

        while queue:
            start = queue.popleft()
            print(start, end=' ')

            for i in self.graph[start]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

# Create a graph and add edges to it
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)

# Perform BFS starting from vertex 0
print("BFS Traversal:")
g.bfs(0)

