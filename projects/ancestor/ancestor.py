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
        # If target has no parents return -1 (no path)
        # print(node[0], node[1])
        if v:
            # Append path to list of paths
            paths.append(v)
            # print(paths)
    if len(paths) <= 1:
        # print(paths)
        return -1

    # for elment is list of paths
    longest = []
    for p in paths:
        if len(p) > len(longest):
            longest = p
        elif len(p) == len(longest):
            if p[0] < longest[0]:
                longest = p
    return longest[0]
            
            # Find largest len(path)




# class earliest_ancestor:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, vertex):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex] = set()
#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("That vertex does not exist")


#     def bfs(self, target):
        # """
        # Print each vertex in breadth-first order
        # beginning from starting_vertex.
        # """
        # If starting_vertex has no parents return -1





        # Create an empty set to store visited nodes
        # visited = set()
        # # Create an empty Queue and enqueue the starting vertex
        # q = Queue()
        # q.enqueue(starting_vertex)
        # # While the queue is not empty...
        # while q.size() > 0:
        #     # Dequeue the first vertex
        #     v = q.dequeue()
        #     # If that vertex has not been visited...
        #     if v not in visited:
        #         # Mark it as visited
        #         visited.add(v)
        #         print(v)
        #         # Then add all of its neighbors to the back of the queue
        #         for neighbor in self.vertices[v]:
        #             q.enqueue(neighbor)


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(10)
# for i in graph:

#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(4)
#     graph.add_vertex(11)
#     graph.add_vertex(3)
#     graph.add_vertex(5)
#     graph.add_vertex(8)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_vertex(9)
#     graph.add_edge(10, 1)
#     graph.add_edge(1, 3)
#     graph.add_edge(3, 6)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 5)
#     graph.add_edge(5, 7)
#     graph.add_edge(5, 6)
#     graph.add_edge(4, 8)
#     graph.add_edge(11, 8)
#     graph.add_edge(8, 9)


#     print(graph.vertices)


#     print(graph.bft(6))