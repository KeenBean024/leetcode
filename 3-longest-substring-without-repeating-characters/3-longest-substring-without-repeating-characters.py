class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        mem = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in mem:
                mem.remove(s[l])
                l+=1
            mem.add(s[r])
            max_len = max(max_len, r-l+1)
        return  max_len