class Solution:
    def dummy(self, nums):
        print(len(nums))
        p1 = 0
        for p2 in range( len(nums)):
            if nums[p1] < nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
                print(nums)
            

        print(nums, p1, p2)






obj = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]

obj.dummy(nums)

