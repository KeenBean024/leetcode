class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memory = {}
        for num in nums:
            if memory.get(num):
                return True
            else:
                memory[num]='exists'
                
        return False