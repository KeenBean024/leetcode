class Solution(object):
    # def hammingWeight(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     count = 0
    #     while n!=0:
    #         count+=n%2
    #         n = n>>1
    #     return count
    
# T O(32)/O(1) S O(1)

#ALTERNATE

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n!=0:
            n = n&(n-1)
            count+=1
        return count
    
#Same time complexity but slightly faster than normal as it doesnt iteratively search for each 1