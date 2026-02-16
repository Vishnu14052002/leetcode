class Solution:
    def dummy(self, nums):
        res = 0 
        for i in nums:
            res = i ^ res
            print(res)
        print(res)
        print(2^1)








obj = Solution()
nums = [4,1,2,1,2]
obj.dummy(nums)

