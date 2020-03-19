from Queue import PriorityQueue


def uniformCostSearch(graph, start, end):
    start_node = graph.nodes[start]
    start_node.distanceToStart = 0
    to_visit = PriorityQueue()
    #We start with only the start node in our queue
    to_visit.put((start_node.distanceToStart, start_node))
    #We keep track of all the nodes that we already visited
    visited = set([])
    while True:
        if to_visit.empty():
            return None
        current_node = to_visit.get(block=False)[1]
        if current_node.id == end:
            #We found the end node and can return the distance
            return current_node.distanceToStart
        #Current node is added to the set of visited node
        visited.add(current_node.id)
        for neighbour_id, neighbour_distance in current_node.neighbours.items():
            neighbour = graph.nodes[neighbour_id]
            distance = current_node.distanceToStart + int(neighbour_distance)
            if distance<neighbour.distanceToStart:
                #We found a shorter path to this node and update it's distance to the start node
                neighbour.distanceToStart = distance
            if neighbour_id not in visited:
                #Add the neighbour to the queue
                to_visit.put((neighbour.distanceToStart, neighbour))


