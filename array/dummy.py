class Solution:
    def dummy(self, nums):
        curr_count = 0
        fin_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            
            if nums[i] != 1:
                fin_count = curr_count
                curr_count = 0
        print(curr_count, fin_count)









obj = Solution()
nums = [1,1,0,1,1,1]

obj.dummy(nums)

