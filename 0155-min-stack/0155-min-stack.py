class MinStack(object):
    
    def __init__(self):
        self._stack = []  
        self._min_val = float("inf")
        self.prev_min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val <= self._min_val:
            self.prev_min.append(self._min_val)
            self._min_val = val
        
        self._stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        value = self._stack.pop()
        if value == self._min_val:
            self._min_val = self.prev_min.pop()
        return value
    
    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()