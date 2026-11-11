def is_connected(graph):
    nodes = graph.nodes()
    if len(nodes) == 0:
        result = True
    else:
        visited = set()
        stack = [nodes[0]]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)
        result = len(visited) == len(nodes)

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
                