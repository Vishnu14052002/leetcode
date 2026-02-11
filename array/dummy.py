class Solution:
    def dummy(self, nums1, nums2, m, n):
        dnum1 = nums1.copy()
        p1 = 0
        p2 = 0

        for i in range(len(nums1)):
            if p2 >= n or (p1 < m and dnum1[p1] < nums2[p2]):
                nums1[i] = dnum1[p1]
                p1 += 1

            else:
                nums1[i] = nums2[p2]
                p2 += 1

            print(nums1)


        print(nums1)




obj = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [1,1,1]
n = 3

obj.dummy(nums1, nums2, m, n)

