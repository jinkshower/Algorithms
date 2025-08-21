class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def toInt(s):
            try:
                return int(s)
            except ValueError:
                return -201
        
        def calculate(sign, a, b):
            if sign == "+":
                return a + b
            elif sign == "-":
                return a - b
            elif sign == "*":
                return a * b
            else:
                return int(a / b)

        for token in tokens:
            val = toInt(token)
            if val != -201:
                stack.append(val)
            else:
                b = stack.pop()
                a = stack.pop()
                val = calculate(token, a, b)
                stack.append(val)
                print(val)
        
        return int(stack[-1])
