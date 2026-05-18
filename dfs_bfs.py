graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS Function
def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# DFS Function
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Menu Driven Program
while True:

    print("\n--- MENU ---")
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("BFS Traversal:")
        bfs(graph, 'A')

    elif choice == 2:
        print("DFS Traversal:")
        visited = set()
        dfs(visited, graph, 'A')

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")