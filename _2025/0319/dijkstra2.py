import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    iter = 0
    while priority_queue:
        iter += 1
        print("iter: "+str(iter))
        current_distance, current_node = heapq.heappop(priority_queue)
        print("popped> distance: " + str(current_distance) + "  node: " + str(current_node))
        
        # If we found a shorter way to this node, skip processing
        if current_distance > shortest_distances[current_node]:
            print("distance is greater than shortest, pass")
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                print(f'updated shortest distance for {neighbor} as {distance}')
                heapq.heappush(priority_queue, (distance, neighbor))
                print(f'added: {distance},{neighbor} to que!')
            else:
                print("didnt update!")
    
    return shortest_distances

# Example graph (Adjacency list representation)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
