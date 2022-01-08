class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        if l==r:
            return nums[l]
        while l<r:
            if r==l+1:
                return min(nums[l], nums[r])
            elif nums[l] < nums[r]:
                return nums[l]
            elif nums[r] < nums[l]:
                mid = (r+l)//2
                if nums[mid]>nums[l]:
                    l=mid
                else:
                    r=mid
                    
#SPACE COMPLEXITY - O(1)
#Time Complexity - O(log(n))