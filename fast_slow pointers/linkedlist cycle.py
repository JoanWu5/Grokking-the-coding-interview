# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

# O(N) space:O(1)
class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None
    

def linkedlist_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# follow up:Given the head of a LinkedList with a cycle, find the length of the cycle.
# O(N) space:O(1)
def linkedlist_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return caculate_cycle_length(slow)

    return 0

def caculate_cycle_length(pointer):
    current = pointer
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == pointer:
            break
    return cycle_length

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print(linkedlist_cycle(head))
print(linkedlist_cycle_length(head))

head.next.next.next.next.next.next = head.next.next
print(linkedlist_cycle(head))
print(linkedlist_cycle_length(head))




    