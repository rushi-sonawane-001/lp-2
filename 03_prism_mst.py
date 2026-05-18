# Prim's Minimum Spanning Tree Algorithm

graph = {

    'A': [('B', 4), ('C', 4)],

    'B': [('A', 4), ('C', 2), ('D', 3), ('E', 1), ('F', 6)],

    'C': [('A', 4), ('B', 2)],

    'D': [('B', 3), ('F', 2)],

    'E': [('B', 1), ('F', 3)],

    'F': [('D', 2), ('E', 3)]
}

visited = []
mst = []

start = 'A'

visited.append(start)

cost = 0

# Run until all nodes are visited
while len(visited) < len(graph):

    minimum = 999

    x = ''
    y = ''

    # Check all visited nodes
    for node in visited:

        for neighbour, weight in graph[node]:

            if neighbour not in visited:

                if weight < minimum:

                    minimum = weight

                    x = node
                    y = neighbour

    visited.append(y)

    mst.append((x, y, minimum))

    cost += minimum

# Output
print("Minimum Spanning Tree:\n")

for x, y, weight in mst:
    print(x, "->", y, "=", weight)

print("\nTotal Cost =", cost)