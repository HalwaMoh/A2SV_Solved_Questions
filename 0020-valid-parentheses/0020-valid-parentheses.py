class Solution(object):
    def isValid(self, s):
        stack = []
        hashmap = {")":"(", "}":"{", "]":"["}

        for ch in s:
            if ch in hashmap:  
                top = stack.pop() if stack else ""
                if top != hashmap[ch]:
                    return False
            else:              
                stack.append(ch)

        return not stack