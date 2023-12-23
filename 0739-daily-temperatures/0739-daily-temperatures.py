class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] # stores pair [val, index]
        result = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            if len(stack)==0:
                stack.append((temp, i))
                continue
                
            while len(stack)>0 and temp > stack[-1][0]:
                val = stack.pop()
                result[val[1]] = i - val[1]
            
            stack.append((temp, i))
        return result