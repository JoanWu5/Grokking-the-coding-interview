# Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

# Example:
# Input: Matrix=[
#     [2, 6, 8], 
#     [3, 7, 10],
#     [5, 8, 11]
#   ], 
#   K=5
# Output: 7
# Explanation: The 5th smallest number in the matrix is 7.

# O(K * logN + min(N, K))
# space: O(N)
from heapq import *


def kth_smallest_number_in_sorted_matrix(matrix, k):
    n = len(matrix)
    minheap = []

    for i in range(min(len(matrix), k)):
        heappush(minheap, (matrix[i][0], 0, i))
    
    number = -1
    while minheap and k > 0:
        number, i, row = heappop(minheap)
        k -= 1
        if i + 1 < n:
            heappush(minheap, (matrix[row][i + 1], i + 1, row))

    return number

print(kth_smallest_number_in_sorted_matrix([
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 5))


# alternative approach: binary search

# O(N * log(max - min)) where ‘max’ is the largest and ‘min’ is the smallest element in the matrix
# space: O(1)
def kth_smallest_number_in_sorted_matrix_2(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) // 2
        smaller, larger = matrix[0][0], matrix[n - 1][n - 1]
        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        elif count < k:
            start = larger
        else:
            end = smaller
    
    return start

def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1
    
    return count, smaller, larger

print(kth_smallest_number_in_sorted_matrix_2([
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 5))