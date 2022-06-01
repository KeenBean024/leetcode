class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        while r >= l:
            if nums[r]==0:
                r-=1
            else:
                break
        
        while l<=r:
            # print(l)
            if nums[l]==0:
                nums.insert(r,nums.pop(l))
                r -= 1
            else:
                l += 1
                
        