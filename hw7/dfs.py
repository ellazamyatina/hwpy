class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        if start not in self.graph:
            return []

        visited = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

    def __iter__(self):
        if not self.graph:
            return iter([])
        start_vertex = list(self.graph.keys())[0]
        return iter(self.dfs(start_vertex))
