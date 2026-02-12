class Solution(object):
    def transpose(self, matrix):
        
        m,n=len(matrix),len(matrix[0])
        newMatrix=[]
        
        for i in range(0,n):
            inner=[0]*m
            newMatrix.append(inner)
        
        for i in range(0,n):
            for j in range(0,m):
                newMatrix[i][j]=matrix[j][i]
        return newMatrix
        
