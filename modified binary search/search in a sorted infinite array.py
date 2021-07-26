# Given an infinite sorted array (or an array with unknown size), 
# find if a given number ‘key’ is present in the array. 
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

# Since it is not possible to define an array with infinite (unknown) size, 
# you will be provided with an interface ArrayReader to read elements of the array. 
# ArrayReader.get(index) will return the number at index; 
# if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.
# Example 1:

# Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
# Output: 6
# Explanation: The key is present at index '6' in the array.


# O(logN) space: O(1)
import math

class ArrayReader:
    def __init__(self, arr) -> None:
        self.arr = arr
    
    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
        new_start = end + 1
        end += (end - start + 1) * 2
        start = new_start

    return binary_search(reader, start, end, key)

def binary_search(reader, start, end, key):
    while start <= end:
        mid = start + (end - start) // 2
        if reader.get(mid) == key:
            return mid
        elif reader.get(mid) < key:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(search_in_infinite_array(reader, 16))
print(search_in_infinite_array(reader, 11))
reader = ArrayReader([1, 3, 8, 10, 15])
print(search_in_infinite_array(reader, 15))
print(search_in_infinite_array(reader, 200))
