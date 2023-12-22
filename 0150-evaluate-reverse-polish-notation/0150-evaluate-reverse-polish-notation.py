class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                
                if token == "+":
                    stack.append(val1+val2)
                
                elif token ==  "-":
                    stack.append(val1-val2)

                elif token ==  "*":
                    stack.append(val1*val2)

                elif token ==  "/":
                    stack.append(int(float(val1)/val2))
                    
        return stack.pop()
        