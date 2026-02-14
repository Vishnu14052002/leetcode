class Solution:
    def dummy(self, s):
        leng = int(len(s) / 2)
        p2 = len(s)-1
        print(p2)
        for p1 in range(leng):
            s[p1], s[p2] = s[p2], s[p1]
            p2 -= 1
            
        print(s)









obj = Solution()
s = ["h","e","l","l","o"]
obj.dummy(s)

