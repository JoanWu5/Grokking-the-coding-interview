# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.

# Example:
# k = 3, 1->2->3->4->5->6->null 
# output: 4->5->6->1->2->3->null

# k = 8, 1->2->3->4->5->null 
# output: 3->4->5->1->2->null

# O(N) space:O(1)
class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None

    def print_linkedlist(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + "", end = "")
            temp = temp.next
        print()

def rotate_linkedlist(head, k):
    if head is None or head.next is None or k <= 0:
        return head
    
    linkedlist_length = 1
    pointer = head
    sub_list_last_node = None
    while pointer is not None:
        linkedlist_length += 1
        sub_list_last_node = pointer
        pointer = pointer.next
    
    k = k % linkedlist_length
    if k <= 0:
        return head

    first_node = head
    previous = None
    for _ in range(k):
        previous = first_node
        first_node = first_node.next
    
    previous.next = None
    sub_list_last_node.next = head

    return first_node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = rotate_linkedlist(head,8)
head.print_linkedlist()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head = rotate_linkedlist(head,3)
head.print_linkedlist()