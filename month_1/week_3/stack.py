# class Stack:
#     def __init__(self):
#         self.stack = []
        
#     def __str__(self):
#         return f"Stack: {self.stack}"
    
#     def push(self, val):
#         self.stack.append(val)
        
#     def pop(self):
#         if not self.isEmpty():
#             return self.stack.pop()
#         return "Stack Underflow"
        
#     def isEmpty(self):
#         return len(self.stack) == 0
    
#     def peek(self):
#         if not self.isEmpty():
#             return self.stack[-1]
#         return None
        

# s = Stack()

# def isValid(s):
#     bracket_map = {")": "(", "}": "{", "]": "["}
#     stack = []

#     for char in s:
#         if char in bracket_map:
#             top_element = stack.pop() if stack else '#'
#             print(top_element)
#             if bracket_map[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#             print('apped', stack)
            
#     return not stack

# # Example usage:
# # print(isValid("()[]{}"))


# map = {")": "(", "}": "{", "]": "["}

# if map[")"] == "(":
#     print(' tHis si matched')

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # If min_stack is empty OR val is smaller than current min, push val
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Otherwise, repeat the current minimum
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
