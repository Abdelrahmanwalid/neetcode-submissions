class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {
            '{': '}',
            '(':')',
            '[':']'
        }
        stack = []
        for char in s:
            if char in parMap:
                stack.append(parMap[char])
            elif char not in parMap and len(stack) == 0:
                return False
            elif stack[-1] != char:
                return False
            elif stack[-1] == char:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False