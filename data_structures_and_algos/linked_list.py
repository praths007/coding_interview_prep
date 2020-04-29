class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# TODO: create add, delete, print nodes to LL functionality
# count_nodes etc...
class LinkedList():
    def __init__(self):
         self.head = None


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    while(llist.head):
        print(llist.head.data)
        llist.head = llist.head.next



