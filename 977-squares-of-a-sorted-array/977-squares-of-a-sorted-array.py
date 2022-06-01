class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = [i**2 for i in nums]
        l = 0
        r = len(squares) - 1
        while l<=r:
            if squares[l] <= squares[r]:
                r-=1
            else:
                squares.insert(r, squares.pop(l))
        return squares