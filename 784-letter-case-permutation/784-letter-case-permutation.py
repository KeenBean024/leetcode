class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        
        def backtrack(inp, res=''):
            if not inp:
                result.append(res)
                return
            i = inp[0]
            if i.isalpha():
                backtrack(inp[1:], res+i.upper())
                backtrack(inp[1:], res+i.lower())
            else:
                backtrack(inp[1:], res+i)
        
        backtrack(s)
        return result