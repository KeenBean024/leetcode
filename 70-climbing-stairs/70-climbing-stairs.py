class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {}
        def traverse(n):
            if n==0:
                return 1
            if n<0:
                return 0
            if n in mem:
                return mem[n]
            else:
                mem[n] = traverse(n-1) + traverse(n-2)
            return mem[n]
        
        return traverse(n)