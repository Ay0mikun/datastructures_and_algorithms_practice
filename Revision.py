class bfsNode():
    
	def __init__(self, name):
		self.name = name;
		self.adjacenciesList = [];
		self.visited = False;

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, num):
        if self.root is None:
            self.root = Node(num)
        else:
            self.insertNewNode(num, self.root)

    def insertNewNode(self, num, current):
        if num<=current.data:
            if current.left is None:
                current.left = Node(num)
            else:
                self.insertNewNode(num, current.left)
        elif num>current.data:
            if current.right is None:
                current.right = Node(num)            
            else:
                self.insertNewNode(num,current.right)

    def inOrderTraversal(self):
        if self.root is not None:
            self.inOrder(self.root)

    def inOrder(self, current):
        if current.left is not None:
            self.inOrder(current.left)
        print("Element is {}".format(current.data))
        if current.right is not None:
            self.inOrder(current.right)




elements = [1, 5, 9, 11, 13, 14, 22]

someTree = BinaryTree(1)
for i in range(1,len(elements)):
    someTree.insertNode(elements[i])

#someTree.inOrderTraversal()


#print("Left value is {}".format(someTree.root.left))
#print("Right value is {}".format(someTree.root.right.data))


def bfs(node):
    key = 0
    map = {}
    queue = []
    node.visited=True
    queue.append(node)

    map[key]=[]
    map[key].append(node)

    while queue:
        
        map[key] = []
        current = queue.pop(0)
        #print("%s " % current.name)

        for child in current.adjacenciesList:
            if child.visited is False:
                child.visited = True
                map[key].append(child)
                queue.append(child) 
        key += 1

    return map            



def reverseStringOne(string):
    """
    create a new string
    for each letter in the string, pre-concatenate it to the new string
    """
    result=""

    for i in range(len(string)):
        result = string[i]+result

    return result    


def reverseStringTwo(string):
    """
    Set two pointers, begin and end, pointing to the ends of the string
    While begin is less than end, swap characters at both positions and move each pointer till begin>=end
    """
    begin = 0
    end = len(string)-1
    listChar = list(string)

    while begin<end:
        swapItems(listChar, begin, end)
        begin+=1
        end-=1
    string = ''.join(listChar)

    return string    

def swapItems(elements,left, right):
    temp = elements[left]
    elements[left] = elements[right]
    elements[right] = temp


class Stack:

	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeStack(self):
		return len(self.stack)    




def sortStack(given):
    result = Stack()
    result.push(given.pop())
    while not given.isEmpty():
        if given.peek()>result.peek():
            tempGiven = given.pop()
            tempDest = result.pop()

            result.push(tempGiven)
            result.push(tempDest)
        else:
            result.push(given.pop())    

    return result


def ctciSortStack(given):
    result = Stack()

    while not given.isEmpty():
        temp = given.pop()

        while not result.isEmpty and result.peek()>temp:
            given.push(result.pop())
        result.push(temp)

    while not result.isEmpty():
        given.push(result.pop())
    
    return given


stack=Stack()
stack.push(9)
stack.push(6)
stack.push(2)
stack.push(4)
stack.push(3)

sorted = sortStack(stack)

while not sorted.isEmpty():
    print("Sort stack {}".format(sorted.pop()))

var1 = True
var2 = True
var3 = True
var4 =False
test = var1 and var2 and var3 and var4

print("Reverse one {}".format(reverseStringOne("BADMAN")))
print("Reverse two {}".format(reverseStringTwo("BADMAN")))
print("ASCII value: {}".format(chr(104)))
print("Test is %s" % test)
"""
node1 = bfsNode(21)
node2 = bfsNode(10)
node3 = bfsNode(30)
node4 = bfsNode(7)
node5 = bfsNode(12)
node6 = bfsNode(27)
node7 = bfsNode(34)

node1.adjacenciesList.append(node2)
node1.adjacenciesList.append(node3)
node2.adjacenciesList.append(node4)
node2.adjacenciesList.append(node5)
node3.adjacenciesList.append(node6)
node3.adjacenciesList.append(node7)


given_map = bfs(node1)

for key in given_map.keys():
    print (key)


for value in given_map:
    print("==========")
    for i in given_map[value]:
        print("Value {}".format(i.name))
"""
