class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 0:
            return s

        stack = list()
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
