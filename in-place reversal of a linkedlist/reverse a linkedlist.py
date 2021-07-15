# reverse a linkedlist
# O(N) space:O(1)

class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None

    def print_linkedlist(head):
        while head is not None:
            print(str(head.value) + "", end = "")
            head = head.next
        print()

def reverse_linkedlist(head):
    if head is None or head.next is None:
        return head
    
    new_header = None
    while head is not None:
        pointer = head.next
        head.next = new_header
        new_header = head
        head = pointer

    return new_header  

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)
new_header = reverse_linkedlist(head)
new_header.print_linkedlist()



