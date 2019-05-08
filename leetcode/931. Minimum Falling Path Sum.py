class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        
        infinity = float("inf")
        opt = [[0] * n for _ in range(n)]
        
        for index in range(0,n):
            opt[0][index] = A[0][index]
        
        for i in range(1, n):
            for j in range(0, n):    
                if(i > 0 and j > 0):
                    topLeft = opt[i-1][j-1]
                else :
                    topLeft = infinity
                if(i > 0):
                    top = opt[i-1][j]
                    
                else:
                    top = infinity
                if(i > 0 and j < n-1):
                    topRight = opt[i-1][j+1]
                else:
                    topRight = infinity
                    
                previousOpt = infinity
                if j > 0:
                    previousOpt = opt[i][j-1]
                    
                opt[i][j] = (min(topLeft,top,topRight) + A[i][j])
        minResult = infinity
        for i in range(0,n):
            if(minResult > opt[n-1][i]):
                minResult = opt[n-1][i]
        return minResult
                
