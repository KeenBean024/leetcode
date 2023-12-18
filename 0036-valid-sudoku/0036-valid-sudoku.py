class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = defaultdict(set)
        rows = defaultdict(set)
        matrix = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value ==".":
                    continue
                    
                if (value in columns[col]) or (value in rows[row]) or (value in matrix[(row//3, col//3)]):
                    return False
                
                columns[col].add(value)
                rows[row].add(value)
                matrix[(row//3, col//3)].add(value)
        return True