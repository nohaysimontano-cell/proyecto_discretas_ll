from .graphs import DirectedGraph


def _connected(graph):
    nodes = graph.nodes()
    if len(nodes) == 0:
        return True

    visited = set()
    stack = [nodes[0]]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.adjacent_nodes(node):
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited) == len(nodes)


def _undirected_cycle(graph):
    visited = set()
    for start in graph.nodes():
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, None)]
        while stack:
            node, parent = stack.pop()
            for neighbor in graph.neighbors(node):
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return True
                visited.add(neighbor)
                stack.append((neighbor, node))

    return False


def _directed_cycle(graph):
    visiting = set()
    done = set()

    def visit(node):
        visiting.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor in visiting:
                return True
            if neighbor not in done and visit(neighbor):
                return True
        visiting.remove(node)
        done.add(node)
        return False

    for start in graph.nodes():
        if start not in done and visit(start):
            return True
    return False


def _cycle(graph):
    if isinstance(graph, DirectedGraph):
        return _directed_cycle(graph)
    return _undirected_cycle(graph)


def _in_degrees_ok(graph):
    if not isinstance(graph, DirectedGraph):
        return True
    for node in graph.nodes():
        if graph.in_degree(node) > 1:
            return False
    return True


def is_connected(graph):
    result = _connected(graph)
    print(f"is_connected: {result}")
    return result


def has_cycle(graph):
    result = _cycle(graph)
    print(f"has_cycle: {result}")
    return result


def is_tree(graph):
    result = (
        len(graph.nodes()) > 0
        and _in_degrees_ok(graph)
        and not _cycle(graph)
        and _connected(graph)
    )
    print(f"is_tree: {result}")
    return result


def is_forest(graph):
    result = _in_degrees_ok(graph) and not _cycle(graph)
    print(f"is_forest: {result}")
    return result