class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                ans += 1
                left += 1
                right -= 1
            elif cur < k:
                left += 1
            else:
                right -= 1
        asd
        return ans
a=Solution()
a.maxOperations([1,1,2,1,2,1,1],2)