class Solution(object):
    def pivotInteger(self, n):
        if n == 1:
            return 1
        else:
            l = [int(x) for x in range(1, n + 1)]
            a = len(l) - 1
            for i in range(len(l)):
                if sum(l[:a - i]) == sum(l[a - i - 1:]):
                    return l[a - i - 1:][0]
            return -1
print(Solution().pivotInteger(1))