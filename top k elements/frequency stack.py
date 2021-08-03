# Design a class that simulates a Stack data structure, implementing the following two operations:

# push(int num): Pushes the number ‘num’ on the stack.
# pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

# Example:
# After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
# 1. pop() should return 2, as it is the most frequent number
# 2. Next pop() should return 1
# 3. Next pop() should return 2

from heapq import *


class Element:
    def __init__(self, num, frequency, sequence) -> None:
        self.num = num
        self.frequency = frequency
        self.sequence = sequence
    
    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        return self.sequence > other.sequence


class FrequenceStack:
    maxheap = []
    frequencymap = dict()
    sequence = 0

    def push(self, num):
        self.frequencymap[num] =  self.frequencymap.get(num, 0) + 1
        heappush(self.maxheap, Element(num, self.frequencymap[num], self.sequence))
        self.sequence += 1


    def pop(self):
        element = heappop(self.maxheap)
        if element.frequency > 1:
            self.frequencymap[element.num] -= 1
        else:
            del self.frequencymap[element.num]
        
        return element.num

frequenceStack = FrequenceStack()
frequenceStack.push(1)
frequenceStack.push(2)
frequenceStack.push(3)
frequenceStack.push(2)
frequenceStack.push(1)
frequenceStack.push(2)
frequenceStack.push(5)
print(frequenceStack.pop())
print(frequenceStack.pop())
print(frequenceStack.pop())