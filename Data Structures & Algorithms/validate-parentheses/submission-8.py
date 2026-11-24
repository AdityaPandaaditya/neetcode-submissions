class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {')':'(', '}':'{',']':'['}

        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)

            elif i in valid_parentheses:
                if stack and stack[-1] == valid_parentheses[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
