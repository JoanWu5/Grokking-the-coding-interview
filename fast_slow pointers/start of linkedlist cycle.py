# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

# O(N) space:O(1)
class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = None

def start_of_linkedlist_cycle(head):
    cycle_length = linkedlist_cycle(head)
    if cycle_length == 0:
        return None
    
    pointer1, pointer2 = head, head
    for i in range(cycle_length):
        pointer2 = pointer2.next
    
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1.value

def linkedlist_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return caculate_linkedlist_cycle(slow)
    
    return 0

def caculate_linkedlist_cycle(pointer):
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
print(start_of_linkedlist_cycle(head))

head.next.next.next.next.next.next = head.next.next
print(start_of_linkedlist_cycle(head))