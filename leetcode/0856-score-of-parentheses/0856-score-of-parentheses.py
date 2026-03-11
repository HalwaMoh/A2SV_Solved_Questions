class Solution(object):
    def scoreOfParentheses(self, s):
        
        stack = []
        curr = 0

        for ch in s:
            if ch == "(":
                stack.append(curr)
                curr = 0
            else:
                prev = stack.pop()
                curr = prev + max(2 * curr, 1)

        return curr
        