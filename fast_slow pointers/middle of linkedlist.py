# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
# If the total number of nodes in the LinkedList is even, return the second middle node.

# Example:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# O(N) space:O(1)
class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None

def middle_of_linkedlist(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.value


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(middle_of_linkedlist(head))

head.next.next.next.next.next = Node(6)
print(middle_of_linkedlist(head))
