class Solution:
    def dummy(self, nums1, nums2, m, n):
        dummy = nums1.copy()
        p1 = 0
        p2 = 0
        i = 0
        while p1 < m and p2 < n:
            if dummy[p1] >= nums2[p2]:
                nums1[i] =  nums2[p2]
                p2 += 1



obj = Solution()
m = 3
n = 3
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
a = obj.dummy(nums1, nums2, m, n)
# print(a)
