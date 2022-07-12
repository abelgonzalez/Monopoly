# Linked list
class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def add(self, item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node


test_list = LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
for item in test_list:
    print(item)