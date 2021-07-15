# Given the head of a LinkedList and a number ‘k’, 
# reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
# Example:
# k = 3, 1->2->3->4->5->6->7->null 
# output: 3->2->1->6->5->4->7->null

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

def reverse_every_k_element_sub_list(head, k):
    if head is None or head.next is None or k <= 1:
        return head
    
    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current
        next_pointer = None
        i = 0
        while current is not None and i < k:
            next_pointer = current.next
            current.next = previous
            previous = current
            current = next_pointer
            i += 1
        
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous
        
        last_node_of_sub_list.next = current
        if current is None:
            break

        previous = last_node_of_sub_list
    
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head = reverse_every_k_element_sub_list(head,3)
head.print_linkedlist()

