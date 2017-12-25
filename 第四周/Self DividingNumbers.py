class Solution(object):
    def findComplement(self, num):
        t = num
        c = 1 << 31
        count = 0
        while t&c != c:
            count += 1
            t = t << 1
        m=0
        for i in range(32 - count):
            m = m << 1
            m += 1
        return m^num

solution = Solution()
num = 5
print(solution.findComplement(num))