class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedBrackets = {')':'(',
        ']':'[',
        '}':'{'}
        for item in s:
            if item in closedBrackets:
                top = stack.pop() if stack else '#'

                if top != closedBrackets[item]:
                    return False
            else:
                stack.append(item)
        return not stack



        