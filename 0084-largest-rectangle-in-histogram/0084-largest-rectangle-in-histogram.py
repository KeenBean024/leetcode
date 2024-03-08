class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            if stack and stack[-1][1] > height:
                while stack and stack[-1][1] > height:
                    i, h = stack.pop()
                    max_area = max(max_area, (index - i)*h)
                stack.append((i, height))
                
            else:
                stack.append((index, height))

        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (index +1 - i)*h)
            
        return max_area
    
    
    # Time Commplexity O(n)
     # Space Complexity O(n)