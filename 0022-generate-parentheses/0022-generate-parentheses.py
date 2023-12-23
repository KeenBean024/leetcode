class Solution(object):
    

    def backtrack(self, openN, closeN, result, currentStack = []):
        if openN== closeN == 0:
            result.append("".join(currentStack))
        
        if openN>0:
            currentStack.append("(")
            self.backtrack(openN-1, closeN, result, currentStack)
            currentStack.pop()
        
        if closeN>0 and closeN>openN:
            currentStack.append(")")
            self.backtrack(openN, closeN-1, result, currentStack)
            currentStack.pop()
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtrack(n, n, result)
        return result