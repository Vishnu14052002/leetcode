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
                i += 1
            elif dummy[p1] <= nums2[p2]:
                nums1[i] = dummy[p1]
                p1 += 1
                i += 1
            print(p1,p2, i)
            print(nums1)
            
        if p1 < m:
            for ii in range(i, len(nums1)):
                nums1[ii] = dummy[p1]
                p1 += 1
        elif p2 < n: 
            for ii in range(i, len(nums1)):
                nums1[ii] = nums2[p2]
                p2 += 1
        print(nums1)


obj = Solution()
m = 3
n = 3
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
a = obj.dummy(nums1, nums2, m, n)
# print(a)
