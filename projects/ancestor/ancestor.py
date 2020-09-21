class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):   
    # dfs - use a stack 
    s = Stack()
    # keep track of the earliest_ancestor, initialized with the starting_node
    earliest_list = [[starting_node]]
    # get the neighbors
    neighbors = find_neighbors(starting_node, ancestors)
    
    # no neighbors then return -1
    if len(neighbors) == 0:
        return -1

    # add the neighbors to the stack
    s.push(neighbors)
    # keep track of the earliest_ancestor
    earliest_list.append(neighbors)

    # while stack still has items
    while s.size() > 0:
        # get the top item in the stack
        curr = s.pop()
        # iterate through the tuple
        for el in curr:
            # find the neighbors of each num in the tuple
            next_node = find_neighbors(el, ancestors)
            # if the neighbor exists
            if len(next_node) != 0:
                # add the neighbors to the stack
                s.push(next_node)
                # keep track of the ancestors
                earliest_list.append(next_node)

    # isolate and return the first number in the tupple of the last added ancestor (the earliest) 
    last = earliest_list[-1][0]

    return last


def find_neighbors(child, arr):
    neighbors = []
    # iterate through the list
    for neighbor in arr:
        # if the first num in the list is the given child, it's a neighbor, add it to the list
        if neighbor[1] == child:
            neighbors.append(neighbor[0])
    # return the list of neighbors
    return neighbors

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 10))

