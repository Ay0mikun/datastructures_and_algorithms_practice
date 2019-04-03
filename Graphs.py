"""
Adjacency Matrix Implementation
"""
def make_graph():
    graph = []

    for x in range(0,3):
        graph.append([])
        for y in range(0,3):
            graph[x].append(0)


    return graph


print(make_graph())



"""
Adjacency List Implementation
"""