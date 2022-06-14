class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0
        mem = set()
        max_len = 0
        while r<len(s):
            if s[r] not in mem:
                mem.add(s[r])
                r+=1
            elif s[r] in mem:
                max_len = max(max_len, r-l)
                while s[l]!=s[r]:
                    mem.remove(s[l])
                    l+=1
                l+=1
                r+=1
        return max(max_len, r-l)