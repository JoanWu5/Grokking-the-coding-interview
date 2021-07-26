# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
# To flip an image horizontally means that each row of the image is reversed. 
# For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
# For example, inverting [1, 1, 0] results in [0, 0, 1].

# Example 1:

# Input: [
#   [1,0,1],
#   [1,1,1],
#   [0,1,1]
# ]
# Output: [
#   [0,1,0],
#   [0,0,0],
#   [0,0,1]
# ]
# Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

def flip_invert_image(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1] ^ 1, matrix[i][j] ^ 1
    
    return matrix

print(flip_invert_image([
  [1,0,1],
  [1,1,1],
  [0,1,1]
]))

print(flip_invert_image([
  [1,1,0,0],
  [1,0,0,1],
  [0,1,1,1], 
  [1,0,1,0]
]))