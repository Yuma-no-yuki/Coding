class Solution(object):
    def getRow(self, rowIndex):
        rowIndex +=1
        tri = []
        for i in range(rowIndex):
            row = [1] * (i+1)
            if i >= 2 :
                for j in range(1,i):
                    row[j] = tri[i-1][j] + tri[i-1][j-1]
            tri.append(row)
        return row
        
