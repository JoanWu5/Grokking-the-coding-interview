# Any number will be called a happy number if, 
# after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
# leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Example:
# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:

# O(logN) ??? don't understand
# space:O(1)
def happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_next_number(slow)
        fast = find_next_number(find_next_number(fast))
        if slow == fast:
            break
    
    return slow == 1

def find_next_number(num):
    next_number = 0
    while num > 0:
        digit = num % 10
        next_number += digit * digit
        num = num // 10
    return next_number

print(happy_number(23))
print(happy_number(12))