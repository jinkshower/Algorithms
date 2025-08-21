class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')' : '(', '}' : '{', ']' : '['}
        for i in range(len(s)):
            if s[i] in map: # if is closing bracket
                if stack and stack[-1] == map[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return len(stack) == 0