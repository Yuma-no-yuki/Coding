class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = []
        for i in range(numRows):
            row = [1] * (i+1)
            if i >= 2 :
                for j in range(1,i):
                    row[j] = tri[i-1][j] + tri[i-1][j-1]
            tri.append(row)
        print(tri)
Solution().generate(5)