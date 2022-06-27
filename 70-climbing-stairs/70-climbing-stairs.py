class Solution(object):
#     #Memoization
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         mem = {}
#         def traverse(n):
#             if n==0:
#                 return 1
#             if n<0:
#                 return 0
#             if n in mem:
#                 return mem[n]
#             else:
#                 mem[n] = traverse(n-1) + traverse(n-2)
#             return mem[n]
        
#         return traverse(n)
    
    #Dynamic Programming
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1,1
        for _ in range(n-1):
            tmp = one
            one = one+two
            two=tmp
        return one
#Without Memoization - T O(2^N) S O(2^N)
#With Memoization - T O(N) S O(N)
#With DP T O(N) S O(1)