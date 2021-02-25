class DisjointSet:
    def __init__(self, arr):
        self.arr = arr
        self.representative = {x: x for x in self.arr}
        self.rank = {x: 1 for x in self.arr}

    def find(self, u):

        if u == self.representative[u]:
            return u
        else:
            self.representative[u] = self.find(self.representative[u])
            return self.representative[u]

    def combine(self, u, v):

        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        else:
            if (self.rank[u] > self.rank[v]):
                self.representative[v] = u
                self.rank[u] += self.rank[v]
            else:
                self.representative[u] = v
                self.rank[v] += self.rank[u]


disjoint = DisjointSet(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
disjoint.combine('a', 'b')
disjoint.combine('c', 'd')
disjoint.combine('e', 'f')
disjoint.combine('g', 'h')
disjoint.combine('a', 'c')
disjoint.combine('e', 'c')
disjoint.combine('g', 'f')
# disjoint.combine(0,1)
