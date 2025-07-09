def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    traversal_order = []
    def dfs_recursive(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in the graph.")
        return []
    dfs_recursive(start_node)
    return traversal_order
if __name__ == "__main__":
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H'],
        'F': [],
        'G': [],
        'H': []
    }
    print("DFS Traversal starting from 'A':")
    dfs_result = dfs(sample_graph, 'A')
    print(dfs_result)  # Expected: ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
