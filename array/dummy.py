class Solution:
    def dummy(self, nums):
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            
            elif nums[i] == 0:
                if count > max_count:
                    max_count = count
                    count = 0
                count = 0
        
            if max_count > count:
                print('x',max_count)
                # return max_count
            else:
                print('xx',count)
                # return count


        


obj = Solution()
nums = [1,1,0,1,1,1]
a = obj.dummy(nums)
# print(a)
