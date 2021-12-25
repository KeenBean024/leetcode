class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start =-1
        ref_sum = float("-inf")
        max_val = float("-inf")
        for num in nums:
            if num>ref_sum+num:
                ref_sum = num
            else:
                ref_sum += num
            
            if ref_sum>max_val:
                max_val = ref_sum
                
        return max_val

# Kadane's Algorithm
# Time Complexity - O(n)
# Space Complexity - O(1)