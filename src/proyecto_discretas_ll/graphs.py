class UndiretedGraph:
    def __init__(self):
        self._adjacency = {}

    def add_node(self, node):
        if node not in self._adjacency:
            self._adjacency[node] = {}

    def add_edge(self, source, target, weight=1):
        self.add_node(source)
        self.add_node(target)

        self._adjacency[source][target] = weight
        self._adjacency[target][source] = weight

    def nodes(self):
        return list(self._adjacency)

    def neighbors(self, node):
        return self._adjacency[node]

class DirectedGraph:
    def __init__(self):
        self._adjacency = {}

    def add_node(self, node):
        if node not in self._adjacency:
            self._adjacency[node] = {}

    def add_edge(self, source, target, weight=1):
        self.add_node(source)
        self.add_node(target)

        self._adjacency[source][target] = weight

    def nodes(self):
        return list(self._adjacency)

    def neighbors(self, node):
        return self._adjacency[node]
    