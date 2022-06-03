class Solution:
    def rob(self, nums):
        # 1. access the length of the array
        len_arr = len(nums) # 4
        # 2. potential final value 1
        max_val_two_houses_ago = 0
        # 3. potential final value 2
        max_val_one_house_ago = 0
                    
        # 4. loop
        for i in range(len_arr): 
            cur_house_val = nums[i] # 1 --> 3 --> 2 --> 1
            rob_cur_house = max_val_two_houses_ago + cur_house_val
            skip_cur_house = max_val_one_house_ago
            max_val_two_houses_ago = max_val_one_house_ago # 4 --> 1 --> 1 --> 0
            max_val_one_house_ago = max(rob_cur_house, skip_cur_house) # 4 --> 4 --> 2 --> 1
        return max(max_val_two_houses_ago, max_val_one_house_ago) # 4


a=Solution()
a.rob([2,7,9,3,1])
