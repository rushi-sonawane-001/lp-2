import sys

def solve(graph, v, start) :
    infinite = sys.maxsize

    explored = {node : False for node in graph}
    distance = {node : infinite for node in graph}
    distance[start] = 0 

    count = v
    while (count) :
        currNode = " "
        value = infinite

        for n in graph:
            if( not explored[n] and value > distance[n]) :
                currNode = n
                value = distance[n]
        
        explored[currNode] = True
        
        for n in graph[currNode] :
            neighbour = n[0]
            weight = n[1]
            if( not explored[neighbour] and distance[currNode] + weight < distance[neighbour]) :
                distance[neighbour] = distance[currNode] + weight
        
        count -= 1

    return distance
    


def main() :

    graph = {
        'A' : [ ('B', 4), ('C', 4)],
        'B' : [ ('A', 4), ('C', 2), ('D', 3), ('E', 1), ('F', 6)],
        'C' : [ ('A', 4), ('B', 2)],
        'D' : [ ('B', 3), ('F', 2)],
        'E' : [ ('B', 1), ('F', 3)],
        'F' : [ ('D', 2), ('E', 3)],
    }

    v = len(graph)
    
    start = 'A'

    result = solve(graph, v, start)
    
    print("\nShortest Distance ---->\n")
    for node in result:
        print(f"{start} -> {node} = {result[node]}")
   
main()
