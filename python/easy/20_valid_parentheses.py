class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = ('()', '{}', '[]')
        stack = []

        for p in s:
            if not stack:
                stack.append(p)
                continue

            if stack[-1] + p in parentheses:
                stack.pop()
            else:
                stack.append(p)

        return False if stack else True