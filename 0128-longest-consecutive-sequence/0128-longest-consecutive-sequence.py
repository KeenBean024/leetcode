class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in nums:
                length = 0
                while num + length in nums:
                    length +=1
                        
                longest = max(longest, length)
                
        return longest
    
    # Time Complexity O(n)
    # SPace Complexity O(n)