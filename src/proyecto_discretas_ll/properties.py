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