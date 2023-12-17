class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = dict()
        for index in range(len(nums)):
            num=nums[index]
            delta = target-num
            if delta in hashMap:
                return [index,hashMap[delta]]
            else:
                hashMap[num]=index

# Time Complexity - O(n)
# Space Complexity - O(n)
