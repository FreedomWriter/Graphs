"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # adding this line would produce a bi-directional graph
            #self.vertices[v2].add(v1)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        queue = Queue()

        # Add starting vertex id
        queue.enqueue(starting_vertex)
        # Create set for visited verts
        visited = set()
        #while queue is not empty
        while queue.size() > 0:
            # dequeue a vert
            v = queue.dequeue()
            # if not visitied
            if v not in visited:
                # visit it
                print(v)
                # Mark as visited
                visited.add(v)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        stack = Stack()

        # Add starting vertex id
        stack.push(starting_vertex)
        # Create set for visited verts
        visited = set()
        #while stack is not empty
        while stack.size() > 0:
            # pop a vert
            v = stack.pop()
            # if not visitied
            if v not in visited:
                # visit it
                print(v)
                # Mark as visited
                visited.add(v)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    stack.push(neighbor)

    # def dft_recursive(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
    #     visited = set()

    #     def recursive_helper(starting_vertex):
    #         if starting_vertex not in visited:
    #             visited.add(starting_vertex)
    #             print(starting_vertex)
    #             for neighbor in self.get_neighbors(starting_vertex):
    #                 recursive_helper(neighbor)

    #     return recursive_helper(starting_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

     
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        # create an empty queue
        q = Queue()
        # enqueue a path to the starting vertex ID
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from the path
            last = path[-1]
            # if that vertex has not been visited
            if last not in visited:
                # check if it's the target
                if last == destination_vertex:
                    # if so, return the path
                    return path
                # mark it as visited
                visited.add(last)
                # then add a path to it's neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    # copy the path
                    new_path = list(path)
                    # append the neighbor to the back
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        # create an empty stack
        s = Stack()
        # push a path to the starting vertex ID
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            # dequeue the first path
            path = s.pop()
            # grab the last vertex from the path
            last = path[-1]
            # if that vertex has not been visited
            if last not in visited:
                # check if it's the target
                if last == destination_vertex:
                    # if so, return the path
                    return path
                # mark it as visited
                visited.add(last)
                # then add a path to it's neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    # copy the path
                    new_path = list(path)
                    # append the neighbor to the back
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if path is None:
            path= []

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return path_copy


            for neighbor in self.get_neighbors(starting_vertex):
                # print(visited, path_copy)
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
                




        

       



        
                    

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
