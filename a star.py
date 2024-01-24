# If we have to reach from one place to another place there exist 
#several paths. Write a Python Program to find the shortest distance between any two 
#places using a A* search algorithm.


import heapq

Map_taken_as_example = {
    'S': {'A':1,'G':10},

    'A': {'B':2, 'C':2, 'S':1},
    'B': {'D':5, 'A':2},
    'C': {'D':3, 'G':6, 'A':2},
    'D': {'G':2, 'C':3, 'B':5},
    'G': {'S':10, 'C':6, 'D':2},

}

# Define the heuristic function (straight-line distance to G)
heuristic1 = {
    'S': 15,
    'A': 4,

    'B': 7,
    'C': 5,
    'D': 9,
    'G': 0
}

def a_star_search(graph, start, goal, heuristic1):
    open_list = [(0, start)]
    closed_set = set()
    g_score = {location: float('inf') for location in graph}
    g_score[start] = 0
    
    while open_list:
        current_g, node_current = heapq.heappop(open_list)
        if node_current == goal:
            return g_score[goal]
        
        if node_current in closed_set:
            continue
        
        closed_set.add(node_current)
        
        for neighbor, distance in graph[node_current].items():
            tentative_g = g_score[node_current] + distance

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic1[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
    return float('inf') # If no path is found

location_to_start = 'S'
location_of_goal = 'G'
shortest_distance = a_star_search(Map_taken_as_example, location_to_start, location_of_goal, heuristic1)
if shortest_distance < float('inf'):
    print(f"The shortest distance from node {location_to_start} to node {location_of_goal} is {shortest_distance} km.")
else:
    print(f"No path found from node {location_to_start} to node {location_of_goal}.")

