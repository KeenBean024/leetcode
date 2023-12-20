class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start <= end:
            # print(s[start], s[end])
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[end].lower() == s[start].lower():
                end -= 1
                start += 1
                continue
            return False
        
        return True
    
    # Time Complexity O(n)