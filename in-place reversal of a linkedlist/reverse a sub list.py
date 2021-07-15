# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

# Example:
# p = 2, q = 4, 1->2->3->4->5->null 
# output: 1->4->3->2->5->null

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

def reverse_sub_list(head, p, q):
    if p == q:
        return head

    current, pre_pointer = head, None
    count = 0
    while current is not None:
        if count == p - 1:
            break
        count += 1
        pre_pointer = current
        current = current.next
    
    count = 0
    new_header = None
    last_node_of_sub_list = current

    while current is not None:
        if count == q - p + 1:
            break
        next_pointer = current.next
        current.next = new_header
        new_header = current
        current = next_pointer
        count += 1
    
    if pre_pointer is not None:
        pre_pointer.next = new_header
    else:
        head = new_header

    last_node_of_sub_list.next = current
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = reverse_sub_list(head,2,4)
head.print_linkedlist()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = reverse_sub_list(head,1,5)
head.print_linkedlist()

# follow up:
# Problem 1: Reverse the first ‘k’ elements of a given LinkedList.
# Solution: This problem can be easily converted to our parent problem; 
# to reverse the first ‘k’ nodes of the list, we need to pass p=1 and q=k.

# Problem 2: Given a LinkedList with ‘n’ nodes, reverse it based on its size in the following way:
# If ‘n’ is even, reverse the list in a group of n/2 nodes.
# If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
# Solution: When ‘n’ is even we can perform the following steps:

# Reverse first ‘n/2’ nodes: head = reverse(head, 1, n/2)
# Reverse last ‘n/2’ nodes: head = reverse(head, n/2 + 1, n)
# When ‘n’ is odd, our algorithm will look like:

# head = reverse(head, 1, n/2)
# head = reverse(head, n/2 + 2, n)
# Please note the function call in the second step. We’re skipping two elements as we will be skipping the middle element.