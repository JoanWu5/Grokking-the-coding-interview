# Important properties of XOR to remember #
# Following are some important properties of XOR to remember:

# Taking XOR of a number with itself returns 0, e.g.,

# 1 ^ 1 = 0
# 29 ^ 29 = 0
# Taking XOR of a number with 0 returns the same number, e.g.,

# 1 ^ 0 = 1
# 31 ^ 0 = 31
# XOR is Associative & Commutative, which means:

# (a ^ b) ^ c = a ^ (b ^ c)
# a ^ b = b ^ a

# Given an array of n-1 integers in the range from 1 to n, find the one number that is missing from the array.

# Example:
# Input: 1, 5, 2, 6, 4
# Answer: 3

# O(N) space: O(1)
def find_missing_number(arr):
    n = len(arr) + 1
    arr_sum = 0
    for i in range(1, n + 1):
        arr_sum += i
    
    for i in arr:
        arr_sum -= i
    
    return arr_sum

print(find_missing_number([1, 5, 2, 6, 4]))

# problem: While finding the sum of numbers from 1 to n, we can get integer overflow when nn is large.
def find_missing_number_2(arr):
    n = len(arr) + 1
    arr_xor1 = 1
    for i in range(2, n + 1):
        arr_xor1 = arr_xor1 ^ i
    
    arr_xor2 = arr[0]
    for i in range(1, n - 1):
        arr_xor2 = arr_xor2 ^ arr[i]
    
    return arr_xor2 ^ arr_xor1
print(find_missing_number_2([1, 5, 2, 6, 4]))
