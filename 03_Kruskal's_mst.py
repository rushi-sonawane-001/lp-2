# Kruskal's Minimum Spanning Tree Algorithm

edges = [

    ['A', 'B', 4],
    ['A', 'C', 4],
    ['B', 'C', 2],
    ['B', 'D', 3],
    ['B', 'E', 1],
    ['D', 'F', 2],
    ['E', 'F', 3]
]

# Sort edges by weight
edges.sort(key=lambda x: x[2])

parent = {}

# Find function
def find(node):

    if parent[node] == node:
        return node

    return find(parent[node])

# Union function
def union(a, b):

    rootA = find(a)
    rootB = find(b)

    parent[rootB] = rootA

# Create parent for each node
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

for node in nodes:
    parent[node] = node

mst = []
cost = 0

# Kruskal Algorithm
for edge in edges:

    u = edge[0]
    v = edge[1]
    w = edge[2]

    # Check cycle
    if find(u) != find(v):

        union(u, v)

        mst.append(edge)

        cost += w

# Output
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge[0], "-", edge[1], "=", edge[2])

print("Total Cost =", cost)