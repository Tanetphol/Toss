class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        x = len(obstacleGrid[0])-1
        y = len(obstacleGrid)-1
        def sol(x,y,obstacleGrid):
            if obstacleGrid[y][] == 1:
                return 0
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0
            ans = sol(x-1,y,obstacleGrid) + sol(x,y-1,obstacleGrid)
            return ans
        return sol(x,y,obstacleGrid)
a=Solution()
a.uniquePathsWithObstacles([[0,0,]])


