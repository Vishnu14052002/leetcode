class Solution:
    def isPowerOfTwo(self, n):
        if n == 1: return True
        elif n < 1 : return False
        return self.isPowerOfTwo(n/2)

obj = Solution()
val = obj.isPowerOfTwo(10)
print(val)