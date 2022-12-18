class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinedList:
    def __init__(self):
        self.head = None

    # Liked list traversal
    def display_LL(self):
        if self.head is None:
            print('Linked List Is Empty')
        else:
            n = self.head
            print('\nLinked List :')
            while n is not None:
                print(n.data, end=' --> ')
                n = n.ref
            print('\n')

    # Adding node in began
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Adding node at the end of the LL
    def adding_At_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Adding node after
    def add_after(self, data,after):
        n = self.head
        while n is not None:
            if n.data == after:
                break
            n = n.ref

        if n is None:
            print('Node is not Present')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


LL1 = LinedList()
LL1.add_begin(10)
LL1.adding_At_end(11)
LL1.add_begin(9)
LL1.adding_At_end(12)
LL1.add_begin(8)
LL1.add_after(1,11)
LL1.display_LL()
