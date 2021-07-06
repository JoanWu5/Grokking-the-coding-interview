# Given the head of a Singly LinkedList, 
# write a method to modify the LinkedList such that 
# the nodes from the second half of the LinkedList are inserted alternately to 
# the nodes from the first half in reverse order. 
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, 
# your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

# Example:
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

# O(N) space:O(1)

class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None

    def print_linkedlist(self):
        head = self
        while head is not None:
            print(str(head.value) + " ", end = '')
            head = head.next
        print()

def rearrange_linkedlist(head):
    if head is None or head.next is None:
        return head
    
    middle = find_middle_of_linkedlist(head)
    reversed_seconf_half = reverse_linkedlist(middle)
    pointer1, pointer2 = head, reversed_seconf_half
    while pointer1 is not None and pointer2 is not None:
        pointer1_next = pointer1.next
        poineter2_next = pointer2.next
        pointer1.next = pointer2
        pointer2.next =  pointer1_next
        pointer2 = poineter2_next
        pointer1 = pointer1_next
    
    if pointer1 is not None:
        pointer1.next = None
    return head

def find_middle_of_linkedlist(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_linkedlist(head):
    new_header = None
    while head is not None:
        pointer = head.next
        head.next = new_header
        new_header = head
        head = pointer
    return new_header


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
rearrange_linkedlist(head)
head.print_linkedlist()

head.next.next.next.next.next = Node(12)
rearrange_linkedlist(head)
head.print_linkedlist()

