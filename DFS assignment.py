# Define the DFS function
def dfs(graph, start, destination, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    
    # Check if the start is the destination
    if start == destination:
        return True

    # Visit each adjacent node
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, destination, visited):
                return True

    return False

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run the DFS function to check if there's a path from 'A' to 'F'
root = 'A'
destination = 'F'
result = dfs(graph, root, destination)

print(f"Path from {root} to {destination}: {'Found' if result else 'Not Found'}")
