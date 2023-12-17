class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramMap = defaultdict(list)
        
        for s in strs:
            ordList = [0]*26
            for c in s:
               ordList[ord(c) - ord('a')] += 1
            anagramMap[tuple(ordList)].append(s)
        
        return anagramMap.values()

    # Time Complexity O(n*m)  n-number of strs and m is average length of words
    