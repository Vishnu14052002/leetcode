class Solution:
    def dummy(self, nums):
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1 
        for i in range(p1, len(nums)):
            nums[i] = 0 
            
        return nums


            


            





obj = Solution()
nums = [1]
a = obj.dummy(nums)
print(a)
