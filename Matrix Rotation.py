class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)

        for _ in range(4):
            if mat == target:
                return True

           
            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

           
            for row in mat:
                row.reverse()

        return False
