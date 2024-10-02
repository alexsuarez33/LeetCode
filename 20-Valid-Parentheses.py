class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        opens = \([{\
        for element in s:
            if element in opens:
                brackets.append(element)
            elif not brackets:
                return False
            elif element == ')':
                if brackets[-1] == '(':
                    brackets.pop()
                else:
                    return False
            elif element == ']':
                if brackets[-1] == '[':
                    brackets.pop()
                else:
                    return False
            else:
                if brackets[-1] == '{':
                    brackets.pop()
                else:
                    return False
        if brackets:
            return False
        else:
            return True