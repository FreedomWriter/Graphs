# """
# Given two words (begin_word and end_word), and a dictionar's word list, 
# return the shortest transformation sequence from being_word to end_word, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

# return None if it can't be done
# all words are lowercase (or you can make them lowercase)

# 'sail' ==> 'boat

# 1. Graphs terminology
# - Nodes: words!
# - Edges: a word is connected to another if they share all letters except one

# 2. getNeighbors - graph optional

# 3. Choose Algorithm: Breadth first search

# """
# import string
# word_list = set()

# def find_neighbors_alt(word):
#     ## for every letter in the word, substitue a letter of the alphabet 0(len(word) * 26)
#     # check if new word is in our giant word list O(1)
#     # If so, it's a neighbor
#     for i in range(len(word)):
#         for alpha_letter in string.ascii_lowercase
#         word_arr = list(word)
#         word_arr[i] = alpha_letter

#         mayboe_neighbor = "".join(word_arr)

#         if maybe_neighborin word_list and maybe

# # def find_neighbors(something):
# #     # find all wors that re the same in length
# #     same_length = [word for word in all_the_words if len(word) == len(something)]
# #     matches = []

# #     #count how many letters are the same to see if each word is an edge
# #     for word in same_length:
# #         chars = split(word)
# #         match = split(something)
# #         count = 0
# #         for i in range(0, len(chars)):
# #             if chars[i] == match[i]:
# #                 count += 1
# #         if count == len(something) - 1:
# #             matches.append(word)
# #     return matches

# def bfs(start_word, end_word):
#     q  = Queue()
#     visited = set()

#     q.enqueue([start_word]) # path to the start word

#     while q.size() > 0:
#         current_path = q.dequeue()
#         current_word = current_path[-1]

#         if current_word == end_word:
#             return current_path

#         if current_word not in visited:
#             visited.add(current_word)

#             neighbors = get_neighbors(current_word)

#             for neighbor in neighbors:
#                 path_copy = list(current_path)
#                 path_copy.append(neighbor)
#                 q.enqueue(path_copy)

class NewQueue():
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

def get_neighbors():
    

def find_word_ladder(begin_word, end_word):
    visited = set()

    q = NewQueue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None
