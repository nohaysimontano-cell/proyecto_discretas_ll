class UndirectedGraph:
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

    def adjacent_nodes(self, node):
        return set(self._adjacency[node])

    


class DirectedGraph:
    def __init__(self):
        self._adjacency = {}
        self._incoming = {}

    def add_node(self, node):
        if node not in self._adjacency:
            self._adjacency[node] = {}
            self._incoming[node] = set()

    def add_edge(self, source, target, weight=1):
        self.add_node(source)
        self.add_node(target)


        self._adjacency[source][target] = weight
        self._incoming[target].add(source)
        
    def nodes(self):
        return list(self._adjacency)

    def neighbors(self, node):
        return self._adjacency[node]

    def adjacent_nodes(self, node):
        return set(self._adjacency[node]) | self._incoming[node]

        
    def in_degree(self, node):
        return len(self._incoming[node])