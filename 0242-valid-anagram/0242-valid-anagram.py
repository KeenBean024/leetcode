class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count_map = [0]*26
        for char in s:
            count_map[ord(char)-ord('a')] += 1
        
        for char in t:
            if count_map[ord(char)-ord('a')] == 0:
                return False
            count_map[ord(char)-ord('a')] -= 1
        
        return True

    # Time Complexity O(n)
    # Space Complexity O(26) = O(1)