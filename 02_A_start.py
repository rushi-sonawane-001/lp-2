import heapq

def a_star(start, goal, graph, heuristic):

    open_list=[]
    heapq.heappush(open_list,(0,start))
    g_cost={start:0}
    parent={start:None}
    visited=set()

    while open_list:

        f , current = heapq.heappop(open_list)

        print("\nCurrent Node:",current)

        if current==goal:

            path=[]
            while current:
                path.append(current)
                current=parent[current]

            path.reverse()
            print("Final Path:",path)
            print("Total Cost:",g_cost[goal])

            return path

        visited.add(current)

        for neighbour,cost in graph[current]:
            new_g = g_cost[current] + cost
            if (neighbour not in g_cost) or (new_g < g_cost[neighbour]):
                g_cost[neighbour] = new_g
                f_value = new_g + heuristic[neighbour]
                parent[neighbour] = current
                heapq.heappush( open_list, (f_value,neighbour) )

    print("No path found")

def main() :

    map = {
        'S' : [('A', 1), ('B', 4)],
        'A' : [('B', 2), ('C', 5), ('D', 12)],
        'B' : [('C',2)],
        'C' : [('D',3)],
        'D' : []
    }

    heuristic_value = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 0, }

    start = 'S'
    goal = 'D'

    a_star(start, goal, map, heuristic_value)

main()
    