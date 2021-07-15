"""
 Complexity to find cyclic 
    O(E * V)(edge and vertex)
    Edge for iterating every edge
    Vertex for finding the absolute parent as we need to iterate to every vertex in worst case
"""


class DisjointSet:
    def __init__(self, E=4, V=5):
        self.parent = [-1] * V
        self.edgeList = [(0, 1), (1, 2), (2, 3), (3, 0)]

    def find(self, vertex):
        if self.parent[vertex] == -1:
            return vertex
        return self.find(self.parent[vertex])

    def union(self, fro, to):
        fromP = self.find(fro)
        toP = self.find(to)
        self.parent[fromP] = toP

    def isCyclic(self):
        for edge in self.edgeList:
            if self.find(edge[0]) == self.find(edge[1]):
                return True

            self.union(edge[0], edge[1])

        return False


# set_ = DisjointSet()
# print(set_.isCyclic())

# Optimised Code
# Path Compression and Union by rank
"""
dsuf: disjoint set union find
"""


class Node:
    def __init__(self, parent=-1, rank=0):
        self.parent = parent
        self.rank = rank


class DisjointSetOpt:
    def __init__(self, E=4, V=5):
        self.dsuf = [Node() for _ in range(V)]
        self.edgeList = [(0, 1), (1, 2), (2, 3), (3, 0)]

    def find(self, vertex):
        if self.dsuf[vertex].parent == -1:
            return vertex
        self.dsuf[vertex].parent = self.find(self.dsuf[vertex].parent)
        return self.dsuf[vertex].parent

    def union(self, fro, to):
        if self.dsuf[fro].rank > self.dsuf[to].rank:
            self.dsuf[to].parent = fro
        elif self.dsuf[fro].rank < self.dsuf[to].rank:
            self.dsuf[fro].parent = to
        else:
            self.dsuf[fro].parent = to
            self.dsuf[to].rank += 1

    def isCyclic(self):
        for edge in self.edgeList:
            fromP = self.find(edge[0])
            toP = self.find(edge[1])
            if fromP == toP:
                return True

            self.union(fromP, toP)

        return False


set_ = DisjointSetOpt()
print(set_.isCyclic())
