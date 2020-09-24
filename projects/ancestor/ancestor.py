'''

Describe the problem in graphs termininology
what are our nodes?
what are our edges?

build your graph or write geetNeighbors()

Choose your fighter
Which alogorithm?

'''

def earliest_ancestor_fav(ancestors, starting_node):   
    hash_table = {}
    # initialize the solution with a value
    solution = starting_node

    for i in range(len(ancestors)):
        # populate hash_table where the key is the child, and the value current earliest ancestor (ancestors[i][0] gives us the earlier of the two possible ancestors because of the order ancestors are stored in the tuple)
        if not ancestors[i][1] in hash_table:
            hash_table[ancestors[i][1]] = ancestors[i][0]

    # While the value stored in solution exists as a key in the hash tabble, update the solution to that childs earliest ancestor
    while solution in hash_table:
        solution = hash_table[solution] 

    if solution != starting_node:
        return solution
    else:
        return -1


def earliest_ancestor_fav_verbose(ancestors, starting_node):   
    # for storing a list of ancestors for each node
    hash_table = {}
    # to use while looping through 
    iterating = True
    # initialize the solution with a value
    solution = starting_node
   
    print(solution)
    # iterate through the ancestors list
    for i in range(len(ancestors)):
        # populate hash_table where the key is the child, and the value current earliest ancestor (ancestors[i][0] gives us the earlier of the two possible ancestors because of the order ancestors are stored in the tuple)
        if not ancestors[i][1] in hash_table:
            hash_table[ancestors[i][1]] = ancestors[i][0]
        print(hash_table)

    while iterating:
        # if the value currently stored as the solution is in the hash_table, update the solution to that childs earliest ancestor
        if solution in hash_table:
            solution = hash_table[solution] 
        # if the value stored in solution is not in the hash_table, stop iterating
        else:
            iterating = False
    
    if solution != starting_node:
        return solution
    else:
        return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 2))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 10))

# Got help with this solution, it's probably more along the lines of what we were looking for, but it felt unnecessarily complex to me so I redid it in a way that makes sense to my brain (above)

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

def earliest_ancestor_graph(ancestors, starting_node):   
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

def earliest_ancestor_tim(ancestors, starting_node):
    pass
    ## iterate over all ancestors,
    ## add each node to the graph
    ## add each eduge to the graph

    ## run a traversal

    ## modify it so as you go, you keep track of the node that's farthers

# earliest_ancestor = earliest_ancestor_graph
earliest_ancestor = earliest_ancestor_graph

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 10))


