class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            p = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = p[-1]
            # IF VERTEX = TARGET, RETURN PATH
            if v == destination_vertex:
                return p
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                for neighbor in self.vertices[v]:
                    new_path = list(p)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                # Then add A PATH TO all of its neighbors to the back of the queue
                    # Copy the path
                    # Append neighbor to the back of the copy
                    # Enqueue copy

def earliest_ancestor(graph, target):
    # populate the graph data structure
    data = Graph()
    for i in graph:
        data.add_vertex(i[0])
        data.add_vertex(i[1])
    for i in graph:
        data.add_edge(i[0], i[1])
    # Loop through every node
    paths = []
    for node in graph:
        # Perform BFS from node -> target
        v = data.bfs(node[0], target)
        if v:
            # Append path to list of paths
            paths.append(v)

    # for elment is list of paths
    longest = []
    for p in paths:
        if len(p) > len(longest):
            longest = p
        elif len(p) == len(longest):
            if p[0] < longest[0]:
                longest = p
    if len(longest) == 1:
        return -1
    return longest[0]