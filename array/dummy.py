class Solution:
    def dummy(self, nums1, nums2):
        p1 = 0
        p2 = 0
        dummy = nums1.copy()
        for i in range(len(nums1)):
            if dummy[p1] > nums2[p2]:
                nums1[i] = nums2[p2]
                p2 += 1
                print('first ',nums1, p1, p2)
            else:
                nums1[i] = dummy[p1]
                p1 += 1
                print('second ',nums1, p1, p2)
        


obj = Solution()
nums1 = [1, 3, 4, 7, 0, 0, 0, 0]
nums2 = [2, 5, 6, 8]
a = obj.dummy(nums1, nums2)
