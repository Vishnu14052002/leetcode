class Solution:
    def dummy(self, nums, target):
        left = 0
        right = len(nums) - 1
        print(right)
        while(right >= left):
            middle = int((left + right) / 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                print(nums[middle], 'nums[middle]')
                left = middle + 1
            else:
                right = middle - 1
            print('middle',middle)
            print('right',right)
            print('left',left)
        return -1
            


            





obj = Solution()
target = 12
nums = [-1,0,3,5,9,12]
a = obj.dummy(nums, target)
print(a)
