class LinkedList:

    def __init__(self, ListofNodes = None):
        self.head = None
        if ListofNodes is not None: # not empty
            node = Node( data = ListofNodes.pop(0) )
            self.head = node
            for elem in ListofNodes:
                node.next = Node( data = elem)
                node = node.next


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


llist = LinkedList(["a", "b", "c", "d", "e"])


for  i in llist:
    print(i)




