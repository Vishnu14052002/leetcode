def bubble(nums):
    for i in range(len(nums)):
        min = i
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                print(nums,i)
    print(nums)






nums = [9, 5, 7, 2]
bubble(nums)