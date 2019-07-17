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




"""
List of nodes on each level
"""

def makeListBFS(node):
    result = []
    current = []

    current.append(node)

    while current:
        result.append(current)
        list = current
        current = []

        for n in list:
            if n.left:
                current.append(n.left)

            if n.right:
                current.append(n.right)

    return result


def makeArray(num):
    list = [0]*num
    print("Start...")
    while num>0:
        print(list[num-1])
        num = num-1
    print("End...")

makeArray(5)