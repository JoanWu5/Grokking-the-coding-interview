# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

# Example:
# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
# Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

# O(N * logK) where ‘N’ is the total number of elements in all the ‘K’ input arrays.
# space: O(K)
from heapq import *

class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __lt__(self, other):
        return self.value < other.value

def merge_k_sorted_lists(lists):
    minheap = []
    for root in lists:
        if root:
            heappush(minheap, root)
    
    head, tail = None, None
    while minheap:
        node = heappop(minheap)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next:
            heappush(minheap, node.next)
    
    return head

l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)


result = merge_k_sorted_lists([l1, l2, l3])
while result:
    print(str(result.value) + ",", end = '')
    result = result.next
print()
