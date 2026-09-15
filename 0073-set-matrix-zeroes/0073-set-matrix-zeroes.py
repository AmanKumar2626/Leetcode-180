class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        clen = len(matrix)
        rlen = len(matrix[0])
        row = [0] * rlen
        col = [0] * clen 
        for i in range(clen):
            for j in range(rlen):
                if(matrix[i][j] == 0):
                    col[i] = 1
                    row[j] = 1
        
        for i in range(clen):
            if(col[i] == 1):
                for j in range(rlen):
                    matrix[i][j] = 0

        for i in range(rlen):
            if(row[i] == 1):
                for j in range(clen):
                    matrix[j][i] = 0 



        