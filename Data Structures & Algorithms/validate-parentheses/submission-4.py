class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {')':'(','}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in valid_dict:
                if len(stack)>0 and stack[-1] == valid_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if len(stack) == 0:
            return True
        return False