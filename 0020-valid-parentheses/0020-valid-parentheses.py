class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {"(":")", "[":"]","{":"}"}
        stack = []
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char in match:
                stack.append(char)
                continue
            if len(stack) == 0 or char != match[stack.pop()]:
                return False
        if len(stack) == 0:
            return True
        return False
        