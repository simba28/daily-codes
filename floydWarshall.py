# all source shortest path

# no. of vertices
V = 4

# define infiniy
inf = 99999


def floydWarshall(graph):
    """ dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """

    """ initializing the solution matrix same as input graph matrix
    OR we can say that the initial values of shortest distances
    are based on shortest paths considering no intermediate vertices """

    # dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    dist = []
    for row in graph:
        dist.append(row.copy())

    """ Add all vertices one by one to the set of intermediate
     vertices.
     ---> Before start of an iteration, we have shortest distances
     between all pairs of vertices such that the shortest
     distances consider only the vertices in the set 
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a iteration, vertex no. k is 
      added to the set of intermediate vertices and the set becomes {0, 1, 2, .. k}
    """

    for k in range(V):

        # pick all the vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the above picked source
            for j in range(V):

                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    printSolution(dist)

# A utility function to print the solution


def printSolution(dist):
    print("Following matrix shows the shortest distances\
between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == inf):
                print("%7s" % ("INF"), end=' ')
            else:
                print("%7d\t" % (dist[i][j]), end='')
            if j == V-1:
                print()


# Driver program to test the above program
# Let us create the following weighted graph

'''
            10
       (0)------->(3)
        |          ^
      5 |          |
        |          |
     "\"|/         |
       (1)------->(2)
            3           
'''
graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0,   1],
         [inf, inf, inf, 0]
         ]
# Print the solution
floydWarshall(graph)
