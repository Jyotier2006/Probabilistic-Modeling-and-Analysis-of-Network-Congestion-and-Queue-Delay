class QueueDelayGraph:
    def __init__(self, n, edges, queue_len, service_rate, coords):
        self.n = n
        self.edges = edges
        self.queue_len = queue_len
        self.service_rate = service_rate
        self.coords = coords
        self.graph = [[] for _ in range(n)]
        self.build_graph()

    def node_delay(self, node):
        return self.queue_len[node] / self.service_rate[node]

    def build_graph(self):
        for u, v in self.edges:
            w = self.node_delay(v)
            self.graph[u].append((v, w))

    def reconstruct_path(self, parent, source, dest):
        if dest != source and parent[dest] == -1:
            return None
        path = []
        cur = dest
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        return path
