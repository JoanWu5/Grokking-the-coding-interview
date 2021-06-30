# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, 
# i.e., you will stop when you have to pick from a third fruit type.

# Example:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# sliding window: O(N) space: O(1)
def fruits_into_two_baskets(fruits):
    result = 0
    fruit_hashmap = dict()
    window_start = 0
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_hashmap:
            fruit_hashmap[right_fruit] = 0
        fruit_hashmap[right_fruit] += 1
        while(len(fruit_hashmap)) > 2:
            left_fruit = fruits[window_start]
            fruit_hashmap[left_fruit] -= 1
            if fruit_hashmap[left_fruit] == 0:
                del fruit_hashmap[left_fruit]
            window_start += 1
        result = max(result, window_end - window_start +1)
    return result

print(fruits_into_two_baskets(['A', 'B', 'C', 'A', 'C']))
print(fruits_into_two_baskets(['A', 'B', 'C', 'B', 'B', 'C']))