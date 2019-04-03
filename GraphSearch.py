class Node():
    
	def __init__(self, name):
		self.name = name;
		self.adjacenciesList = [];
		self.visited = False;

def depth_first(node):
    """
    Go as deep as possible on current node's first child before 
    backtracking and going to the next child
    Do above for all children
    """
    node.visited = True

    print("Visiting "+node.name)

    for n in node.adjacenciesList:
        if n.visited==False:
            depth_first(n)

"""
Queue keeps track of nodes in a certain order so we can 
visit each node's children in the order that the parents were stored
"""

def breadth_first(first_node):
    queue = []
    first_node.visited = True

    queue.append(first_node)

    while queue:
        current_node = queue.pop(0)
        print("%s " % current_node.name)

        for n in current_node.adjacenciesList:
            if n.visited ==False:
                n.visited= True
                queue.append(n)




node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");		
	
node1.adjacenciesList.append(node2);
node1.adjacenciesList.append(node3);
node2.adjacenciesList.append(node4);
node4.adjacenciesList.append(node5);	


depth_first(node1)


breadth_first(node1)