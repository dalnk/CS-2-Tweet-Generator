class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_List(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return not self.head

    def append(self, data):
        temp_node = new Node(data)
        if not self.head:
            self.head = temp_node
            self.tail = temp_node
        else
            self.tail.next = temp_node
            self.tail = temp_node

    def prepend(self, data):
        #todo
        temp_node = new Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def find()
