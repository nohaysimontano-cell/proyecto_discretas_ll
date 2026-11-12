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

def is_connected(graph):
    result = _connected(graph)
    print(f"is_connected: {result}")
    return result


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

def has_cycle(graph):
    result = _undirected_cycle(graph)
    print(f"has_cycle: {result}")
    return result


def is_tree(graph):
    result = len(graph.nodes()) > 0 and not _undirected_cycle(graph) and _connected(graph)
    print(f"is_tree: {result}")
    return result

def is_forest(graph):
    result = not _undirected_cycle(graph)
    print(f"is_forest: {result}")
    return result
                