class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i-1][j] + aux[i][j-1]
        return aux[-1][-1]
