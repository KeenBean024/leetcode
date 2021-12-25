class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        #Solution will need a prefix and postfix multiplication to get the result
        # first append result with prefix
        result.append(1)
        value = 1
        for i in range(len(nums)-1):
            value = value*nums[i]
            result.append(value)
        # multiply result with postfix
        value =1
        for i in range(-2,-1*len(result)-1,-1):
            value = value*nums[i+1]
            result[i] = result[i]*value
            
        return result
        
# Time Complexity O(n)
# Space Complexity O(1)

            