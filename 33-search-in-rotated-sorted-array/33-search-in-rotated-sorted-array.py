class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        if l==r:
            if target==nums[l]:
                return l
            
        while l<r:
            mid = (l+r)//2
            if target==nums[mid]:
                return mid
            if target==nums[l]:
                return l
            if target==nums[r]:
                return r
            if target>nums[l]:
                if nums[mid]>nums[l]:
                    if nums[l]<target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                else:
                    r=mid
            elif target<nums[r]:
                if nums[mid]<nums[r]:
                    if nums[mid]<target<nums[r]:
                        l=mid+1
                    else:
                        r=mid-1
                else:
                    l=mid+1
            else:
                break
        return -1
                
                