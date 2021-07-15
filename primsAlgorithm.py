# Prims Algorithm
import sys


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, sol):

        for idx in range(1, self.v):
            print(f"{sol[idx]}-->{idx}  == {self.graph[idx][sol[idx]]}")

    def minVertex(self, dist, mstSet):

        min_ = sys.maxsize

        for v in range(self.v):
            if dist[v] < min_ and mstSet[v] == False:
                min_ = dist[v]
                min_index = v

        return min_index

    def prims(self, src):

        dist = [sys.maxsize] * self.v
        sol = [None] * self.v
        dist[src] = 0
        mstSet = [False] * self.v
        sol[src] = [-1]

        for _ in range(self.v):

            u = self.minVertex(dist, mstSet)

            mstSet[u] = True

            for v in range(self.v):
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and dist[v] > self.graph[u][v]
                ):
                    dist[v] = self.graph[u][v]
                    sol[v] = u

        self.printSolution(sol)


g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

g.prims(0)
