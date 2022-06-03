class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i][1] > nums[j][1] and nums[i][0]>nums[j][1]:
                    print(dp[i])
                    print(dp[j])
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)

a = Solution()
a.lengthOfLIS([[2,3],[5,4],[6,4],[6,7]])
        