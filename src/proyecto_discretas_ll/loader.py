from .graphs import UndirectedGraph, DirectedGraph


def load_graph(path, directed=False):
    if directed:
        graph = DirectedGraph()
    else:
        graph = UndirectedGraph()
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            source, target, weight = line.split(",")
            if source == "source":
                continue
            graph.add_edge(source, target, int(weight))
    return graph