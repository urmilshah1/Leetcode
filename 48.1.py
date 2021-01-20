class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        #Transpose
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Reverse
        N = len(matrix)
        for i in range(N//2):
            for j in range(N):
                matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
        return matrix
