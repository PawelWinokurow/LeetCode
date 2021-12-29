class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        reverse = {'(': ')', '{': '}', '[': ']'}
        for ch in s:
            if ch in open:
                stack.append(ch)
            else:
                if len(stack) == 0 or ch != reverse[stack.pop(-1)]:
                    return False
        return len(stack) == 0