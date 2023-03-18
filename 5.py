from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True
        recursion_stack[node] = False
        return False

    def has_cycle(self):
        visited = [False] * (len(self.graph) + 1)
        recursion_stack = [False] * (len(self.graph) + 1)
        for node in self.graph:
            if not visited[node]:
                if self.dfs(node, visited, recursion_stack):
                    return True
        return False
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(4, 5)
g.add_edge(5, 6)

has_cycle = g.has_cycle()
if has_cycle:
    print("Cycle detected in graph")
else:
    print("No cycle detected in graph")
