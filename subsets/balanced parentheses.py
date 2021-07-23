# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

# Example:
# Input: N=2
# Output: (()), ()()
# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()

# O(N*2^N)  
# While processing each element, we do need to concatenate the current string with ( or ). 
# This operation will take O(N)
#  in the worst case, it is equivalent to a binary tree, where each node will have two children. 
# This means that we will have 2^N leaf nodes
# space : O(N * 2^N)
from collections import deque

class Parentheses:
    def __init__(self, str, open_count, close_count) -> None:
        self.str = str
        self.open_count = open_count
        self.close_count = close_count

def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(Parentheses("", 0, 0))
    while queue:
        ps = queue.popleft()
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                queue.append(Parentheses(ps.str + "(", ps.open_count + 1, ps.close_count))
            
            if ps.open_count > ps.close_count:
                queue.append(Parentheses(ps.str + ")", ps.open_count, ps.close_count + 1))
    
    return result

# recursive
def generate_valid_parentheses_2(num):
    result = []
    parenthese_str = [0 for _ in range(2 * num)]
    generate_valid_parenthese_recursive(num, 0, 0, 0, parenthese_str, result)
    return result

def generate_valid_parenthese_recursive(num, open_count, close_count, index, parenthese_str, result):
    if open_count == num and close_count == num:
        result.append(''.join(parenthese_str))
    else:
        if open_count < num:
            parenthese_str[index] = '('
            generate_valid_parenthese_recursive(num, open_count + 1, close_count, index + 1, parenthese_str, result)
        
        if open_count > close_count:
            parenthese_str[index] = ')'
            generate_valid_parenthese_recursive(num, open_count, close_count + 1, index + 1, parenthese_str, result)
    
    
print(generate_valid_parentheses(3))
print(generate_valid_parentheses_2(3))
