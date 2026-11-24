class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {')':'(','}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in ('(', '{', '['):
                stack.append(ch)
            else:
                if ch in valid_dict and len(stack) > 0:
                    if valid_dict[ch] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                

        if len(stack) == 0:
            return True
        return False