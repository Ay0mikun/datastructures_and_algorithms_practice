class Node():
    
    def __init__(self, data=None):
        self.data = data
        self.left =None
        self.right = None    


class BinaryTree():

    def __init__(self, data=None):
        self.root = data

    """    
    Writing the insert like this will cause an exception
    when the root value is not null and a node argument is not inserted
    when calling the function
    def insertNode(self, data, node=None):
        
        if self.root is None:
            self.root = Node(data)
        
        else:
            if data<=node.data:
                if node.left is None:
                    node.left = Node(data)
                else:   
                    self.insertNode(data, node.left)
                
            if data>node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.insertNode(data, node.right)    
    """
    def insertNode(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNewNode(data, self.root)

    def insertNewNode(self, data, node):
        if data<=node.data:
            if(node.left is None):
                node.left = Node(data)
            else:
                self.insertNewNode(data, node.left)    
         
        elif data>node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insertNewNode(data, node.right)  


    def deleteNode(self, node, data):
        if node is None:
            return node

        elif data<node.data:
            node.left = self.deleteNode(node.left, data)    
        elif data>node.data:
            node.right = self.deleteNode(node.right, data)    
        else:
            if node.left is None and node.right is None:    
                node = None
                return node
            elif node.left is not None and node.right is not None:
                tempSmallestValue = self.getMinNodeData(node.right)
                node.data= tempSmallestValue
                node.right = self.deleteNode(node.right, tempSmallestValue)
            else:
                if node.left is not None and node.right is None:
                    node = node.left
                    return node
                elif node.right is not None and node.left is None:
                    node =node.right
                    return node   
        return node            
            

    # DeleteNode requires getMin for right subtree or getMax for left subtree
    def getMinNodeData(self, node):
        if node.left is not None:
            return self.getMinNodeData(node.left)
        return node.data    

    def getMaxNodeData(self, node):
        if node.right is not None:
            return self.getMaxNodeData(node.right)
        return node.data    


    def findNode(self, data):
        if self.root.data == data:
            return True
        else:
            return self.findGivenNode(data, self.root)    

    def findGivenNode(self, data, node):
        if data<node.data:
            if node.left.data == data:
                return True
            else:
                self.findGivenNode(data, node.left)
        if data>node.data:
            if node.right.data==data:
                return True             
            else:
                self.findGivenNode(data, node.right)

        return False        

   
    def inOrder(self):
        if self.root is not None:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.left is not None:
            self.traverseInOrder(node.left)
        
        print(node.data, end=" ")
        
        if node.right is not None:
            self.traverseInOrder(node.right)


    def preOrder(self):
        if self.root is not None:
            self.traversePreOrder(self.root)

    def traversePreOrder(self, node):
        print(node.data, end=" ")
        
        if node.left is not None:
            self.traversePreOrder(node.left)

        if node.right is not None:
            self.traversePreOrder(node.right)    

 
    def postOrder(self):
        if self.root is not None:
            self.traversePostOrder(self.root)         

    def traversePostOrder(self, node):
        if node.left is not None:
            self.traversePostOrder(node.left)
        if node.right is not None:
            self.traversePostOrder(node.right)
        print(node.data, end=" ")    

def main():
    given_node = BinaryTree()
    given_node.insertNode(12)
    given_node.insertNode(9)
    given_node.insertNode(23)
    given_node.insertNode(7)
    given_node.insertNode(11)
    given_node.insertNode(16)
    given_node.insertNode(28)

    print("The root node is {} {}".format(given_node.root.data, "\n"))

    print("Computing In Order Traversal")
    given_node.inOrder()

    print("\n")

    print("Computing Pre Order Traversal")
    given_node.preOrder()

    print("\n")

    print("Computing Post Order Traversal")
    given_node.postOrder()

    print("\n")

    if given_node.findNode(9):
        print("EUREKA!")
    else:
        print("Not in my backyard!")
        
    print("\n")

    print("Deleting node...".format(given_node.deleteNode(given_node.root,12)))        
    
    print("\n")
    
    print("Computing In Order Traversal")
    given_node.inOrder()

    
        

if __name__ == "__main__":
    main()   

