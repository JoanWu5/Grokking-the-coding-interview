# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and 
# the input LinkedList should be in the original form once the algorithm is finished. 
# The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Example:
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true

class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None
    
def palindorme_linkedlist(head):
    if head is None or head.next is None:
        return True
    
    middle = find_middle_of_linkedlist(head)
    reversed_second_half = reverse_linkedlist(middle)
    pointer1, pointer2 = head, reversed_second_half
    while pointer1 is not None and pointer2 is not None:
        if pointer1.value != pointer2.value:
            break
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    reverse_linkedlist(reversed_second_half)

    if pointer1 is None or pointer2 is None:
        return True
    return False
    
def reverse_linkedlist(head):
    new_header = None
    while head is not None:
        pointer = head.next
        head.next = new_header
        new_header = head
        head = pointer
    return new_header

def find_middle_of_linkedlist(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
print(palindorme_linkedlist(head))

head.next.next.next.next.next = Node(1)
print(palindorme_linkedlist(head))

head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(2)
head2.next.next.next = Node(1)
print(palindorme_linkedlist(head2))