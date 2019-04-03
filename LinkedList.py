import pdb 

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def insertNewNode(self, data):
        if (self.head is None):
            self.head = Node(data)
            return self.head  #Important: Without this, the head would be inserted twice.
                              #Something is needed to break the program's flow, in this case, "return"

        current = self.head    

        while(current.next is not None):
            current=current.next

        current.next = Node(data)
        return self.head   


    def deleteNode(self, data): 
        if(self.head.data ==data):
            self.head = self.head.next
            return self.head

        current = self.head    
        while(current.next.data!=data):
            current =current.next

        current.next = current.next.next
        return self.head    





def main():
    given_list = SinglyLinkedList()

    given_list.insertNewNode(9)
    given_list.insertNewNode(11)
    given_list.insertNewNode(13)
    given_list.insertNewNode(21)
    given_list.insertNewNode(64)
    given_list.insertNewNode(15)
    given_list.insertNewNode(67)
    given_list.insertNewNode(89)
    

    current =given_list.head

    while(current is not None):
        print("The list contains: {}".format(current.data))
        current=current.next

    print("Delete operation")    
    given_list.deleteNode(89)

    while(given_list.head is not None):
        print("The list contains: {}".format(given_list.head.data))
        given_list.head=given_list.head.next    


if __name__=="__main__":
    main()    